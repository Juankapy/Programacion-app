import mysql.connector
config = {
'user': 'root',
'password': '1234 ',
'host': 'localhost', # Puede ser 'localhost' si la base de datos está en tu máquina
'database': 'prototipos',
'port': '3307',
'collation': 'utf8mb4_general_ci',
}

# Conectar a la base de datos
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

