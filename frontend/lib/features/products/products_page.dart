import 'package:flutter/material.dart';

import '../core/api.dart';

class ProductsPage extends StatefulWidget {
  const ProductsPage({super.key});

  @override
  State<ProductsPage> createState() => _ProductsPageState();
}

class _ProductsPageState extends State<ProductsPage> {
  bool loading = true;
  String? error;
  List<dynamic> items = [];

  @override
  void initState() {
    super.initState();
    load();
  }

  Future<void> load() async {
    setState(() {
      loading = true;
      error = null;
    });

    try {
      final response = await Api.instance.get('/pos/products/');
      final data = response is Map ? (response['results'] ?? response['data'] ?? response) : response;
      if (data is List) {
        items = data;
      } else {
        items = [];
      }
    } catch (e) {
      error = e.toString();
    }

    if (mounted) {
      setState(() => loading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    if (loading) {
      return const Center(child: CircularProgressIndicator());
    }

    if (error != null) {
      return RefreshIndicator(
        onRefresh: load,
        child: ListView(
          children: [
            const SizedBox(height: 160),
            Padding(
              padding: const EdgeInsets.all(16),
              child: Text('Unable to load products\n$error'),
            ),
          ],
        ),
      );
    }

    if (items.isEmpty) {
      return RefreshIndicator(
        onRefresh: load,
        child: ListView(
          children: const [
            SizedBox(height: 160),
            Center(child: Text('No products found')),
          ],
        ),
      );
    }

    return RefreshIndicator(
      onRefresh: load,
      child: ListView.builder(
        padding: const EdgeInsets.all(12),
        itemCount: items.length,
        itemBuilder: (context, index) {
          final product = items[index];
          if (product is! Map) {
            return const SizedBox.shrink();
          }

          final name = product['name']?.toString() ?? 'Unnamed product';
          final sku = product['sku']?.toString() ?? '';
          final unit = product['unit']?.toString() ?? 'piece';
          final price = double.tryParse('${product['selling_price'] ?? 0}') ?? 0;
          final stock = double.tryParse('${product['stock_quantity'] ?? 0}') ?? 0;

          return Card(
            margin: const EdgeInsets.only(bottom: 10),
            child: ListTile(
              title: Text(name, style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text([
                if (sku.isNotEmpty) 'SKU: $sku',
                'Unit: $unit',
                'Stock: ${stock.toStringAsFixed(0)}',
              ].join('  ')),
              trailing: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  const Text('Selling price'),
                  Text(
                    '₦${price.toStringAsFixed(2)}',
                    style: const TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Color(0xFF7A4A1D),
                    ),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
