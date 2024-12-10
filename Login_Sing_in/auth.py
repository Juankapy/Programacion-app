from Base import get_connection  # Importar la función de conexión a la base de datos desde Base.py
import bcrypt  # Librería para verificar contraseñas cifradas

def login(username, password):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Buscar al usuario en la base de datos por el nombre de usuario
            query = "SELECT * FROM empleados WHERE nombre = %s"
            cursor.execute(query, (username,))
            user = cursor.fetchone()

            # Si el usuario existe y la contraseña es correcta
            if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                return user  # Retornar los datos del usuario si el login es exitoso
            return None  # Si no se encuentra el usuario o la contraseña es incorrecta, retornar None
    finally:
        connection.close()
