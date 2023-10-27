import sqlite3
import pandas as pd
import os  # Importar la biblioteca os para trabajar con rutas de archivos


def export_to_csv(csv_file):
    # Conectar a la base de datos
    conn = sqlite3.connect('productos.db')

    # Ejecutar una consulta SQL para seleccionar los datos que deseas exportar
    query = "SELECT * FROM producto"

    # Usar pandas para leer los datos desde la base de datos
    df = pd.read_sql_query(query, conn)


    # Ruta completa al archivo CSV
    output_folder = 'C:/Users/elopez/Desktop/YO/FORUS/ejercicio_1/database_script/db_export_files'  # Reemplaza con la ruta de la carpeta deseada
    csv_path = os.path.join(output_folder, csv_file)

    # Guardar los datos en un archivo CSV en la carpeta deseada
    df.to_csv(csv_path, sep = ';', index=False)

    # Cerrar la conexión a la base de datos
    conn.close()

    print(f'Los datos se han exportado a {csv_path}')

