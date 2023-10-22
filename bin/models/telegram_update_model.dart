class TelegramUpdate {
  final int updateId;
  final TelegramMessage message;

  TelegramUpdate(this.updateId, this.message);

  factory TelegramUpdate.fromJson(Map<String, dynamic> json) {
    return TelegramUpdate(
      json['update_id'] as int,
      TelegramMessage.fromJson(json['message'] as Map<String, dynamic>),
    );
  }
}

class TelegramMessage {
  final int messageId;
  final TelegramUser from;
  final TelegramChat chat;
  final int date;
  final String text;
  final List<TelegramMessageEntity> entities;

  TelegramMessage(this.messageId, this.from, this.chat, this.date, this.text,
      this.entities);

  factory TelegramMessage.fromJson(Map<String, dynamic> json) {
    return TelegramMessage(
      json['message_id'] as int,
      TelegramUser.fromJson(json['from'] as Map<String, dynamic>),
      TelegramChat.fromJson(json['chat'] as Map<String, dynamic>),
      json['date'] as int,
      json['text'] as String,
      (json['entities'] as List)
          .map((e) => TelegramMessageEntity.fromJson(e as Map<String, dynamic>))
          .toList(),
    );
  }
}

class TelegramUser {
  final int id;
  final bool isBot;
  final String firstName;
  final String username;
  final String languageCode;

  TelegramUser(
      this.id, this.isBot, this.firstName, this.username, this.languageCode);

  factory TelegramUser.fromJson(Map<String, dynamic> json) {
    return TelegramUser(
      json['id'] as int,
      json['is_bot'] as bool,
      json['first_name'] as String,
      json['username'] as String,
      json['language_code'] as String,
    );
  }
}

class TelegramChat {
  final int id;
  final String firstName;
  final String username;
  final String type;

  TelegramChat(this.id, this.firstName, this.username, this.type);

  factory TelegramChat.fromJson(Map<String, dynamic> json) {
    return TelegramChat(
      json['id'] as int,
      json['first_name'] as String,
      json['username'] as String,
      json['type'] as String,
    );
  }
}

class TelegramMessageEntity {
  final int offset;
  final int length;
  final String type;

  TelegramMessageEntity(this.offset, this.length, this.type);

  factory TelegramMessageEntity.fromJson(Map<String, dynamic> json) {
    return TelegramMessageEntity(
      json['offset'] as int,
      json['length'] as int,
      json['type'] as String,
    );
  }
}
