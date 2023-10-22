import 'dart:async';

import '../helpers/env.dart';
import '../helpers/http_client.dart';
import '../models/nasa_apod_model.dart';
import 'nasa_service.dart';

class TelegramService {
  final HttpClient _httpClient;
  final NASAService _nasaService;
  final kTelegramToken = Env.instance.get('TELEGRAM_API_KEY');
  final kTelegramBaseURL = Env.instance.get('TELEGRAM_BASE_URL');

  int offset = 0;

  TelegramService(
      {required NASAService nasaService, required HttpClient httpClient})
      : _httpClient = httpClient,
        _nasaService = nasaService;

  init() async {
    listenToUpdates();
  }

  Future<void> listenToUpdates() async {
    Timer.periodic(
      Duration(milliseconds: 500),
      (timer) {
        try {
          checkUpdates();
        } catch (e) {
          print(e);
        }
      },
    );
  }

  checkUpdates() async {
    var response = await _httpClient.get(
      '$kTelegramBaseURL/bot$kTelegramToken/getUpdates?offset=$offset&timeout=60',
    );

    if (response.statusCode != 200) {
      print('Error: ${response.statusCode}');
      return;
    }

    final messages = response.body['result'] as List;

    if (messages.isEmpty) {
      return;
    }

    print('received ${messages.length} updates - ${DateTime.now()}');

    for (Map update in messages) {
      final currentOffset = update['update_id'];
      if (currentOffset > offset) {
        offset = currentOffset;
      } else {
        continue;
      }

      if (!update.containsKey('message')) {
        continue;
      }

      final command = update['message']?['text'] as String;
      final chatId = update['message']['chat']['id'];
      print(
        'Sending APOD on chat id $chatId for message $offset id and command $command',
      );

      if (command.contains('/getapodwithespecificdate')) {
        try {
          final splitCommand = command.split(' ');
          final dateParts = splitCommand[1].split('/');
          final date = DateTime(
            int.parse(dateParts[2]),
            int.parse(dateParts[1]),
            int.parse(dateParts[0]),
          );
          sendMessage(chatId.toString(), date: date);
        } catch (e) {
          print(e);
          sendErrorMessage(
            chatId.toString(),
            'Data inválida. Tente novamente. \nFormato aceito: dd/mm/yyyy',
          );
        }
      } else if (command.contains('/getapod')) {
        sendMessage(chatId.toString());
      } else {
        sendErrorMessage(
          chatId.toString(),
          'Comando não reconhecido. Tente novamente.',
        );
      }
    }
  }

  sendMessage(String chatId, {DateTime? date}) async {
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

  sendErrorMessage(String chatId, String errorMessage) async {
    _httpClient.get(
      '$kTelegramBaseURL/bot$kTelegramToken/sendMessage',
      queryParameters: {
        'chat_id': chatId,
        'text': errorMessage,
      },
    );
  }
}
