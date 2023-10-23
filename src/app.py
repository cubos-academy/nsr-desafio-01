from flask import Flask, request
from config import setBotWebhook
from utils import sendMessage, sendPhoto, getApod

app = Flask(__name__)

setBotWebhook()


@app.route("/", methods=["POST"])
def reply():
    message_json = request.get_json()
    message_text = message_json["message"]["text"]
    chat_id = message_json["message"]["from"]["id"]

    # Reply 1:
    if message_text.lower() == "hj":
        apod = getApod()

        sendPhoto(chat_id, apod["url"], f'[EXPLICAÇÃO]: {apod["explanation"]}')
        return "ok."

    # Reply 2:
    if "/" in message_text and message_text != "/start":
        date = message_text
        splittedDate = date.split("/")

        if len(splittedDate) != 3:
            sendMessage(
                chat_id,
                "⚠️ Por favor, insira uma data válida e no formato <strong>DD/MM/AAAA</strong>.",
                "html",
            )
        else:
            formattedDate = f"{splittedDate[2]}-{splittedDate[1]}-{splittedDate[0]}"

            apod = getApod(formattedDate)

            try:
                sendMessage(chat_id, f"<b>Viajando para {date}...</b> 💫", "html")
                sendPhoto(chat_id, apod["url"], f'[EXPLICAÇÃO]: {apod["explanation"]}')
            except:
                sendMessage(
                    chat_id,
                    f"Lamento 😢, mas não conseguimos encontrar nos arquivos da NASA a foto do dia {date}.",
                )
                return "ok."
        return "ok."

    # Default reply:
    else:
        sendMessage(
            chat_id,
            "👋 Olá, eu sou o <b>APOD Bot 🌌</b> e eu consigo te mostrar a <b>Foto Astronomica do Dia</b> disponibilizada pela <b>NASA</b>!",
            "html",
        )
        sendMessage(
            chat_id,
            'Você pode ver a de hoje digitando "<b>hj</b>" (sem aspas) ou a de qualquer dia digitando a data no seguinte formato: "<b>DD/MM/AAAA</b>" (sem aspas, exemplo: 12/10/2023).',
            "html",
        )
        return "ok."

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
