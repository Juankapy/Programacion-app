from PyQt6 import uic
from PyQt6.QtCore import Qt  # Aquí importamos Qt desde el módulo correcto (QtCore)
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from App_Menu_Base.menu import MenuWindow  # Importamos MenuWindow directamente
from Login_Sing_in.auth import login

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)

        # Conexión de los botones con sus respectivas funciones
        self.IniciarSesion.clicked.connect(self.handle_login)
        self.bt_restaurar.clicked.connect(self.showNormal)
        self.bt_minimizar.clicked.connect(self.showMinimized)
        self.bt_maximizar.clicked.connect(self.showMaximized)
        self.bt_cerrar.clicked.connect(self.close)

        # Configurar ventana sin bordes
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.resize(800, 600)
        self.old_position = None

        # Inicializa el QLabel de mensajes de error como invisible
        self.lb_error.setVisible(False)

    def handle_login(self):
        """
        Maneja el inicio de sesión del usuario al presionar el botón "Login".
        """
        # Entradas del formulario
        username = self.lineEdit1.text().strip()  # Captura del nombre de usuario
        password = self.lineEdit2.text().strip()  # Captura de la contraseña

        # Validación de campos vacíos
        if not username or not password:
            self.show_error_message("Por favor, complete todos los campos.")
            return

        # Verificar credenciales a través de la función de login
        try:
            user = login(username, password)
            if user:
                self.lb_error.setVisible(False)  # Limpiar cualquier mensaje previo si las credenciales son correctas
                self.open_menu_window()  # Abrir ventana de menú principal
            else:
                self.show_error_message("Usuario o contraseña incorrectos.")
        except Exception as e:
            self.show_error_message(f"Error al procesar el inicio de sesión: {str(e)}")

    def show_error_message(self, message):
        """
        Muestra un mensaje de error en el QLabel correspondiente.
        """
        self.lb_error.setText(message)  # Establece el texto del mensaje de error
        self.lb_error.setVisible(True)  # Muestra el QLabel si estaba oculto

    def open_menu_window(self):
        """
        Abre la ventana principal de la aplicación y cierra la ventana de login.
        """
        self.menu_window = MenuWindow()  # Crea una instancia de MenuWindow
        self.menu_window.show()  # Muestra la ventana del menú
        self.close()  # Cierra la ventana de login actual

    def show_message(self, title, message, icon):
        """
        Muestra un cuadro de mensaje con el título, mensaje y tipo de ícono especificados.
        """
        msg_box = QMessageBox(self)  # Crea un cuadro de mensaje
        msg_box.setWindowTitle(title)  # Título del cuadro
        msg_box.setText(message)  # Texto del mensaje
        msg_box.setIcon(icon)  # Ícono correspondiente
        msg_box.exec()  # Ejecuta el cuadro de mensaje


if __name__ == "__main__":
    app = QApplication([])  # Se asegura de que QApplication solo se crea aquí
    window = LoginWindow()
    window.show()
    app.exec()