import 'package:flutter/material.dart';
import '../../core/api.dart';

class OperationsPage extends StatelessWidget {
  const OperationsPage({super.key});

  static const items = <Map<String, dynamic>>[
    {'title':'Suppliers','icon':Icons.local_shipping,'path':'/commerce/suppliers/'},
    {'title':'Warehouses','icon':Icons.warehouse,'path':'/commerce/warehouses/'},
    {'title':'Stock in transit','icon':Icons.swap_horiz,'path':'/commerce/transfers/'},
    {'title':'Consignments','icon':Icons.inventory,'path':'/commerce/consignments/'},
    {'title':'Currencies & rates','icon':Icons.currency_exchange,'path':'/commerce/currencies/'},
    {'title':'Recognition dataset','icon':Icons.camera_alt,'path':'/commerce/recognition-datasets/'},
  ];

  Future<void> open(BuildContext context, String title, String path) async {
    try {
      final data = await Api.instance.get(path);
      if (!context.mounted) return;
      final list = (data['results'] ?? data['data'] ?? data) as dynamic;
      showModalBottomSheet(context: context, showDragHandle: true,
        builder: (_) => Padding(padding: const EdgeInsets.all(20), child: ListView(
          children: [Text(title, style: Theme.of(context).textTheme.headlineSmall),
            const SizedBox(height: 12), Text(list.toString())])));
    } catch (e) {
      if (!context.mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('$title unavailable: $e')));
    }
  }

  @override
  Widget build(BuildContext context) => ListView.separated(
    padding: const EdgeInsets.all(16),
    itemCount: items.length,
    separatorBuilder: (_, __) => const SizedBox(height: 8),
    itemBuilder: (_, i) {
      final item = items[i];
      return Card(child: ListTile(
        leading: Icon(item['icon'] as IconData),
        title: Text(item['title'] as String),
        subtitle: Text(item['path'] as String),
        trailing: const Icon(Icons.chevron_right),
        onTap: () => open(context, item['title'] as String, item['path'] as String),
      ));
    },
  );
}
