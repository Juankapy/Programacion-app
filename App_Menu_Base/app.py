import sys
from PyQt5.QtWidgets import QApplication
from Login_Sing_in.login_window import LoginWindow  # Verifica que login_window.py exista y tiene la clase LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear e iniciar la ventana de login
    login_window = LoginWindow()
    login_window.show()  # Mostrar la ventana de login

    sys.exit(app.exec_())  # Ejecutar el bucle de eventos de la aplicación
