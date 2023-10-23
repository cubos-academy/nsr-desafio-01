import os, requests, datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY_NASA')
BASE_URL = 'https://api.nasa.gov/planetary/apod'


def get_photo_date(date: str):
    
    QUERY = f'?api_key={API_KEY}&date={date}'
    
    try:
        response = requests.get(f'{BASE_URL}{QUERY}')

        if response.status_code == 200:
            data = response.json()
            
            if 'url' in data:
                image_url = data['url']
                return image_url
            else:
                print("A resposta não contém uma URL de imagem.")
        else:
            print(f"A solicitação GET falhou com o código de status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação GET: {e}")


def get_photo_last5days():
    
    end_date = datetime.date.today().strftime(r"%Y-%m-%d")
    start_date = (datetime.date.today()-datetime.timedelta(days=5)).strftime(r"%Y-%m-%d")
    
    QUERY = f'?api_key={API_KEY}&start_date={start_date}&end_date={end_date}'
    
    try:
        response = requests.get(f'{BASE_URL}{QUERY}')

        if response.status_code == 200:
            datas = response.json()
            
            list = []
            for data in datas:
                if 'url' in data:
                    image_url = data['url']
                    list.append(image_url)
                else:
                    print("A resposta não contém uma URL de imagem.")
            return list
        else:
            print(f"A solicitação GET falhou com o código de status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação GET: {e}")


def get_photo_today():
    
    date = datetime.date.today().strftime(r"%Y-%m-%d")
    
    QUERY = f'?api_key={API_KEY}&date={date}'
    
    try:
        response = requests.get(f'{BASE_URL}{QUERY}')

        if response.status_code == 200:
            data = response.json()
            
            if 'url' in data:
                image_url = data['url']
                return image_url
            else:
                print("A resposta não contém uma URL de imagem.")
        else:
            print(f"A solicitação GET falhou com o código de status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação GET: {e}")

