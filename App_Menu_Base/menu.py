from PyQt6 import QtGui, uic
from PyQt6.QtWidgets import QMainWindow


class MenuWindow(QMainWindow):
    def __init__(self):
        super(MenuWindow, self).__init__()
        uic.loadUi("C:/Users/mrnat/Desktop/Repo-clase/Programacion-app/App_Menu_Base/menu.ui", self)

        # Configuración de íconos
        self.bt_restaurar.setIcon(QtGui.QIcon("imagenes/new-tab.png"))
        self.bt_minimizar.setIcon(QtGui.QIcon("imagenes/minimize.png"))
        self.bt_maximizar.setIcon(QtGui.QIcon("imagenes/maximize.png"))
        self.bt_cerrar.setIcon(QtGui.QIcon("imagenes/cancel.png"))
        self.bt_tool.setIcon(QtGui.QIcon("imagenes/engranaje.png"))
        self.bt_menu.setIcon(QtGui.QIcon("imagenes/hamburger.png"))
        self.bt_BD.setIcon(QtGui.QIcon("imagenes/database.png"))
        self.bt_buscador.setIcon(QtGui.QIcon("imagenes/lupa.png"))
        self.searchButton.setIcon(QtGui.QIcon("imagenes/magnifying-glass.png"))

        self.setWindowIcon(QtGui.QIcon("imagenes/Logo .ico"))

        # Conectar botones
        self.bt_restaurar.clicked.connect(self.showNormal)
        self.bt_minimizar.clicked.connect(self.showMinimized)
        self.bt_maximizar.clicked.connect(self.showMaximized)
        self.bt_cerrar.clicked.connect(self.close)
        self.bt_BD.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_uno))
        self.bt_tool.clicked.connect(self.show_settings_page)
        self.bt_menu.clicked.connect(self.toggle_side_panel)
        self.bt_insert.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_tres))
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_cuatro))
        self.searchButton.clicked.connect(lambda: self.setup_search())

        self.bt_buscar.clicked.connect(self.toggle_search_widget)
        self.bt_empleados.clicked.connect(lambda: self.load_data("empleados"))
        self.bt_gastos.clicked.connect(lambda: self.load_data("gastos"))
        self.bt_prototipos.clicked.connect(lambda: self.load_data("prototipos"))
        self.bt_etapas.clicked.connect(lambda: self.load_data("etapas"))
        self.bt_recursos.clicked.connect(lambda: self.load_data("recursos"))

        # Configurar ventana sin bordes
        self.setWindowFlags(QtGui.Qt.WindowType.FramelessWindowHint)
        self.resize(800, 600)
        self.old_position = None

        # Configurar QTableWidget
        self.tableWidget.setGeometry(10, 10, 800, 400)
        self.tableWidget.setAlternatingRowColors(True)

        self.searchbar = self.findChild(QtGui.QLineEdit, "searchbar")  # Busca el QLineEdit por su nombre
        self.widget_bar.setVisible(False)

        self.timer = QtGui.QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.hide_search_widget)

        # Configurar página inicial
        self.stackedWidget.setCurrentWidget(self.page)  # Cambia "page" por la página inicial adecuada

        # Estado inicial del panel lateral
        self.is_panel_visible = True


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication

    app = QApplication([])  # Crear QApplication si este archivo se ejecuta directamente
    window = MenuWindow()
    window.show()
    app.exec()