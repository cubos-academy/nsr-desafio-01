import 'dart:io';

import './nasa_service.dart';
import '../helpers/env.dart';
import '../helpers/http_client.dart';
import '../models/nasa_apod_model.dart';
import '../models/telegram_update_model.dart';

class TelegramService {
  final HttpClient _httpClient;
  final NASAService _nasaService;
  final kTelegramToken = Env.instance.get('TELEGRAM_API_KEY');
  final kTelegramBaseURL = Env.instance.get('TELEGRAM_BASE_URL');
  final kNGROKDomain = Env.instance.get('NGROK_DOMAIN');

  int offset = 0;

  TelegramService(
      {required NASAService nasaService, required HttpClient httpClient})
      : _httpClient = httpClient,
        _nasaService = nasaService;

  init() async {
    setWebhook();
  }

  setWebhook() async {
    print('Setting webhook with domain: $kNGROKDomain');
    var response = await _httpClient.get(
      '$kTelegramBaseURL/bot$kTelegramToken/setWebhook',
      queryParameters: {
        'url': kNGROKDomain,
        'allowedUpdates': '["message"]',
      },
    );

    if (response.statusCode != 200) {
      print('Error: ${response.statusCode}');
      exit(0);
    }
  }

  checkUpdates(TelegramUpdate update) async {
    if (update.message.text == '') {
      return;
    }

    final command = update.message.text;
    final chatId = update.message.chat.id;

    print(
      'Sending APOD on chat id $chatId id, with command $command',
    );

    if (command.contains('/apod')) {
      late final DateTime date;

      final splitCommand = command.split(' ');

      if (splitCommand.length == 1) {
        sendAPODMessage(chatId.toString());
        return;
      }

      try {
        final dateParts = splitCommand[1].split('/');
        if (dateParts.length != 3) {
          throw Exception('Invalid date format');
        }
        date = DateTime(
          int.parse(dateParts[2]),
          int.parse(dateParts[1]),
          int.parse(dateParts[0]),
        );

        sendAPODMessage(chatId.toString(), date: date);
        return;
      } catch (e) {
        print(e);
        sendTextMessage(
          chatId.toString(),
          'Data inválida. Tente novamente. \nFormato aceito: dd/mm/yyyy',
        );
      }
    } else if (command == '/help' || command == '/start') {
      sendTextMessage(
        chatId.toString(),
        'Comandos disponíveis: \n/apod dd/mm/yyyy - Busca a imagem da data informada. \n/apod - Busca a imagem do dia atual. \n/about - Informações sobre o bot. \n/help - Lista de comandos disponíveis.',
      );
    } else if (command == '/about') {
      sendTextMessage(chatId.toString(),
          'Bot desenvolvido por @vinisoaresr. \nCódigo fonte disponível em: https://github.com/vinisoaresr/nsr-desafio-01');
    } else {
      sendTextMessage(
        chatId.toString(),
        'Comando não reconhecido. Tente novamente.',
      );
    }
  }

  sendAPODMessage(String chatId, {DateTime? date}) async {
    late final NASAApodModel nasaApodModel;

    if (date != null) {
      nasaApodModel = await _nasaService.getAPODByDate(date);
    } else {
      nasaApodModel = await _nasaService.getCurrentAPOD();
    }

    _httpClient.get(
      '$kTelegramBaseURL/bot$kTelegramToken/sendMessage',
      queryParameters: {
        'chat_id': chatId,
        'text': nasaApodModel.toString(),
      },
    );
  }

  sendTextMessage(String chatId, String errorMessage) async {
    _httpClient.get(
      '$kTelegramBaseURL/bot$kTelegramToken/sendMessage',
      queryParameters: {
        'chat_id': chatId,
        'text': errorMessage,
      },
    );
  }
}
