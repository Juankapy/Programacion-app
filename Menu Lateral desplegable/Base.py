import mysql.connector

config = {
    'user': 'root',
    'password': '1234 ',
    'host': 'localhost',
    'database': 'prototipos',
    'port': '3307',
    'collation': 'utf8mb4_general_ci',
}


def fetch_all_data(query):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]  # Obtén nombres de las columnas
    conn.close()
    return columns, data

# Conectar a la base de datos

