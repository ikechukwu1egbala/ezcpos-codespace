import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class Api {
  Api._();

  static final instance = Api._();

  final String baseUrl = const String.fromEnvironment(
    'EZC_API_URL',
    defaultValue: 'http://127.0.0.1:8000/api',
  );

  String? accessToken;

  Future<void> init() async {
    final prefs = await SharedPreferences.getInstance();
    accessToken = prefs.getString('ezc_access_token');
  }

  Future<void> saveToken(String token) async {
    accessToken = token;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('ezc_access_token', token);
  }

  Map<String, String> get authHeaders => {
    if (accessToken != null && accessToken!.isNotEmpty)
      'Authorization': 'Bearer $accessToken',
  };

  Future<dynamic> get(String path) async {
    final response = await http.get(
      Uri.parse('$baseUrl$path'),
      headers: {
        'Content-Type': 'application/json',
        ...authHeaders,
      },
    );
    return _decode(response);
  }

  Future<dynamic> post(String path, [Map<String, dynamic>? body]) async {
    final response = await http.post(
      Uri.parse('$baseUrl$path'),
      headers: {
        'Content-Type': 'application/json',
        ...authHeaders,
      },
      body: body == null ? null : jsonEncode(body),
    );
    return _decode(response);
  }

  dynamic _decode(http.Response response) {
    final body = response.body.trim();
    if (body.isEmpty) {
      return {};
    }

    try {
      final decoded = jsonDecode(body);
      if (response.statusCode >= 400) {
        throw ApiException(response.statusCode, decoded);
      }
      return decoded;
    } catch (e) {
      if (response.statusCode >= 400) {
        throw ApiException(response.statusCode, {'detail': body});
      }
      throw FormatException('Invalid API response: $body');
    }
  }
}

class ApiException implements Exception {
  ApiException(this.statusCode, this.details);

  final int statusCode;
  final dynamic details;

  @override
  String toString() => 'ApiException($statusCode): $details';
}
