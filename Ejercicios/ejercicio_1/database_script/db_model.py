import sqlite3

# Nombre del la base de datos
database_file = 'productos.db'

def create_database_table():
    """Crea una tabla de productos en la base de datos."""
    try:
        # Conectar a la base de datos SQLite (o crearla si no existe)
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        # Definir el esquema de la tabla
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS producto (
                productoId INTEGER PRIMARY KEY,
                productoNombre TEXT,
                productoDescripcion TEXT,
                productoCantidad INTEGER,
                productoUbicacion INTEGER
            )
        '''

        # Crear la tabla
        cursor.execute(create_table_query)

        # Guardar los cambios en la base de datos
        conn.commit()

        print("Tabla 'productos' creada con éxito.")

    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {str(e)}")

    finally:
        # Cerrar la conexión a la base de datos
        if conn:
            conn.close()

