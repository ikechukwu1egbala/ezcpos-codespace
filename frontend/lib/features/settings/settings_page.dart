import 'package:flutter/material.dart';
class SettingsPage extends StatelessWidget{const SettingsPage({super.key});@override Widget build(BuildContext c)=>ListView(children:const[AboutListTile(icon:Icon(Icons.store),applicationName:'EZC POS',applicationVersion:'1.0.0'),ListTile(leading:Icon(Icons.sync),title:Text('Sync status'),subtitle:Text('Offline queue architecture enabled'))]);}
