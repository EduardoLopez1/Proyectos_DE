import pandas as pd
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_WAPI
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def obtener_divisa(divisa):
    """
    Función que consulta a la API y obtiene el valor de
    la divisa el día de hoy, devuelta en un dataframe.

    Args:
        divisa (string): nombre de la divisa
    """
    api_key = ''
    formato_respuesta = 'json'

    # URL de las APIs
    url_dolar = f"https://api.cmfchile.cl/api-sbifv3/recursos_api/{divisa}?apikey={api_key}&formato={formato_respuesta}"

    payload = {}
    headers = {}

    try:
        response = requests.get(url_dolar, headers = headers, data = payload)

        # Comprobamos que pasan las solicitudes
        if response.status_code == 200:
            data_api = response.json()
        else:
            print("Alguna de las solicitudes a las APIs falló.")
            data_api = None
    except Exception as e:
        print("Se produjo un error al acceder a una o ambas APIs:", str(e))
        data_api = None

    return data_api
        
def send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,valor):

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body='\nHola! \n\n\n El valor del dolar hoy '+ input_date +' es: ' + valor,
                        from_=PHONE_NUMBER,
                        to=''
                    )

    return message.sid

