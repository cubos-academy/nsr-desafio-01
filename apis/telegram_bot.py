import os
import threading

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, CallbackQueryHandler
from utils.db_queue import add_chat_id, get_chat_id

from utils.useDB import Sqlite
from .nasa import get_photo_date, get_photo_last5days, get_photo_today


db = Sqlite()

TOKEN = os.getenv('TOKEN_TELEGRAM')
DATE = 0
CHOOSING, FOTO_HOJE, FOTO_DATA, ULTIMOS_5_DIAS = range(4)


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    
    update.message.reply_text(
        f"Olá, {user.full_name}\n\n"
        "*Sou o seu bot inteligente da NASA* 😎\n\n",
        parse_mode='MarkdownV2',
    )
    
    update.message.reply_text(
        "Escolha uma opção abaixo e curta as fotos \nmais incriveis do universo! 🚀🌠",
        reply_markup=main_menu()
    )
    return CHOOSING


def main_menu():
    keyboard = [
        [InlineKeyboardButton("Foto de hoje", callback_data='fotoHoje')],
        [InlineKeyboardButton("Foto de uma data", callback_data='fotoData')],
        [InlineKeyboardButton("Fotos últimos 5 dias", callback_data='ultimos5dias')],
        [InlineKeyboardButton("Habilitar envio automatico", callback_data='envioAutomatico')],
    ]
    return InlineKeyboardMarkup(keyboard)


def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'fotoHoje':
        query.edit_message_text(text="Enviando a foto de hoje...")
        send_foto_hoje(query.message.chat_id, context)

    elif query.data == 'fotoData':
        query.message.reply_text("Por favor, informe a data no formato YYYY-MM-DD.")
        return FOTO_DATA

    elif query.data == 'ultimos5dias':
        query.edit_message_text(text="Buscando as fotos dos últimos 5 dias...")
        send_ultimos_5_dias(query.message.chat_id, context)
        
    elif query.data == 'envioAutomatico':
        query.edit_message_text(text="Cadastrando no envio automatico...")
        
        register_automatic_send(query.message.chat_id, context)

    return CHOOSING


def send_foto_hoje(chat_id, context):
    
    foto_url = get_photo_today()
    context.bot.send_photo(chat_id=chat_id, photo=foto_url)
    return ConversationHandler.END
    

def send_ultimos_5_dias(chat_id, context):
    
    api_urls = get_photo_last5days()
    print(api_urls)
    
    for url in api_urls:
        context.bot.send_photo(chat_id=chat_id, photo=url)
    


def send_photo_date(update, context):
    date_text = update.message.text
    update.message.reply_text(f"Buscando a foto da data {date_text}...")
    
    api_url = get_photo_date(str(date_text))
    
    update.message.reply_photo(photo=api_url)
    

def register_automatic_send(chat_id, context):
    add_chat_id(chat_id)
    
    context.bot.send_message(
        chat_id=chat_id,
        text=f"Você foi cadastrado no envio automatico e receberá a foto do dia, diariamente às 08:00 horas da manhã",
    )
    
    
    
def run_bot():
    
    def saveDB_from_queue():
        
        db = Sqlite()
    
        while True:
            chat_id = get_chat_id()
            
            if chat_id is not None:
                db.insert_sub(chat_id)
        
    
    db_thread = threading.Thread(target=saveDB_from_queue)
    db_thread.daemon = True
    db_thread.start()
    
    
    
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [CallbackQueryHandler(button)],
            FOTO_DATA: [MessageHandler(Filters.text & ~Filters.command, send_photo_date)],
        },
        fallbacks=[]
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


def send_daily_photo(chat_id: str):
    bot = telegram.Bot(token=TOKEN)

    message = "Bom dia! \nComece bem o seu dia, admirando o unviverso!"
    url = get_photo_date()

    bot.send_message(chat_id=chat_id, text=message)
    bot.send_photo(chat_id=chat_id, photo=url)