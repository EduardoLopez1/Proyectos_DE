import requests
import sqlite3
import pandas as pd


def fetch_data(url_api):
# Realiza una solicitud a una API
    response = requests.get(f"{url_api}/producto/", verify = False) # DESPUES QUITAR EL VERIFY

    if response.status_code == 200:
        data = response.json()
        
        return data
    
    else:
        print('Error al obtener datos de la API')
