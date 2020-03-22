# bot.py
import requests  
import os
from flask import Flask, request
import logging,csv


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('Covid19-esp')

def start():
    logger.info('He recibido un comando start')
    #Mando la información referente al comando
    mensaje ="La información que ofrece este bot es la publicada por el Ministerio de Sanidad Español. La información puede encontrarse en la web: covid19.isciii.es .\n"
    mensaje += "*Lista de comandos:*\n"
    mensaje += "/start - Inicia el bot y ofrece información inicial\n"
    mensaje += "/esp - Ofrece los datos generales de todo el estado\n"
    mensaje += "/comunidades - Ofrece los datos por comunidades autónomas\n"
    return mensaje
def esp():
    logger.info('He recibido un comando espania')
    mensaje = ""
    with open('datos/data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mensaje += "*Fecha:* " + row['Fecha'] + "\n"
            mensaje += "*Hora:* " + row['Hora'] + "\n"
            mensaje += "*Casos Totales:* " + row['Casos'] + "\n"
            mensaje += "*Defunciones:* " + row['Defunciones'] + "\n"
            mensaje += "*Recuperados:* " + row['Recuperados'] + "\n"
    return mensaje
    
def comunidades():
    logger.info('He recibido un comando comunidades')
    mensaje = ""
    with open('datos/ccaa.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mensaje += "*"+row["﻿CCAA"]+":* "+row["Nº Casos"] + "\n"
    return mensaje

# Add your telegram token as environment variable
if not 'HEROKU' in os.environ:
    from config.auth import token
    BOT_URL = f'https://api.telegram.org/bot{token}/'
else:
    #Si esta desplegado en Heroku
    BOT_URL = f'https://api.telegram.org/bot{os.environ["TOKEN"]}/'


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():  
    data = request.json

    chat_id = data['message']['chat']['id']


    message = data['message']['text']
    message = message.replace("/", "") 

    if message == "start":
        message = start()
    elif message == "esp":
        message = esp()
    elif message == "comunidades":
        message = comunidades()
    else:
        message = "Comando no soportado"
        
        
    json_data = {
        "chat_id": chat_id,
        "text": message,
        'parse_mode': 'Markdown',
    }

    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=json_data)

    return ''


if __name__ == '__main__':  
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)