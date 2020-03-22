from telegram.ext import Updater
from config.auth import token
from telegram.ext import CommandHandler
import logging,csv
import urllib.request
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('Covid19-esp')

def start(bot, update):
    logger.info('He recibido un comando start. Usuario: '+ str(update.message.chat_id))
    #Mando la información referente al comando
    mensaje ="La información que ofrece este bot es la publicada por el Ministerio de Sanidad Español. La información puede encontrarse en la web: covid19.isciii.es .\n"
    mensaje += "*Lista de comandos:*\n"
    mensaje += "/start - Inicia el bot y ofrece información inicial\n"
    mensaje += "/esp - Ofrece los datos generales de todo el estado\n"
    mensaje += "/comunidades - Ofrece los datos por comunidades autónomas\n"
    #Se envia al chat_id
    #el texto es el mensaje
    #Y como estoy usando markdown indico que lo parse de ese modo
    bot.send_message(
        chat_id=update.message.chat_id,
        text=mensaje,
        parse_mode = "Markdown"
    )
def esp(bot,update):
    logger.info('He recibido un comando espania. Usuario: '+ str(update.message.chat_id))
    mensaje = ""
    with open('datos/data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mensaje += "*Fecha:* " + row['Fecha'] + "\n"
            mensaje += "*Hora:* " + row['Hora'] + "\n"
            mensaje += "*Casos Totales:* " + row['Casos'] + "\n"
            mensaje += "*Defunciones:* " + row['Defunciones'] + "\n"
            mensaje += "*Recuperados:* " + row['Recuperados'] + "\n"

    bot.send_message(
        chat_id=update.message.chat_id,
        text=mensaje,
        parse_mode = "Markdown"
    )

def comunidades(bot,update):
    logger.info('He recibido un comando comunidades. Usuario: '+ str(update.message.chat_id))
    mensaje = ""
    with open('datos/ccaa.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mensaje += "*"+row["﻿CCAA"]+":* "+row["Nº Casos"] + "\n"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=mensaje,
        parse_mode = "Markdown"
    )
if __name__ == '__main__':
    #Si se ejecuta en local
    if not 'HEROKU' in os.environ:
        updater = Updater(token)
    else:
        #Si esta desplegado en Heroku
        updater = Updater(os.environ['TOKEN'])

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    espania_handler = CommandHandler('esp', esp)
    dispatcher.add_handler(espania_handler)

    comunidades_handler = CommandHandler('comunidades', comunidades)
    dispatcher.add_handler(comunidades_handler)

    updater.start_polling()
    updater.idle()

