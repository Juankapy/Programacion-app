from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt6 import uic
import PyQt6.uic.properties
from App_Menu_Base.menu import QApplication
from auth import login  # Funciones de autenticación
from App_Menu_Base import menu
from App_Menu_Base import Base  # Ventana principal tras login exitoso

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)  # Carga del diseño desde el archivo .ui generado por QtDesigner

        # Conexión de los botones con sus respectivas funciones
        self.pushButton.clicked.connect(self.handle_login)  # Acción para el botón de login

        # Configuración de íconos
        self.bt_restaurar.setIcon(PyQt6.uic.properties.QtGui.QIcon("image/new-tab.png"))
        self.bt_minimizar.setIcon(PyQt6.uic.properties.QtGui.QIcon("image/minimize.png"))
        self.bt_maximizar.setIcon(PyQt6.uic.properties.QtGui.QIcon("image/maximize.png"))
        self.bt_cerrar.setIcon(PyQt6.uic.properties.QtGui.QIcon("image/cancel.png"))

        # Conectar botones
        self.bt_restaurar.clicked.connect(self.showNormal)
        self.bt_minimizar.clicked.connect(self.showMinimized)
        self.bt_maximizar.clicked.connect(self.showMaximized)
        self.bt_cerrar.clicked.connect(self.close)

        # Configurar ventana sin bordes
        self.setWindowFlags(PyQt6.uic.properties.QtCore.Qt.WindowType.FramelessWindowHint)
        self.resize(800, 600)
        self.old_position = None

        # Inicializa el QLabel de mensajes de error como invisible
        self.lb_error.setVisible(False)

    def handle_login(self):
        """
        Maneja el inicio de sesión del usuario al presionar el botón "Login".
        """
        username = self.lineEdit1.text().strip()  # Captura del nombre de usuario
        password = self.lineEdit2.text().strip()  # Captura de la contraseña

        # Validación de campos vacíos
        if not username or not password:
            self.show_error_message("Por favor, complete todos los campos.")
            return

        # Verificar credenciales a través de la función de login en auth.py
        user = login(username, password)
        if user:
            self.lb_error.clear()  # Limpiar el mensaje de error si existe
            self.open_menu_window()  # Abrir ventana de menú principal
        else:
            self.show_error_message("Usuario o contraseña incorrectos.")

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
        self.menu_window = QApplication  # Crea una instancia de la ventana principal
        self.menu_window.show()  # Muestra la ventana principal
        self.close()  # Cierra la ventana de login

    def show_message(self, title, message, icon):
        """
        Muestra un cuadro de mensaje con el título, mensaje y tipo de ícono especificados.
        """
        msg_box = QMessageBox(self)  # Crea un cuadro de mensaje
        msg_box.setWindowTitle("Menudo Error Maquina")  # Establece el título del cuadro
        msg_box.setText("Tienes tremendo error ni nosotros podriamos hacerlo tan mal")  # Establece el texto del mensaje
        msg_box.setIcon(icon)  # Establece el ícono del mensaje
        msg_box.exec_()  # Muestra el cuadro de mensaje

if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec()