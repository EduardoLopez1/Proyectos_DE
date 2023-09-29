# Funciones
import json
from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_WAPI

# Funciones propias
import utils as ar

# EXTRAER DATOS
# Se obtiene valor de divisa
data_euro = ar.obtener_divisa("euro")
data_usd = ar.obtener_divisa("dolar") # A modo de ejemplo, que se pueden agregar más en el tiempo
print(data_usd, type(data_usd))

# Analizar el JSON en un diccionario de Python

# Acceder a los valores "Valor" y "Fecha"
dolares = data_usd['Dolares'][0]  # Acceder al primer elemento de la lista bajo 'Dolares'

valor = dolares['Valor']
fecha = dolares['Fecha']

# UN POCO DE TRANSFORMACION
# Eliminar la coma decimal
valor = valor.replace(',', '.')

# Imprimir los valores a insertar
print("Valor:", valor)
print("Fecha:", fecha)

# SMS
# Enviar valor del dólar a nuestro celular
message_id = ar.send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,fecha,valor)
