import 'package:intl/intl.dart';

class NASAApodModel {
  final String? date;
  final String? explanation;
  final String? title;
  final String? url;

  NASAApodModel({
    required this.date,
    required this.explanation,
    required this.title,
    required this.url,
  });

  @override
  String toString() {
    if (date == null || url == null) {
      return 'Não foi possível obter a imagem do dia.';
    }

    final dateTime = DateTime.parse(date!);

    final formattedDate = DateFormat(
      "dd 'de' MMMM 'de' yyyy",
      'pt_BR',
    ).format(dateTime);

    return 'A imagem do dia $formattedDate é: \n$url';
  }

  static NASAApodModel fromJson(body) {
    return NASAApodModel(
      date: body['date'],
      explanation: body['explanation'],
      title: body['title'],
      url: body['url'],
    );
  }
}
