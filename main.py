import telebot
import requests
from datetime import datetime

KEY_BOT = "6734944049:AAFnUpHfYWUSEjBeD0CJASHxlyX8Slt4o-M"
bot = telebot.TeleBot(KEY_BOT)

KEY_NASA = "vpeLfEp1xeFNAyJf2fHfQ4eIaG0n5cYWfURGw7Ip"
url = "https://api.nasa.gov/planetary/apod?api_key=" + KEY_NASA

user_data = {}

@bot.message_handler(commands=["specificImage"])
def sendImageWithDate(message):
    bot.send_message(message.chat.id, "Por favor, digite a data no formato 'DD/MM/AAAA'")
    user_data[message.chat.id] = "aguardando_data"

@bot.message_handler(func=lambda message: user_data.get(message.chat.id) == "aguardando_data")
def processar_data(message):
    formatedDate = datetime.strptime(message.text, "%d/%m/%Y").strftime("%Y-%m-%d")
    chat_id = message.chat.id

    response = requests.get(url + "&date=" + formatedDate)

    if response.status_code == 200:
        jsonData = response.json()
        imageURL = jsonData["url"]
        bot.send_photo(chat_id, imageURL)
    else:
        print(f"A requisição falhou com o código de status {response.status_code}")

    defaultMessage(message)

def toCheck(message):
    return True

@bot.message_handler(commands=["todayImage"])
def sendImageToday(message):
    response = requests.get(url)
    chat_id = message.chat.id

    if response.status_code == 200:
        jsonData = response.json()
        imageURL = jsonData["url"]
        bot.send_photo(chat_id, imageURL)
    else:
        print(f"A requisição falhou com o código de status {response.status_code}")

    defaultMessage(message)

@bot.message_handler(func=toCheck)
def defaultMessage(message):
    text = """
    Escolha uma opção para continuar (Clique no item):
        /specificImage
        /todayImage
Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(message, text)

bot.polling()
