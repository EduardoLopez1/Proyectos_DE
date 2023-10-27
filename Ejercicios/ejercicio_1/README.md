# Ejercicio 1

Este proyecto contiene una app diseñada utilizando Flask, una base de datos sqlite y manejo de archivos mediante pandas. La que tiene como finalidad la inserción de datos mediante extracción de una API a una base de datos para luego obtener estos mismos en un archivo .csv.

## Estructura del proyecto

ejercicio_1/
- api_script/ # Carpeta que contiene todo lo relacionado a la API forus
    - api_requests.py # Función que obtiene los datos de la API
- app/ # Carpeta que contiene la app
    - exported_files/ # Aquí se guarda el archivo generado por la app
        - productos.csv 
    - __init__.py # Se levanta la app
    - app.py # Archivo que crea la app
    - routes.py # Se definen los parametros de la app, incluyendo exportación del archivo csv
- database_script/ # Todo lo relacionado a la base de datos
    - db_export_files/ # Carpeta en caso de requerir extraer datos directamente a la bd
        - productos.csv
    - db_model.py # Creación de la base de datos
    - db_querys.py # Script que permite exportar datos y posibles otras operaciones 
    - load_data.py # Script que inserta datos a la base de datos
- productos.db # base de datos
- requirements.txt 
- run.py # main del proyecto

## Descarga e Instalación

### Descargar el Proyecto

1. Clona el repositorio desde GitLab:

   ```bash
   git clone URL_DEL_REPOSITORIO

2. Navega al directorio del proyecto
   ```bash
   cd ejercicio_1

### Configuración del Entorno
#### Con Anaconda

1. Crea un entorno de Anaconda(opcional pero recomendado):
   ```bash
   conda create --name nombre_del_entorno --file requirements.txt
2. Activa el entorno de Anaconda:
   ```bash
   conda activate nombre_del_entorno

#### Sin Anaconda

1. Instala las dependencias con pip:
   ```bash
   pip install -r requirements.txt

### Ejecutar el Proyecto

1. Ejecuta el proyecto
   ```bash
   python run.py

### Requisitos
- Python 3.7 o superior
- Otras dependencias especificadas en `requirements.txt`


