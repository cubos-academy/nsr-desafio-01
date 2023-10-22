import 'package:shelf/shelf.dart';
import 'package:shelf_router/shelf_router.dart';

import '../controllers/telegram_controller.dart';

class Routes {
  final TelegramController _telegramController;

  Routes({required TelegramController telegramController})
      : _telegramController = telegramController;

  Router get router {
    final router = Router();

    // final nasaService = NASAService(
    //   httpClient: HttpClient(),
    // );

    router.get('/', (Request request) {
      return _telegramController.sayHelloTelegram(request);
    });

    return router;
  }
}
