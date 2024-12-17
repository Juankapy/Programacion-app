import mysql.connector
def get_database_connection():
    config = {
        'user': 'root',  # Cambia según tu configuración
        'password': '1234',
        'host': 'localhost',
        'database': 'prototipos',
        'port': '3307',
        'collation': 'utf8mb4_general_ci',
    }
    return mysql.connector.connect(**config)

def fetch_all_data(query):
    conn = get_database_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return columns, data
    except mysql.connector.Error as e:
        print(f"Error en la consulta: {e}")
        raise
    finally:
        cursor.close()
        conn.close()


def insert_or_update_data(table, data):
    """
    Inserta o actualiza registros en la base de datos.
    :param table: Nombre de la tabla.
    :param data: Diccionario con las columnas y valores.
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    try:
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        update_clause = ", ".join([f"{key} = VALUES({key})" for key in data.keys()])

        query = f"""
        INSERT INTO {table} ({columns}) 
        VALUES ({placeholders}) 
        ON DUPLICATE KEY UPDATE {update_clause};
        """

        cursor.execute(query, tuple(data.values()))
        conn.commit()
        print("Datos insertados/actualizados correctamente.")
    except mysql.connector.Error as e:
        print(f"Error al insertar/actualizar datos: {e}")
    finally:
        cursor.close()
        conn.close()