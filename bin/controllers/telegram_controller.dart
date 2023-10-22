import 'package:shelf/shelf.dart';

class TelegramController {
  Response sayHelloTelegram(Request req) {
    final name = req.url.queryParameters['name'] ?? 'World';
    return Response.ok('Hello, $name');
  }
}
