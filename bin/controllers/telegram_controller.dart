import 'dart:convert';

import 'package:shelf/shelf.dart';

import '../models/telegram_update_model.dart';
import '../services/telegram_service.dart';

class TelegramController {
  final TelegramService _telegramService;

  TelegramController({required TelegramService telegramService})
      : _telegramService = telegramService;

  Future<Response> getUpdatesFromWebhook(Request req) async {
    req.readAsString().then((jsonString) {
      final json = jsonDecode(jsonString);
      final update = TelegramUpdate.fromJson(json);

      _telegramService.checkUpdates(update);
    });

    return Response.ok('');
  }
}
