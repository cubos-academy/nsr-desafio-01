import telebot
import requests

import os
from dotenv import load_dotenv

from utils import validateData, formatedData

load_dotenv()

bot = telebot.TeleBot(os.getenv("KEY_BOT"))

url = "https://api.nasa.gov/planetary/apod?api_key=" + os.getenv("KEY_NASA")

user_data = {}

@bot.message_handler(commands=["commands"])
def listCommands(message):
    text = """
✨ Recursos do Bot:
    
    /apod - Receba a imagem mais recente do APOD da NASA.
    /data - Escolha uma data específica para ver a imagem do APOD.
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["data"])
def sendImageWithDate(message):
    bot.send_message(message.chat.id, "Por favor, digite a data no formato 'DD/MM/AAAA'")
    user_data[message.chat.id] = "date_loading"

@bot.message_handler(func=lambda message: user_data.get(message.chat.id) == "date_loading")
def processar_data(message):
    del user_data[message.chat.id]
    if not validateData(message.text):
        sendImageWithDate(message)
        return

    response = requests.get(url + "&date=" + formatedData(message.text))
    reqImage(message, response)

@bot.message_handler(commands=["apod"])
def sendImageToday(message):
    response = requests.get(url)
    reqImage(message, response)

def reqImage(message, response):
    chat_id = message.chat.id
    jsonData = response.json()

    if response.status_code == 200:
        imageURL = jsonData["url"]
        imageTitle = jsonData["title"]
        imageDescription = jsonData["explanation"]
        bot.send_photo(chat_id, imageURL)

        text = f"""
               🌌 {imageTitle} 🌌

                {imageDescription}
            """
        bot.send_message(message.chat.id, text)
    else:
        print(f"A requisição falhou com o código de status {response.status_code}")
        bot.send_message(message.chat.id, jsonData["msg"])

    listCommands(message)

def toCheck(message):
    return True

@bot.message_handler(func=toCheck)
def defaultMessage(message):
    text = """
    🚀 Bem-vindo ao nosso Bot do APOD! 🌌

    Este bot é o seu portal para explorar as maravilhas do cosmos todos os dias. Com o Astronomy Picture of the Day (APOD), você receberá diariamente uma imagem espetacular do espaço, juntamente com uma descrição fascinante.
    
✨ Recursos do Bot:
    
    /apod - Receba a imagem mais recente do APOD da NASA.
    /data - Escolha uma data específica para ver a imagem do APOD.
    /commands - Lista todos os camanhos do bot.
    
🌟 Como usar o Bot:
    
    Basta digitar um dos comandos acima no chat, e o nosso bot irá responder prontamente com a imagem ou informações que você deseja. Explore o universo, aprenda mais sobre o espaço e compartilhe essas descobertas com seus amigos!
    """
    bot.reply_to(message, text)

bot.polling()
