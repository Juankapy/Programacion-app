# -*- coding: utf-8 -*-
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QPoint , QPropertyAnimation
from PyQt6.QtWidgets import QApplication, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("menu.ui", self)

        # Configurar iconos de los botones
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

        self.bt_tool.clicked.connect(self.show_settings_page)
        self.bt_menu.clicked.connect(self.toggle_side_panel)

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.resize(800, 600)
        self.old_position = None

        self.stackedWidget.setCurrentIndex(0)

        self.is_panel_visible = True

    def mousePressEvent(self, event):
        """Permitir mover la ventana."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_position = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """Permitir mover la ventana."""
        if event.buttons() == Qt.MouseButton.LeftButton and self.old_position:
            delta = QPoint(event.globalPosition().toPoint() - self.old_position)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_position = event.globalPosition().toPoint()

    def show_settings_page(self):
        """Mostrar la página de Ajustes."""
        self.stackedWidget.setCurrentIndex(1)  # Cambiar al índice de ajustes en QStackedWidget

    def toggle_side_panel(self):
        """Mostrar u ocultar el panel lateral con una animación."""
        current_width = self.frame_lateral.width()  # Obtener el ancho actual del panel lateral
        target_width = 0 if current_width > 0 else 200  # Alternar entre 0 y 200

        # Crear una animación para cambiar el ancho
        animation = QPropertyAnimation(self.frame_lateral, b"maximumWidth")
        animation.setDuration(300)  # Duración de la animación en milisegundos
        animation.setStartValue(current_width)
        animation.setEndValue(target_width)
        animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuad)
        animation.start()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()