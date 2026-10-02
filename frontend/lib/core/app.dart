import 'package:flutter/material.dart';
import 'features/auth/login_page.dart';
import 'features/dashboard/dashboard_page.dart';
import 'features/products/products_page.dart';
import 'features/sales/sales_page.dart';
import 'features/customers/customers_page.dart';
import 'features/expenses/expenses_page.dart';
import 'features/settings/settings_page.dart';
import 'features/operations/operations_page.dart';
class EzcPosApp extends StatelessWidget { const EzcPosApp({super.key});
 @override Widget build(BuildContext context)=>MaterialApp(title:'EZC POS',debugShowCheckedModeBanner:false,theme:ThemeData(useMaterial3:true,colorSchemeSeed:const Color(0xff8B5E34),scaffoldBackgroundColor:const Color(0xfffaf7f2)),home:const LoginPage());}
class HomeShell extends StatefulWidget { const HomeShell({super.key}); @override State<HomeShell> createState()=>_HomeShellState();}
class _HomeShellState extends State<HomeShell>{int index=0; final pages=const [DashboardPage(),ProductsPage(),SalesPage(),OperationsPage(),CustomersPage(),ExpensesPage(),SettingsPage()]; final labels=['Dashboard','Products','Sales','Operations','Customers','Expenses','Settings']; final icons=[Icons.dashboard,Icons.inventory_2,Icons.point_of_sale,Icons.hub,Icons.people,Icons.receipt_long,Icons.settings]; @override Widget build(BuildContext c)=>Scaffold(appBar:AppBar(title:Text('EZC POS • ${labels[index]}'),actions:[IconButton(onPressed:()=>setState((){}),icon:const Icon(Icons.sync))]),body:pages[index],bottomNavigationBar:NavigationBar(selectedIndex:index,onDestinationSelected:(v)=>setState(()=>index=v),destinations:[for(int i=0;i<labels.length;i++)NavigationDestination(icon:Icon(icons[i]),label:labels[i])],));}
