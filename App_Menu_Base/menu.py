from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from Base import fetch_all_data  # Importar la configuración desde tu archivo de conexión

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("menu.ui", self)

        # Configuración de íconos
        self.bt_restaurar.setIcon(QtGui.QIcon("imagenes/new-tab.png"))
        self.bt_minimizar.setIcon(QtGui.QIcon("imagenes/minimize.png"))
        self.bt_maximizar.setIcon(QtGui.QIcon("imagenes/maximize.png"))
        self.bt_cerrar.setIcon(QtGui.QIcon("imagenes/cancel.png"))
        self.bt_tool.setIcon(QtGui.QIcon("imagenes/engranaje.png"))
        self.bt_menu.setIcon(QtGui.QIcon("imagenes/hamburger.png"))
        self.bt_BD.setIcon(QtGui.QIcon("imagenes/database.png"))
        self.setWindowIcon(QtGui.QIcon("imagenes/Logo .ico"))

        # Conectar botones
        self.bt_restaurar.clicked.connect(self.showNormal)
        self.bt_minimizar.clicked.connect(self.showMinimized)
        self.bt_maximizar.clicked.connect(self.showMaximized)
        self.bt_cerrar.clicked.connect(self.close)
        self.bt_BD.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_uno))
        self.bt_tool.clicked.connect(self.show_settings_page)
        self.bt_menu.clicked.connect(self.toggle_side_panel)

        # Botones para cargar datos de las tablas
        self.bt_empleados.clicked.connect(lambda: self.load_data("empleados"))
        self.bt_gastos.clicked.connect(lambda: self.load_data("gastos"))
        self.bt_prototipos.clicked.connect(lambda: self.load_data("prototipos"))
        self.bt_etapas.clicked.connect(lambda: self.load_data("etapas"))
        self.bt_recursos.clicked.connect(lambda: self.load_data("recursos"))

        # Configurar ventana sin bordes
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.resize(800, 600)
        self.old_position = None

        # Configurar QTableWidget
        self.tableWidget.setGeometry(10, 10, 800, 400)
        self.tableWidget.setAlternatingRowColors(True)

        # Configurar página inicial
        self.stackedWidget.setCurrentWidget(self.page)  # Cambia "page" por la página inicial adecuada

        # Estado inicial del panel lateral
        self.is_panel_visible = True

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_position = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.old_position:
            delta = QPoint(event.globalPosition().toPoint() - self.old_position)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_position = event.globalPosition().toPoint()

    def show_settings_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def toggle_side_panel(self):
        current_width = self.frame_lateral.width()
        target_width = 0 if current_width > 0 else 200

        animation = QPropertyAnimation(self.frame_lateral, b"maximumWidth")
        animation.setDuration(300)
        animation.setStartValue(current_width)
        animation.setEndValue(target_width)
        animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuad)
        animation.start()

        if self.is_panel_visible:
            self.bt_menu.setIcon(QtGui.QIcon("imagenes/hamburger-open.png"))
        else:
            self.bt_menu.setIcon(QtGui.QIcon("imagenes/hamburger.png"))
        self.is_panel_visible = not self.is_panel_visible

    def load_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        print(f"Ejecutando consulta: {query}")

        try:
            columns, data = fetch_all_data(query)
            if not data:
                print(f"La tabla '{table_name}' está vacía.")
            self.display_data(columns, data)
        except Exception as e:
            print(f"Error al cargar datos de la tabla '{table_name}': {e}")

    def display_data(self, columns, data):
        if not data:
            # Si no hay datos, mostrar el mensaje y ocultar la tabla
            self.lbl_no_data.setVisible(True)
            self.tableWidget.setVisible(False)
            return

        # Ocultar el mensaje y mostrar la tabla
        self.lbl_no_data.setVisible(False)
        self.tableWidget.setVisible(True)

        # Configurar el QTableWidget con los datos
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)

        for row_num, row_data in enumerate(data):
            self.tableWidget.insertRow(row_num)
            for col_num, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(cell_data)))

        # Cambiar a la página que contiene el QTableWidget
        self.stackedWidget.setCurrentWidget(self.page_uno)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
