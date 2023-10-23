import random
import requests
from datetime import date, datetime

import config

URL_APOD = "https://api.nasa.gov/planetary/apod"
API_KEY = config.NASA_API_KEY


class NASADataException(Exception):
    pass


class DataForaDoIntervalo(NASADataException):
    pass


def get_apod(data):
    """
    Retorna os dados da "Foto do Dia" da NASA para uma data específica.

    :param data: A data no formato 'YYYY-MM-DD'.
    :return: Uma tupla contendo a URL da imagem, o título, a explicação e a data.
    """
    if isinstance(data, str):
        data_atual = date.today()
        data_minima = date(1995, 6, 16)

        try:
            data_formatada = datetime.strptime(data, '%Y-%m-%d').date()
        except ValueError:
            raise DataForaDoIntervalo('A data deve estar no formato YYYY-MM-DD.')

        if data_formatada < data_minima or data_formatada > data_atual:
            data_minima_formatada = data_minima.strftime("%d/%m/%Y")
            data_atual_formatada = data_atual.strftime("%d/%m/%Y")
            raise DataForaDoIntervalo(f'A data deve estar entre {data_minima_formatada} e {data_atual_formatada}.')

    params = {
        'api_key': API_KEY,
        'date': data,
        'hd': 'True'
    }
    try:
        response = requests.get(URL_APOD, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise NASADataException(f'Erro ao fazer requisição: {str(e)}')

    if response.status_code != 200:
        raise NASADataException(f'Erro ao fazer requisição: {response.status_code}')

    dados = response.json()
    explicacao = dados['explanation']
    url = dados['url']
    titulo = dados['title']
    return url, titulo, explicacao


def get_apod_aleatorio():
    params = {
        'api_key': API_KEY,
        'count': str(random.randint(1, 100))
    }
    try:
        response = requests.get(URL_APOD, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise NASADataException(f'Erro ao fazer requisição: {str(e)}')

    if response.status_code != 200:
        raise NASADataException(f'Erro ao fazer requisição: {response.status_code}')

    dados = response.json()[0]
    explicacao = dados['explanation']
    url = dados['url']
    titulo = dados['title']
    data = dados['date']
    data_formatada = datetime.strptime(data, '%Y-%m-%d').date().strftime("%d/%m/%Y")
    return url, titulo, explicacao, data_formatada
