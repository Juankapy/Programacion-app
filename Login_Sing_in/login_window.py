from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from auth import login  # Importar la función de login desde auth.py
from menu import MenuWindow  # Importar la ventana del menú principal


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login_window.ui", self)  # Cargar el diseño desde el archivo .ui generado por QtDesigner

        self.btnLogin.clicked.connect(self.handle_login)  # Conectar el botón de login a la función handle_login

    def handle_login(self):
        username = self.inputUsername.text()  # Obtener el nombre de usuario del campo de texto
        password = self.inputPassword.text()  # Obtener la contraseña del campo de texto

        # Verificar si los campos no están vacíos
        if not username or not password:
            self.lblMessage.setText("Por favor, complete todos los campos.")
            return

        # Verificar las credenciales usando la función login del archivo auth.py
        user = login(username, password)

        if user:
            self.lblMessage.setStyleSheet("color: green;")
            self.lblMessage.setText("¡Bienvenido!")
            self.open_menu_window()  # Si el login es exitoso, abrir la ventana del menú
        else:
            self.lblMessage.setStyleSheet("color: red;")
            self.lblMessage.setText("Usuario o contraseña incorrectos.")

    def open_menu_window(self):
        self.menu_window = MenuWindow()  # Crear una instancia de la ventana del menú
        self.menu_window.show()  # Mostrar la ventana del menú
        self.close()  # Cerrar la ventana de login
