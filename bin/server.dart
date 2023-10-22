import 'dart:io';

import 'package:intl/date_symbol_data_local.dart';
import 'package:shelf/shelf.dart';
import 'package:shelf/shelf_io.dart';

import './controllers/telegram_controller.dart';
import './helpers/http_client.dart';
import './main/routes.dart';
import './services/telegram_service.dart';
import 'services/nasa_service.dart';

void main(List<String> args) async {
  init();

  var routes = Routes(telegramController: TelegramController());

  final handler = Pipeline()
      .addMiddleware(
        logRequests(),
      )
      .addHandler(
        routes.router,
      );

  final port = int.parse(Platform.environment['PORT'] ?? '8080');

  final ip = InternetAddress.anyIPv4;

  final server = await serve(handler, ip, port);

  print('Server listening on ${ip.address}:${server.port}');
}

void init() {
  initializeDateFormatting('pt_BR');

  final client = HttpClient();

  final telegramService = TelegramService(
    httpClient: client,
    nasaService: NASAService(httpClient: client),
  );

  telegramService.init();
}
