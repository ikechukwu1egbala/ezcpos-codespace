import 'package:flutter/material.dart';

import '../../core/api.dart';

class SalesPage extends StatefulWidget {
  const SalesPage({super.key});

  @override
  State<SalesPage> createState() => _SalesPageState();
}

class _SalesPageState extends State<SalesPage> {
  bool loading = true;
  String? error;
  List<dynamic> products = [];
  List<Map<String, dynamic>> cart = [];
  String statusMessage = '';
  String? selectedCustomer; 

  @override
  void initState() {
    super.initState();
    loadProducts();
  }

  Future<void> loadProducts() async {
    try {
      setState(() {
        loading = true;
        error = null;
      });

      final response = await Api.instance.get('/pos/products/');
      final data = response is Map ? (response['results'] ?? response['data'] ?? response) : response;
      if (data is List) {
        products = data;
      }
    } catch (e) {
      error = e.toString();
    } finally {
      if (mounted) {
        setState(() => loading = false);
      }
    }
  }

  void addToCart(Map<String, dynamic> product) {
    final productId = product['id'];
    final existingIndex = cart.indexWhere((item) => item['product_id'] == productId);

    if (existingIndex >= 0) {
      final updated = Map<String, dynamic>.from(cart[existingIndex]);
      updated['quantity'] = (updated['quantity'] as num) + 1;
      cart[existingIndex] = updated;
    } else {
      cart.add({
        'product_id': productId,
        'name': product['name'],
        'quantity': 1,
        'unit_price': double.tryParse('${product['selling_price'] ?? 0}') ?? 0.0,
      });
    }

    setState(() {});
  }

  void updateCartQuantity(int index, int change) {
    final item = cart[index];
    final next = (item['quantity'] as num).toInt() + change;
    if (next <= 0) {
      cart.removeAt(index);
    } else {
      item['quantity'] = next;
    }
    setState(() {});
  }

  double get subtotal => cart.fold(0.0, (sum, item) {
    final qty = (item['quantity'] as num).toDouble();
    final price = (item['unit_price'] as num).toDouble();
    return sum + (qty * price);
  });

  Future<void> checkout() async {
    if (cart.isEmpty) {
      setState(() => statusMessage = 'Cart is empty');
      return;
    }

    setState(() => statusMessage = 'Processing sale...');

    try {
      final items = cart.map((item) {
        return {
          'product': item['product_id'],
          'quantity': item['quantity'],
          'unit_price': item['unit_price'],
        };
      }).toList();

      final result = await Api.instance.post('/pos/sales/', {
        'customer': selectedCustomer,
        'amount_paid': subtotal,
        'discount': 0,
        'items': items,
      });

      setState(() {
        cart.clear();
        statusMessage = 'Sale completed successfully';
      });

      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Sale #${result['id']} saved.')),
        );
      }
    } catch (e) {
      setState(() => statusMessage = 'Checkout failed: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    if (loading) {
      return const Center(child: CircularProgressIndicator());
    }

    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.all(12),
          child: InputDecorator(
            decoration: InputDecoration(
              labelText: 'Customer',
              border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
            ),
            child: DropdownButtonHideUnderline(
              child: DropdownButton<String>(
                value: selectedCustomer,
                isExpanded: true,
                hint: const Text('Walk-in customer'),
                items: const [
                  DropdownMenuItem(value: null, child: Text('Walk-in customer')),
                ],
                onChanged: (value) => setState(() => selectedCustomer = value),
              ),
            ),
          ),
        ),
        Expanded(
          child: Row(
            children: [
              Expanded(
                flex: 3,
                child: ListView.builder(
                  itemCount: products.length,
                  padding: const EdgeInsets.all(12),
                  itemBuilder: (context, index) {
                    final product = products[index] as Map<String, dynamic>;
                    final name = product['name'] ?? 'Product';
                    final price = double.tryParse('${product['selling_price'] ?? 0}') ?? 0.0;
                    final stock = double.tryParse('${product['stock_quantity'] ?? 0}') ?? 0.0;

                    return Card(
                      margin: const EdgeInsets.only(bottom: 8),
                      child: ListTile(
                        title: Text(name),
                        subtitle: Text('Stock: ${stock.toStringAsFixed(0)} • ${product['unit'] ?? 'piece'}'),
                        trailing: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Text('₦${price.toStringAsFixed(2)}'),
                            const SizedBox(height: 4),
                            ElevatedButton(
                              onPressed: () => addToCart(product),
                              child: const Text('Add'),
                            ),
                          ],
                        ),
                      ),
                    );
                  },
                ),
              ),
              Expanded(
                flex: 2,
                child: Container(
                  color: Colors.white,
                  padding: const EdgeInsets.all(12),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      const Text(
                        'Current Cart',
                        style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                      ),
                      const SizedBox(height: 12),
                      if (cart.isEmpty)
                        const Expanded(
                          child: Center(child: Text('Cart is empty')),
                        )
                      else
                        Expanded(
                          child: ListView.builder(
                            itemCount: cart.length,
                            itemBuilder: (context, index) {
                              final item = cart[index];
                              final qty = (item['quantity'] as num).toInt();
                              final price = (item['unit_price'] as num).toDouble();

                              return Card(
                                child: ListTile(
                                  title: Text(item['name']),
                                  subtitle: Text('₦${price.toStringAsFixed(2)} each'),
                                  trailing: Row(
                                    mainAxisSize: MainAxisSize.min,
                                    children: [
                                      IconButton(
                                        onPressed: () => updateCartQuantity(index, -1),
                                        icon: const Icon(Icons.remove_circle_outline),
                                      ),
                                      Text('$qty'),
                                      IconButton(
                                        onPressed: () => updateCartQuantity(index, 1),
                                        icon: const Icon(Icons.add_circle_outline),
                                      ),
                                    ],
                                  ),
                                ),
                              );
                            },
                          ),
                        ),
                      const Divider(),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          const Text('Subtotal'),
                          Text('₦${subtotal.toStringAsFixed(2)}'),
                        ],
                      ),
                      const SizedBox(height: 12),
                      FilledButton.icon(
                        onPressed: cart.isEmpty ? null : checkout,
                        icon: const Icon(Icons.payment),
                        label: const Text('Checkout'),
                      ),
                      if (statusMessage.isNotEmpty) ...[
                        const SizedBox(height: 10),
                        Text(statusMessage, style: const TextStyle(fontSize: 12)),
                      ],
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
