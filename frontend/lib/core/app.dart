import 'package:flutter/material.dart';

class EzcPosApp extends StatelessWidget {
  const EzcPosApp({super.key});

  @override
  Widget build(BuildContext context) {
    const brown = Color(0xFF7A4A1D);
    const amber = Color(0xFFF2B544);
    const cream = Color(0xFFFAF5ED);
    const deepBrown = Color(0xFF40230D);

    final theme = ThemeData(
      useMaterial3: true,
      scaffoldBackgroundColor: cream,
      colorScheme: ColorScheme.fromSeed(
        seedColor: brown,
        primary: brown,
        secondary: amber,
        surface: Colors.white,
        brightness: Brightness.light,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: brown,
        foregroundColor: Colors.white,
      ),
      navigationBarTheme: NavigationBarThemeData(
        backgroundColor: Colors.white,
        indicatorColor: amber.withAlpha(50),
        labelTextStyle: WidgetStateProperty.all(
          const TextStyle(fontWeight: FontWeight.w600),
        ),
      ),
      cardTheme: CardThemeData(
        color: Colors.white,
        elevation: 2,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      ),
      inputDecorationTheme: InputDecorationTheme(
        fillColor: Colors.white,
        filled: true,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: BorderSide(color: brown.withAlpha(40)),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: const BorderSide(color: brown, width: 1.5),
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: brown,
          foregroundColor: Colors.white,
          minimumSize: const Size.fromHeight(48),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      ),
      floatingActionButtonTheme: const FloatingActionButtonThemeData(
        backgroundColor: amber,
        foregroundColor: deepBrown,
      ),
    );

    return MaterialApp(
      title: 'EZC POS',
      debugShowCheckedModeBanner: false,
      theme: theme,
      home: const LoginPage(),
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
        title: Text('EZC POS • ${labels[index]}'),
        actions: [
          IconButton(
            onPressed: () {},
            icon: const Icon(Icons.sync),
            tooltip: 'Sync',
          ),
        ],
      ),
      body: pages[index],
      bottomNavigationBar: NavigationBar(
        selectedIndex: index,
        onDestinationSelected: (value) => setState(() => index = value),
        destinations: [
          for (int i = 0; i < labels.length; i++)
            NavigationDestination(icon: Icon(icons[i]), label: labels[i]),
        ],
      ),
    );
  }
}
