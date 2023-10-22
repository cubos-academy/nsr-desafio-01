import 'dart:io';

class Env {
  static final Env instance = Env._();

  final Map<String, String> _entries = {};

  Env._() {
    _init();
  }

  String get(String key) {
    return instance._entries[key] ?? '';
  }

  _init() {
    final env = Platform.environment;

    for (var element in env.entries) {
      _entries[element.key] = element.value;
    }

    final dotEnvFile = File('.env');

    // Ovewrite env variables if .env file exists
    if (dotEnvFile.existsSync()) {
      final lines = dotEnvFile.readAsLinesSync();

      for (var line in lines) {
        final keyValue = line.split('=');
        _entries[keyValue[0]] = keyValue[1];
      }
    }
  }
}
