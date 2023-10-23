import time
from functions import createTeleBot, imageSender, dateConverter, getDailyImageFromAPOD, getSpecificImageByDate, calcular_tempo_restante, dateValidation, getRandomImage

bot = createTeleBot()

@bot.message_handler(commands=['start', 'olá'])
def send_welcome(message):
  user = message.chat.first_name
  bot.send_message(message.chat.id, "Opa, e aí "+user+", tudo certo? O que posso fazer por você? \n/Foto_Diaria - Enviar imagem da NASA diariamente às 10:00 horas \nEscolher Data - Basta enviar a data desejada \n/Foto_Aleatoria - Receber uma foto Astronomica Aleatória ")

@bot.message_handler(commands=['Foto_Diaria'])
def dailyImageBot(message):
  dailyImage = getDailyImageFromAPOD()
  bot.send_message(message.chat.id, "Certo, a imagem é enviada todos os dias às 07:00 horas (Horário de Brasília)!")

  while True:
    remainingSeconds = calcular_tempo_restante()
    time.sleep(remainingSeconds)
    bot.send_message(message.chat.id, "Aqui está a foto do dia de hoje: ", dailyImage['title'])
    imageSender(bot, message, dailyImage['url'])

@bot.message_handler(commands=['Foto_Aleatoria'])
def randomImageBot(message):
  randomImage = getRandomImage()
  bot.send_message(message.chat.id, randomImage['title'])
  imageSender(bot, message, randomImage['url'])

@bot.message_handler(func=lambda msg: True)
def receiveMessage(message):
  isValid = dateValidation(message.text)
  if isValid == True:
    converttedDate = dateConverter(message.text)
    specificDate = getSpecificImageByDate(converttedDate)
    print("Specific Date: ",specificDate)
    bot.send_message(message.chat.id, specificDate['title'])
    imageSender(bot, message, specificDate['url'])
  else:
    bot.send_message(message.chat.id, isValid)

bot.infinity_polling()