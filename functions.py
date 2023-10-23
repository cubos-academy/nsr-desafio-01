import requests
import os
import telebot
import random
from datetime import datetime, timedelta

APOD_KEY = os.environ.get('APOD_KEY')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
URL_APOD = "https://api.nasa.gov/planetary/apod"
imageUrl = 'none'

def fetchAPOD(date=''):
  params = {
    'api_key': APOD_KEY,
    'date': date,
    'hd': 'True'
  }
  response = requests.get(URL_APOD, params).json()
  print("New Fecth")
  return response

def getSpecificImageByDate(date):
   imageUrl = fetchAPOD(date)
   return imageUrl

def getDailyImageFromAPOD():
  imageUrl = fetchAPOD()
  print("Fetch inicial")
  return imageUrl

def createTeleBot():
  bot = telebot.TeleBot(BOT_TOKEN)
  return bot

def imageSender(bot, message, imageUrl):
  bot.send_photo(message.chat.id, imageUrl)

def calcular_tempo_restante():
  now = datetime.now()
  sentTime = now.replace(hour=7, minute=0, second=0, microsecond=0)
  if now > sentTime:
      sentTime += timedelta(days=1)
  remainingTime = sentTime - now
  return remainingTime.total_seconds()

def dateConverter(date_str):
  parsedDate = datetime.strptime(date_str, '%d/%m/%Y')
  formattedDate = parsedDate.strftime('%Y-%m-%d')
  return formattedDate

def dateValidation(date_str):
    today = datetime.today()
    parsedToday = datetime.strftime(today, "%d/%m/%Y")
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y")
        year = int(date.strftime('%Y'))
        if year >= 1995 and date_str < parsedToday:
          return True  
        else:
           error = "Data Inválida. A data deve ser a partir de 16/06/1995 até " + str(parsedToday) + "."
           return error
    except ValueError:
        error = "Formato da Data Inválida. Escreva uma data no formato dd/mm/aaaa."
        return error
    
def getRandomImage():
  date = randomDateGenerator()
  imageUrl = fetchAPOD(date)
  print(imageUrl)
  return imageUrl

def randomDateGenerator():
    year = random.randint(1996, 2023)  
    month = random.randint(1, 12)       
    day = random.randint(1, 28)
  
    randomDate = datetime(year, month, day)    
    randomDateFormatted = randomDate.strftime('%Y-%m-%d')

    
    return randomDateFormatted