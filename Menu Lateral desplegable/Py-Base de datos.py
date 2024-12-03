import mysql.connector
<<<<<<< Updated upstream

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
=======
# Configuración de la conexión a la base de datos
config = {
'user': 'root',
'password': 'tu_contraseña',
'host': 'tu_host', # Puede ser 'localhost' si la base de datos está en tu máquina
'database': 'tu_base_de_datos',
>>>>>>> Stashed changes
