import 'package:flutter/material.dart';
import '../../core/api.dart';
class CustomersPage extends StatefulWidget{const CustomersPage({super.key});@override State<CustomersPage> createState()=>_CustomersPageState();}
class _CustomersPageState extends State<CustomersPage>{List<dynamic> a=[];bool busy=true;@override void initState(){super.initState();load();}Future<void>load()async{try{final r=await Api.instance.get('/customers/');a=(r['results']??[]) as List<dynamic>;}catch(_){ }setState(()=>busy=false);}@override Widget build(BuildContext c)=>busy?const Center(child:CircularProgressIndicator()):ListView.builder(itemCount:a.length,itemBuilder:(_,i){final x=a[i];return ListTile(leading:const CircleAvatar(child:Icon(Icons.person)),title:Text(x['name']),subtitle:Text(x['phone']??''));});}
