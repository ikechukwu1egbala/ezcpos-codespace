import 'package:flutter/material.dart';

import '../../core/api.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final user = TextEditingController(text: 'demo');
  final pass = TextEditingController(text: 'demo1234');

  bool loading = false;
  String? error;

  Future<void> login() async {
    setState(() {
      loading = true;
      error = null;
    });

    try {
      final api = Api.instance;
      await api.init();
      final response = await api.post('/auth/token/', {
        'username': user.text.trim(),
        'password': pass.text,
      });

      final access = response['access'];
      if (access is String && access.isNotEmpty) {
        await api.saveToken(access);
        if (mounted) {
          Navigator.of(context).pushReplacement(
            MaterialPageRoute(builder: (_) => const HomeShell()),
          );
        }
      } else {
        setState(() => error = 'Login failed. Please check your backend credentials.');
      }
    } catch (e) {
      if (mounted) {
        setState(() => error = 'Login failed. Create a user with the backend setup command.');
      }
    } finally {
      if (mounted) {
        setState(() => loading = false);
      }
    }
  }

  @override
  void dispose() {
    user.dispose();
    pass.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF7A4A1D), Color(0xFFF2B544)],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 440),
            child: Padding(
              padding: const EdgeInsets.all(24),
              child: Card(
                elevation: 8,
                child: Padding(
                  padding: const EdgeInsets.all(24),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Container(
                        width: 80,
                        height: 80,
                        decoration: BoxDecoration(
                          color: const Color(0xFFF2B544).withAlpha(30),
                          borderRadius: BorderRadius.circular(20),
                        ),
                        child: const Icon(Icons.storefront_rounded, size: 44, color: Color(0xFF7A4A1D)),
                      ),
                      const SizedBox(height: 16),
                      const Text(
                        'EZC POS',
                        style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
                      ),
                      const SizedBox(height: 8),
                      const Text('Retail & wholesale operations', style: TextStyle(color: Colors.black54)),
                      const SizedBox(height: 24),
                      TextField(
                        controller: user,
                        decoration: const InputDecoration(
                          labelText: 'Username',
                          prefixIcon: Icon(Icons.person_outline),
                        ),
                      ),
                      const SizedBox(height: 14),
                      TextField(
                        controller: pass,
                        obscureText: true,
                        decoration: const InputDecoration(
                          labelText: 'Password',
                          prefixIcon: Icon(Icons.lock_outline),
                        ),
                      ),
                      if (error != null)
                        Padding(
                          padding: const EdgeInsets.only(top: 16),
                          child: Text(error!, style: const TextStyle(color: Colors.red)),
                        ),
                      const SizedBox(height: 22),
                      SizedBox(
                        width: double.infinity,
                        child: FilledButton.icon(
                          onPressed: loading ? null : login,
                          icon: const Icon(Icons.login_rounded),
                          label: Text(loading ? 'Signing in…' : 'Sign in'),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
