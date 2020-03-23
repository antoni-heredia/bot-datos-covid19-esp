# bot-datos-covid19-esp
Con este bot quiero ofrecer una forma rápida y sencilla de acceder a los datos proporcionados por el Ministerio de Sanidad Español del estado actual del covid-19 en nuestro país.

## Token
Para hacer funcionar el bot tendras que añadir el token del tuyo. Para ello cambia el nombre del fichero [auth.py.copia](src/config/auth.py.copia) al nombre __auth.py__ y añade tu token.
## Lista de comandos
/start - Inicia el bot y ofrece información inicial
/esp - Ofrece los datos generales de todo el estado
/comunidades - Ofrece los datos por comunidades autónomas

## Despliegue en Heroku
Para Heroku hay que crear una variable TOKEN donde se añadira el token de nuestro bot. Y una variable HEROKU para indicar que esta desplegado ahi. 

## Tutoriales seguidos
Al principio empece usando [este](https://medium.com/@goyoregalado/bots-de-telegram-en-python-134b964fcdf7), muy sencillo pero usaba las colas que proporciona Telegram, cosa que no me servia para desplegarlo en Heroku.

Despues pase a [este](https://planetachatbot.com/telegram-bot-webhook-heroku-fa53c5d72081) que hace uso de los webhook de telegram, hacienndo posible el despliegue en Heroku.

