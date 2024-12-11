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


def insert_data(table, columns, values):
    conn = get_database_connection()
    cursor = conn.cursor()

    cols = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(values))
    query = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"

    cursor.execute(query, values)
    conn.commit()
    conn.close()

