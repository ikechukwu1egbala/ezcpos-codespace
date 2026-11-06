from decimal import Decimal

from django.db import transaction
from django.db.models import Sum
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Category, Customer, Product, Sale, SaleItem
from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, SaleSerializer


def scope_business(queryset, user):
    if not user or not getattr(user, "business", None):
        return queryset.none()
    return queryset.filter(business=user.business)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return scope_business(Category.objects.all(), self.request.user)

    def perform_create(self, serializer):
        serializer.save(business=self.request.user.business)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return scope_business(Product.objects.select_related("category").all(), self.request.user)

    def perform_create(self, serializer):
        serializer.save(business=self.request.user.business)


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return scope_business(Customer.objects.all(), self.request.user)

    def perform_create(self, serializer):
        serializer.save(business=self.request.user.business)


class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer

    def get_queryset(self):
        return scope_business(Sale.objects.prefetch_related("items__product"), self.request.user).order_by("-created_at")

    def create(self, request, *args, **kwargs):
        user = request.user
        payload = request.data
        items = payload.get("items") or []
        if not items:
            raise ValidationError({"items": "At least one sale item is required."})

        subtotal = Decimal("0")
        sale_items = []
        with transaction.atomic():
            for raw in items:
                product_id = raw.get("product") or raw.get("product_id")
                if not product_id:
                    raise ValidationError({"items": "Each item must include a product."})
                try:
                    product = Product.objects.select_for_update().get(pk=product_id, business=user.business)
                except Product.DoesNotExist:
                    raise ValidationError({"items": f"Product {product_id} was not found in this business."})

                quantity = Decimal(str(raw.get("quantity", 0)))
                if quantity <= 0:
                    raise ValidationError({"items": "Quantity must be greater than zero."})
                if product.stock_quantity < quantity:
                    raise ValidationError({"items": f"Insufficient stock for {product.name}. Available: {product.stock_quantity}"})

                unit_price = Decimal(str(raw.get("unit_price", product.selling_price)))
                item_total = quantity * unit_price
                subtotal += item_total
                product.stock_quantity -= quantity
                product.save(update_fields=["stock_quantity"])

                sale_items.append(
                    {
                        "product": product,
                        "quantity": quantity,
                        "unit_price": unit_price,
                        "line_total": item_total,
                    }
                )

            discount = Decimal(str(payload.get("discount", 0)))
            amount_paid = Decimal(str(payload.get("amount_paid", 0)))
            total = subtotal - discount
            if total < 0:
                total = Decimal("0")

            payment_status = "paid" if amount_paid >= total else "partial" if amount_paid > 0 else "unpaid"
            sale = Sale.objects.create(
                business=user.business,
                branch=getattr(user, "branch", None),
                cashier=user,
                customer_id=payload.get("customer") or None,
                subtotal=subtotal,
                discount=discount,
                total=total,
                amount_paid=amount_paid,
                payment_status=payment_status,
                operation_id=None,
            )

            for item in sale_items:
                SaleItem.objects.create(
                    sale=sale,
                    product=item["product"],
                    quantity=item["quantity"],
                    unit_price=item["unit_price"],
                    line_total=item["line_total"],
                )

        serializer = self.get_serializer(sale)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"])
    def summary(self, request):
        qs = self.get_queryset()
        total_sales = qs.aggregate(v=Sum("total")) ["v"] or Decimal("0")
        return Response({
            "sales_count": qs.count(),
            "total_sales": float(total_sales),
        })
