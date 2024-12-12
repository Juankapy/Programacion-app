from PyQt6.QtWidgets import QApplication
from Login_Sing_in.login_window import LoginWindow  # Asegúrate de que LoginWindow está importado correctamente

if __name__ == "__main__":
    app = QApplication([])  # Crea la aplicación
    window = LoginWindow()  # Crea la ventana de login
    window.show()  # Muestra la ventana de login
    app.exec()  # Ejecuta el bucle de eventos
