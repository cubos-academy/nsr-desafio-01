import 'package:shelf/shelf.dart';
import 'package:shelf_router/shelf_router.dart';

import '../controllers/telegram_controller.dart';

class Routes {
  final TelegramController _telegramController;

  Routes({required TelegramController telegramController})
      : _telegramController = telegramController;

  Router get router {
    final router = Router();

    router.post('/', (Request request) {
      return _telegramController.getUpdatesFromWebhook(request);
    });

    return router;
  }
}
