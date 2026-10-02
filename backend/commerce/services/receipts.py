from html import escape
from decimal import Decimal

def render_receipt_html(sale, template=None):
    template = template or getattr(getattr(sale, "business", None), "receipt_template", None)
    title = escape(getattr(template, "title", "Sales Receipt"))
    footer = escape(getattr(template, "footer", "Thank you for your purchase!"))
    currency = getattr(getattr(sale, "currency", None), "symbol", "₦")
    rows=[]
    for item in sale.items.select_related("product").all():
        total=Decimal(item.quantity)*Decimal(item.unit_price)
        rows.append(f"<tr><td>{escape(item.product.name)}</td><td>{item.quantity}</td><td>{currency}{total:,.2f}</td></tr>")
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>{title}</title><style>body{{font-family:monospace;max-width:420px;margin:auto;padding:16px}}table{{width:100%;border-collapse:collapse}}td{{padding:5px 0;border-bottom:1px dashed #999}}.total{{font-size:20px;font-weight:700;text-align:right}}</style></head><body><h2>{title}</h2><p>Invoice: {sale.id}<br>{sale.created_at:%Y-%m-%d %H:%M}</p><table>{''.join(rows)}</table><p class="total">TOTAL {currency}{Decimal(sale.total):,.2f}</p><p style="text-align:center">{footer}</p></body></html>'''
