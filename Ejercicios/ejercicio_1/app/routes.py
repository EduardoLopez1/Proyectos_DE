import os
import sqlite3
import pandas as pd
from flask import Blueprint, Response

api = Blueprint("api", __name__)

@api.route("/data.csv", methods=["GET"])
def get_data_csv():
    # Conecta a la base de datos SQLite3
    conn = sqlite3.connect("app/../productos.db")

    # Consulta SQL que trae todos los productos para ser guardados en un DataFrame
    query = "SELECT * FROM producto"
    df = pd.read_sql_query(query, conn)

    # Cierra la conexión a la base de datos
    conn.close()

    # Ruta donde se guardará el archivo CSV
    export_path = "app/exported_files/productos.csv"

    # Guardamos el DataFrame en un archivo CSV en la ubicación especificada
    df.to_csv(export_path, index=False)

    # Configuramos los encabezados de respuesta para indicar que es un archivo CSV descargable
    response = Response(open(export_path, "r").read(), content_type='text/csv')
    response.headers["Content-Disposition"] = "attachment; filename=productos.csv"

    return response
