import requests
import schedule
import time
import telebot

apod_api = "https://api.nasa.gov/planetary/apod?api_key=g1cm9abo4Gbl1grvYR4HPgZTjStl8KGEMmyvEKiW"
token_api = "6783707477:AAGuQnt4nF6hLVeuhbuasuZsTrQVnQ0_eZs"

bot = telebot.TeleBot(token_api)
request = requests.get(apod_api)

url_api = apod_api
response = requests.get(url_api)
if response.status_code == 200:
    dados = response.json()

    imagem = dados['hdurl']
    titulo = dados['title']
    data = dados['date']
    cr = dados['copyright']
    explicacao = dados['explanation']

# -----------------------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=["Yes"])
def Yes(mensagem):
    texto = """
Certo, de qual data você gostaria? 📅
(digite os parâmetros nesse formato YYYY-MM-DD - Ex: 2021-11-01)    
"""
    bot.reply_to(mensagem, texto)


# caso a resposta seja negativa após o horário selecionado
@bot.message_handler(commands=["No"])
def No(mensagem):
    texto = "Ok, aguarde meu contato amanhã ☀️"
    bot.reply_to(mensagem, texto)

# -----------------------------------------------------------------------------------------------------------------------

# Função para enviar a mensagem

@bot.message_handler(commands=["Claro"])
def Claro(mensagem):
    # Mensagem diária com a APOD.

    texto = f"""
Link da imagem:       
{imagem}

⭐ Olá tripulante! ⭐

Logo abaixo está mais uma fotografia tirada pelo nosso estimado fotógrafo para nossa coleção codinome APOD. 
📸

Então, preparado para mais uma aventura de conhecimento e informação sobre o universo? Espero que sim! 
🌌

🌎 Dados sobre essa foto incrível:

Título: {titulo}

Data: {data}

Copyright: {cr}

Explicação: {explicacao}

Wowww, incrível né? 🤩
Bom, espero que tenha gostado da viagem. 🚀

Te espero amanhã para mais... 👽
Dúvidas ou sugestões? Fale conosco através do e-mail: apodtestedeemail@hotmail.com

Deseja consultar alguma imagem de outra data em específico?

/Yes (mais conhecido como sim)
/No (também conhecido como não)

(logo abaixo está a imagem e acima está a descrição)
"""
    bot.send_message(mensagem.chat.id, texto)

# agendamento às 08:00 horas
schedule.every().day.at("08:00").do(Claro)

while True:
    schedule.run_pending()
    time.sleep(1)

# -----------------------------------------------------------------------------------------------------------------------

# caso a resposta seja negativa
@bot.message_handler(commands=["Negativo"])
def Negativo(mensagem):
    texto = "😔 Ah que pena, mas estou disponível caso queira me contatar novamente para começar sua nova aventura! 😄"

    bot.reply_to(mensagem, texto)

# -----------------------------------------------------------------------------------------------------------------------

# função padrão da mensagem inicial
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def answer(mensagem):
    texto = """
⭐ Olá possível futuro tripulante, espero que esteja bem! ⭐  

Deseja embarcar conosco em uma jornada diária de conhecimento e informação sobre esse vasto universo em que habitamos?
🚀

/Claro 
(iremos te retornar nossa mensagem do dia e você estará agendado para receber as 08:00 horas!)

/Negativo
(Quem perde é você...)
"""
    bot.send_message(mensagem.chat.id, texto)

bot.polling()