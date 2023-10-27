import sqlite3

def insert_data(data, table_name):
    # Conectar a la base de datos
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()

    # Obtener las columnas de la tabla
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]

    # Preparar la consulta de inserción con parámetros dinámicos
    insert_query = f"INSERT INTO {table_name} ({', '.join(columns[1:])}) VALUES ({', '.join(['?'] * (len(columns) - 1))})"

    # Iterar a través de los datos y realizar inserciones
    for producto in data:
        cursor.execute(insert_query, tuple(producto.get(column, None) for column in columns[1:]))

    # Hacer commit para guardar los cambios
    conn.commit()

    # Cerrar la conexión
    conn.close()

