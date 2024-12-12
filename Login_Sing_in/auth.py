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

    Args:
        username (str): El correo electrónico del usuario que intenta iniciar sesión.
        password (str): La contraseña proporcionada por el usuario.

    Returns:
        dict: Un diccionario con la información del usuario si las credenciales son válidas.
        None: Si las credenciales son incorrectas o hay un error.
    """
    try:
        # Conectar a la base de datos
        connection = connect_to_db()
        if not connection:
            return None

        cursor = connection.cursor(dictionary=True)  # cursor devuelve filas como diccionarios

        # Consulta para verificar las credenciales
        query = """
        SELECT ID, Nombre, Apellidos, DNI_NIF, email
        FROM gestores
        WHERE DNI_NIF = %s AND contraseña = %s
        """

        # Ejecutar la consulta
        cursor.execute(query, (username, password))

        # Obtener el resultado
        user = cursor.fetchone()

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

# NOTA: Para mayor seguridad, las contraseñas deben ser encriptadas.
# En lugar de comparar contraseñas directamente, puedes usar una biblioteca como bcrypt.
# Por ejemplo, almacenarías una contraseña encriptada en la base de datos,
# y luego usarías bcrypt para verificarla así:
#
# import bcrypt
# hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# bcrypt.checkpw(password.encode('utf-8'), hashed_password)
