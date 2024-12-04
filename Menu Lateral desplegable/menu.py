# -*- coding: utf-8 -*-
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt6.QtWidgets import QApplication, QMainWindow
from Base import fetch_all_data

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("menu.ui", self)

        self.bt_restaurar.setIcon(QtGui.QIcon("imagenes/new-tab.png"))
        self.bt_minimizar.setIcon(QtGui.QIcon("imagenes/minimize.png"))
        self.bt_maximizar.setIcon(QtGui.QIcon("imagenes/maximize.png"))
        self.bt_cerrar.setIcon(QtGui.QIcon("imagenes/cancel.png"))
        self.bt_tool.setIcon(QtGui.QIcon("imagenes/engranaje.png"))
        self.bt_menu.setIcon(QtGui.QIcon("imagenes/hamburger.png"))

        self.bt_restaurar.clicked.connect(self.showNormal)
        self.bt_minimizar.clicked.connect(self.showMinimized)
        self.bt_maximizar.clicked.connect(self.showMaximized)
        self.bt_cerrar.clicked.connect(self.close)
        self.bt_BD.clicked.connect(self.load_data)

        self.bt_tool.clicked.connect(self.show_settings_page)
        self.bt_menu.clicked.connect(self.toggle_side_panel)

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.resize(800, 600)
        self.old_position = None

        self.stackedWidget.setCurrentIndex(0)

        self.bt_load_data.clicked.connect(self.load_data)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(10, 10, 800, 400)
        self.tableWidget.setAlternatingRowColors(True)
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
        self.stackedWidget.setCurrentIndex(1)

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

    def load_data(self):
        query = "SELECT * FROM prototipos"  # Cambia esto por tu consulta
        try:
            columns, data = fetch_all_data(query)  # Llama a la función de conexión
            self.display_data(columns, data)
        except Exception as e:
            print(f"Error al cargar datos: {e}")

    def display_data(self, columns, data):
        self.tableWidget.setRowCount(0)  # Limpia la tabla
        self.tableWidget.setColumnCount(len(columns))  # Define columnas
        self.tableWidget.setHorizontalHeaderLabels(columns)  # Etiquetas de columnas

        # Llena la tabla con datos
        for row_num, row_data in enumerate(data):
            self.tableWidget.insertRow(row_num)
            for col_num, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(cell_data)))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()