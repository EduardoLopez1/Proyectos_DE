# scripts/run.py

from api_script.api_requests import fetch_data
from database_script.db_model import create_database_table
from database_script.load_data import insert_data
from database_script.db_querys import export_to_csv
from app import app
#from src.database_operations import insert_data
#from src.data_to_csv import export_to_csv


def main():
    
    URL_API = 'https://sistemas.forus.cl/forus/challenge/dummy-api'
    table_name = 'producto'
    
    data = fetch_data(URL_API)
    create_database_table()
    print(data)
    insert_data(data, table_name)
    #export_to_csv('productos.csv')

if __name__ == "__main__":
    main()
    app.run(debug=True)
