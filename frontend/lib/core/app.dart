import 'package:flutter/material.dart';

import '../features/auth/login_page.dart';
import '../features/dashboard/dashboard_page.dart';
import '../features/products/products_page.dart';
import '../features/sales/sales_page.dart';
import '../features/operations/operations_page.dart';
import '../features/customers/customers_page.dart';
import '../features/expenses/expenses_page.dart';
import '../features/settings/settings_page.dart';

class EzcPosApp extends StatelessWidget {
  const EzcPosApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'EZC POS',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorSchemeSeed: const Color(0xff8B5E34),
        scaffoldBackgroundColor: const Color(0xfffaf7f2),
      ),
      home: LoginPage(),
    );
  }
}

class HomeShell extends StatefulWidget {
  const HomeShell({super.key});

  @override
  State<HomeShell> createState() => _HomeShellState();
}

class _HomeShellState extends State<HomeShell> {
  int index = 0;

  final labels = const [
    'Dashboard',
    'Products',
    'Sales',
    'Operations',
    'Customers',
    'Expenses',
    'Settings',
  ];

  final icons = const [
    Icons.dashboard,
    Icons.inventory_2,
    Icons.point_of_sale,
    Icons.hub,
    Icons.people,
    Icons.receipt_long,
    Icons.settings,
  ];

  late final List<Widget> pages = [
    const DashboardPage(),
    const ProductsPage(),
    const SalesPage(),
    const OperationsPage(),
    const CustomersPage(),
    const ExpensesPage(),
    const SettingsPage(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('EZC POS ${labels[index]}'),
        actions: [IconButton(onPressed: () {}, icon: const Icon(Icons.sync))],
      ),
      body: pages[index],
      bottomNavigationBar: NavigationBar(
        selectedIndex: index,
        onDestinationSelected: (value) {
          setState(() => index = value);
        },
        destinations: [
          for (int i = 0; i < labels.length; i++)
            NavigationDestination(icon: Icon(icons[i]), label: labels[i]),
        ],
      ),
    );
  }
}
