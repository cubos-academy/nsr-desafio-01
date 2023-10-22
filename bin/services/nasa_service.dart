import '../helpers/env.dart';
import '../helpers/http_client.dart';
import '../models/nasa_apod_model.dart';

class NASAService {
  final HttpClient _httpClient;

  final kNASABaseURL = Env.instance.get('NASA_BASE_URL');
  final kEndpointAPOD = Env.instance.get('NASA_ENDPOINT_APOD');
  final kNASAAPIKey = Env.instance.get('NASA_API_KEY');

  NASAService({required HttpClient httpClient}) : _httpClient = httpClient;

  Future<NASAApodModel> getCurrentAPOD() async {
    final url = kNASABaseURL + kEndpointAPOD;
    final queryParameters = {
      'api_key': kNASAAPIKey,
    };

    final response =
        await _httpClient.get(url, queryParameters: queryParameters);

    return NASAApodModel.fromJson(response.body);
  }

  Future<NASAApodModel> getAPODByDate(DateTime date) async {
    final url = kNASABaseURL + kEndpointAPOD;
    final queryParameters = {
      'api_key': kNASAAPIKey,
      'date': '${date.year}-${date.month}-${date.day}',
    };

    final response =
        await _httpClient.get(url, queryParameters: queryParameters);

    return NASAApodModel.fromJson(response.body);
  }
}
