import time
from functions import createTeleBot, imageSender, dateConverter, getDailyImageFromAPOD, getSpecificImageByDate, calcular_tempo_restante, dateValidation, getRandomImage

bot = createTeleBot()

@bot.message_handler(commands=['start', 'olá'])
def send_welcome(message):
  user = message.chat.first_name
  bot.send_message(message.chat.id, "Opa, e aí "+user+", tudo certo? \n\nUma imagem Astronômica será enviada todos os dias às 07:00 horas (Horário de Brasília).\n\nO que posso fazer por você agora? \n\n-Escolher Data - Basta enviar a data desejada \n-/Foto_Aleatoria - Receber uma foto Astronomica Aleatória \n-/Ajuda")

  dailyImage = getDailyImageFromAPOD()
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

@bot.message_handler(commands=['Ajuda'])
def randomImageBot(message):
  mensagem = "Ajuda no APOD Bot \n\nOlá "+ message.chat.first_name +", o APOD Telegram Bot é um chatbot criado para enviar uma Foto Astronômica Diária. Ao interagir com o botão Start no início do chat ativou o envio diário. \n\nO envio diário destas fotos ocorre todos os dias às 07:00 no horário de Brasília. \n\nAlém da função de foto diária, você também pode escolher uma data específica para receber a foto. Para isso, basta enviar uma data escrita no formato dd/mm/aaaa. Por exemplo: 20/10/2023. \n\nA data deve estar no intervalo de 16/06/1995 e a data atual. \n\nE por fim, você também pode solicitar uma Foto Astronômica aleatória, com o código /Foto_Aleatoria."
  bot.send_message(message.chat.id, mensagem)

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