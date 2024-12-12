import mysql.connector
from mysql.connector import Error

def connect_to_db():
    """
    Establece una conexión con la base de datos y la devuelve.
    """
    try:
        connection = mysql.connector.connect(
            user='root',  # Usuario de la base de datos
            password='1234',  # Contraseña del usuario
            host='localhost',  # Dirección del servidor
            database='prototipos',  # Nombre de la base de datos
            port='3307'  # Puerto del servidor
        )
        return connection
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def login(username, password):
    """
    Verifica las credenciales del usuario contra la base de datos.
    """
    try:
        # Conectar a la base de datos
        connection = connect_to_db()
        if not connection:
            print("No se pudo conectar a la base de datos.")
            return None

        cursor = connection.cursor(dictionary=True)  # cursor devuelve filas como diccionarios

        # Consulta para verificar las credenciales
        query = """ SELECT DNI_NIF, contraseña FROM gestores WHERE DNI_NIF = %s AND contraseña = %s"""

        # Ejecutar la consulta
        cursor.execute(query, (username, password))

        # Obtener el resultado
        user = cursor.fetchone()
        print(f"Resultado de la consulta: {user}")

        # Cerrar recursos
        cursor.close()
        connection.close()

        if user:
            return user  # Retorna el diccionario con la información del usuario
        else:
            print("Credenciales incorrectas.")
            return None

    except Error as e:
        print(f"Error durante el proceso de login: {e}")
        return None
