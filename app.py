import requests

from flask import Flask, request
from config import setBotWebhook, telegramApiUrl, env_vars

app = Flask(__name__)

# Bot configs set
setBotWebhook()
# ------------- #


def getApod(date=None):
    print(date)
    if date:
        return requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={"api_key": env_vars["NASA_API_KEY"], "date": date},
        ).json()
    return requests.get(
        "https://api.nasa.gov/planetary/apod",
        params={"api_key": env_vars["NASA_API_KEY"]},
    ).json()


@app.route("/", methods=["POST"])
def reply():
    message_json = request.get_json()
    message_text = message_json["message"]["text"]
    chat_id = message_json["message"]["from"]["id"]

    if message_text.lower() == "hj":
        apod = getApod()

        requests.post(
            telegramApiUrl + "sendPhoto",
            params={
                "chat_id": chat_id,
                "photo": apod["url"],
                "caption": f'[EXPLICAÇÃO]: {apod["explanation"]}',
            },
        )
        return "ok."

    if "/" in message_text:
        date = message_text.split("/")
        formattedDate = f"{date[2]}-{date[1]}-{date[0]}"

        apod = getApod(formattedDate)

        requests.post(
            telegramApiUrl + "sendPhoto",
            params={
                "chat_id": chat_id,
                "photo": apod["url"],
                "caption": f'[EXPLICAÇÃO]: {apod["explanation"]}',
            },
        )
        return "ok."

    else:
        requests.post(
            telegramApiUrl + "sendMessage",
            params={
                "chat_id": chat_id,
                "text": 'Olá, eu sou o <b>APOD Bot</b> e eu consigo te mostrar a <b>Foto Astronomica do Dia</b> disponibilizada pela <b>NASA</b>! Você pode ver a de hoje digitando "<b>hj</b>" (sem aspas) ou a de qualquer dia digitando a data no seguinte formato: "<b>DD/MM/AAAA</b>" (sem aspas, exemplo: 12/10/2023).',
                "parse_mode": "html",
            },
        )
        return "ok."
