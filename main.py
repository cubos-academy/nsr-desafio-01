from telebot import TeleBot
import nasa
from datetime import date, timedelta
import config

CHAVE_API = config.TELEGRAM_BOT_API_KEY
bot = TeleBot(CHAVE_API)


def enviar_mensagem(chat_id, mensagem):
    bot.send_message(chat_id, mensagem)


def formatar_data(data_usuario):
    try:
        dia, mes, ano = map(int, data_usuario.split('/'))
        data_formatada = date(ano, mes, dia).strftime("%Y-%m-%d")
        return data_formatada
    except ValueError:
        return None


@bot.message_handler(commands=['start'])
def send_welcome(mensagem):
    texto = (f'Olá {mensagem.from_user.first_name}, seja bem vindo!\n'
             'Eu sou o bot da Nasa e estou aqui para te ajudar!\n'
             'Digite /hoje para receber a foto do dia!\n'
             'Digite /ontem para receber a foto de ontem!\n'
             'Digite /dia para receber a foto de uma data específica!\n'
             'Digite /aleatorio para receber uma foto aleatória!\n'
             'Digite /ajuda para saber mais sobre mim!')
    enviar_mensagem(mensagem.chat.id, texto)


@bot.message_handler(commands=['ajuda, help'])
def ajuda(mensagem):
    text = ('Digite /hoje para receber a foto do dia!\n'
            'Digite /ontem para receber a foto de ontem!\n'
            'Digite /dia para receber a foto de uma data específica!\n'
            'Digite /aleatorio para receber uma foto aleatória!')
    enviar_mensagem(mensagem.chat.id, text)


@bot.message_handler(commands=['hoje'])
def hoje(mensagem):
    try:
        url, titulo, explicacao = nasa.get_apod(date.today())
        bot.send_photo(mensagem.chat.id, photo=url)
        enviar_mensagem(mensagem.chat.id, titulo)
        enviar_mensagem(mensagem.chat.id, explicacao)
    except Exception as e:
        enviar_mensagem(mensagem.chat.id, f'Erro: {str(e)}')


@bot.message_handler(commands=['ontem'])
def ontem(mensagem):
    ontem = date.today() - timedelta(1)

    try:
        url, titulo, explicacao = nasa.get_apod(ontem)
        bot.send_photo(mensagem.chat.id, photo=url)
        enviar_mensagem(mensagem.chat.id, titulo)
        enviar_mensagem(mensagem.chat.id, explicacao)
    except Exception as e:
        enviar_mensagem(mensagem.chat.id, f'Erro: {str(e)}')


@bot.message_handler(commands=['dia'])
def dia_especifico(mensagem):
    enviar_mensagem(mensagem.chat.id, 'Digite a data no formato DD/MM/AAAA')
    bot.register_next_step_handler(mensagem, processar_data)


def processar_data(mensagem):
    data_usuario = mensagem.text
    data_formatada = formatar_data(data_usuario)
    if data_formatada:
        try:
            url, titulo, explicacao = nasa.get_apod(data_formatada)
            bot.send_photo(mensagem.chat.id, photo=url)
            enviar_mensagem(mensagem.chat.id, titulo)
            enviar_mensagem(mensagem.chat.id, explicacao)
        except Exception as e:
            enviar_mensagem(mensagem.chat.id, f'Erro: {str(e)}')
    else:
        enviar_mensagem(mensagem.chat.id, 'Data inválida! Use o formato DD/MM/AAAA.')


@bot.message_handler(commands=['aleatorio'])
def aleatorio(mensagem):
    try:
        url, titulo, explicacao, data = nasa.get_apod_aleatorio()
        bot.send_photo(mensagem.chat.id, photo=url)
        enviar_mensagem(mensagem.chat.id, titulo)
        enviar_mensagem(mensagem.chat.id, data)
        enviar_mensagem(mensagem.chat.id, explicacao)
    except Exception as e:
        enviar_mensagem(mensagem.chat.id, f'Erro: {str(e)}')

@bot.message_handler(func=lambda mensagem: True)
def outras_mensagens(mensagem):
    text = ('Digite /hoje para receber a foto do dia!\n'
            'Digite /ontem para receber a foto de ontem!\n'
            'Digite /dia para receber a foto de uma data específica!\n'
            'Digite /aleatorio para receber uma foto aleatória!')
    enviar_mensagem(mensagem.chat.id, text)


bot.polling()
