import requests
from dotenv import dotenv_values

env_vars = dotenv_values('.env')
telegramApiUrl = f'https://api.telegram.org/bot{env_vars['TELEGRAM_API_KEY']}/'

# Bot actions:
def sendMessage(chat_id: str, message: str, parse_mode: str=None):
    requestParams = {
        "chat_id": chat_id,
        "text": message,
    }
    if parse_mode:
        requestParams["parse_mode"] = parse_mode

    requests.post(telegramApiUrl + "sendMessage", params=requestParams)

def sendPhoto(chat_id: str, photo: str, caption: str=None):
    requestParams = {
        "chat_id": chat_id,
        "photo": photo,
    }
    if caption:
        requestParams["caption"] = caption

    requests.post(telegramApiUrl + "sendPhoto", params=requestParams)
# ------------- #

def getApod(date: str=None):
    requestParams = {"api_key": env_vars["NASA_API_KEY"]}
    if date:
        requestParams["date"] = date

    return requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=requestParams,
    ).json()
