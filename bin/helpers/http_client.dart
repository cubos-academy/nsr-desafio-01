import 'dart:convert';

import 'package:http/http.dart' as http;

interface class HttpResponse {
  final int statusCode;
  final dynamic body;

  HttpResponse({
    required this.statusCode,
    required this.body,
  });
}

class HttpClient {
  Future<HttpResponse> get(
    String url, {
    Map<String, String>? queryParameters,
  }) async {
    queryParameters ??= {};

    String query = '?';

    for (var element in queryParameters.entries) {
      query += '${element.key}=${element.value}&';
    }

    if (query != '?') {
      url += query;
    }

    final uri = Uri.parse(url);

    return adpatResponse(
      await http.get(uri),
    );
  }

  HttpResponse adpatResponse(http.Response response) {
    late final dynamic body;

    try {
      body = jsonDecode(response.body);
    } catch (e) {
      return HttpResponse(
        statusCode: response.statusCode,
        body: response.body,
      );
    }

    return HttpResponse(
      statusCode: response.statusCode,
      body: body,
    );
  }
}
