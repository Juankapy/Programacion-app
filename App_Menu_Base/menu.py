from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QLineEdit
from Base import fetch_all_data
import subprocess
import sys
import insertar


class MenuWindow(QMainWindow):
    def __init__(self):
        super(MenuWindow, self).__init__()
        uic.loadUi("menu.ui", self)

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
        self.bt_insert.clicked.connect(self.abrir_insertar)
        self.bt_eliminar.clicked.connect(self.abrir_eliminar)
        self.searchButton.clicked.connect(lambda: self.setup_search())
        self.searchbar.returnPressed.connect(self.search_record)

        self.bt_buscar.clicked.connect(self.toggle_search_widget)
        self.bt_empleados.clicked.connect(lambda: self.load_data("empleados"))
        self.bt_gastos.clicked.connect(lambda: self.load_data("gastos"))
        self.bt_prototipos.clicked.connect(lambda: self.load_data("prototipos"))
        self.bt_etapas.clicked.connect(lambda: self.load_data("etapas"))
        self.bt_recursos.clicked.connect(lambda: self.load_data("recursos"))
        self.bt_eli.clicked.connect(self.vaciar_celda)
        self.bt_ins.clicked.connect(self.insertar_datos)
        self.searchbar.returnPressed.connect(self.buscar_por_id)  # Activar búsqueda al presionar Enter



        self.bt_actualizar1 = QtWidgets.QPushButton("Actualizar")
        self.bt_actualizar1.clicked.connect(self.actualizar_datos)

        # Configurar ventana sin bordes
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.resize(800, 600)
        self.old_position = None

        # Configurar QTableWidget
        self.tableWidget.setGeometry(10, 10, 800, 400)
        self.tableWidget.setAlternatingRowColors(True)

        self.searchbar = self.findChild(QLineEdit, "searchbar") # Busca el QLineEdit por su nombre
        self.widget_bar.setVisible(False)

        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.hide_search_widget)

        # Configurar página inicial
        self.stackedWidget.setCurrentWidget(self.page)  # Cambia "page" por la página inicial adecuada

        # Estado inicial del panel lateral
        self.is_panel_visible = True

    def abrir_insertar(self):
        subprocess.Popen(["python", "insertar.py"])

    def abrir_eliminar(self):
        subprocess.Popen(["python", "eliminar.py"])

    def buscar_por_id(self):
        # Obtener el ID ingresado en la barra de búsqueda
        search_id = self.searchbar.text()

        if not search_id.isdigit():
            self.statusBar().showMessage("Por favor ingresa un ID válido")
            return

        # Consulta para buscar el registro por ID
        query = f"SELECT * FROM empleados WHERE ID = {search_id}"  # Asegúrate de que 'ID' es el nombre correcto de la columna

        try:
            columns, data = fetch_all_data(query)  # Llamada a tu función para obtener datos
            self.tableWidget.setRowCount(0)
            if not data:
                self.statusBar().showMessage(f"No se encontraron registros con ID {search_id}.")
                self.tableWidget.setRowCount(0)  # Limpiar la tabla
                return

            self.display_data(columns, data)  # Método para mostrar los datos en tu tabla
            self.statusBar().showMessage(f"Resultados para ID {search_id}:")
        except Exception as e:
            self.statusBar().showMessage(f"Error al buscar: {e}")

    def insertar_datos(self):
        # Obtener la fila y la columna de la celda seleccionada
        current_row = self.tableWidget.currentRow()
        current_column = self.tableWidget.currentColumn()

        if current_row >= 0 and current_column >= 0:
            # Obtener el texto a insertar desde un QLineEdit (por ejemplo, searchbar)
            new_data = self.searchbar.text()  # Suponiendo que uses un campo de búsqueda para ingresar datos

            # Insertar el nuevo dato en la celda seleccionada
            self.tableWidget.setItem(current_row, current_column, QTableWidgetItem(new_data))
            self.statusBar().showMessage("Datos insertados correctamente")
        else:
            self.statusBar().showMessage("Por favor selecciona una celda para insertar datos")

    def vaciar_celda(self):
        # Obtener la fila y la columna de la celda seleccionada
        current_row = self.tableWidget.currentRow()
        current_column = self.tableWidget.currentColumn()

        if current_row >= 0 and current_column >= 0:

            # Vaciar la celda seleccionada
            self.tableWidget.setItem(current_row, current_column, QTableWidgetItem(""))
            self.statusBar().showMessage("Celda vaciada correctamente")
        else:
            self.statusBar().showMessage("Por favor selecciona una celda para vaciar")

    def setup_search(self):
        # Conectar el botón de búsqueda o el evento de enter en el campo de texto
        self.searchbar.returnPressed.connect(self.search_record)  # Reemplaza "searchLineEdit" con el nombre correcto
        self.searchButton.clicked.connect(self.search_record)  # Si tienes un botón de búsqueda

    def search_record(self):
        # Obtener el texto del campo de búsqueda
        search_id = self.searchbar.text()

        if not search_id.isdigit():
            self.statusBar().showMessage("Por favor ingresa un ID válido")
            return

        # Consulta a la base de datos
        query = f"SELECT * FROM empleados WHERE ID = {search_id}"
        try:
            _, result = fetch_all_data(query)

            if not result:
                self.statusBar().showMessage("No se encontró información para este ID")
                return

            # Extraer los datos
            DNI,Nombre,Titulacion, email, Años_experiencia, tipo_via, nombre_via, codigo_postal, localidad, provincia = result[0]

            # Llenar los campos
            self.dni.setText(str(DNI))  # Reemplaza con el nombre real de tu widget
            self.nom.setText(str(Nombre))
            self.titu.setText(str(Titulacion))
            self.email.setText(email)
            self.via.setText(str(tipo_via))
            self.exp.setText(str(Años_experiencia))
            self.nom.setText(str(nombre_via))
            self.cp.setText(str(codigo_postal))
            self.localidad.setText(str(localidad))
            self.provincia.setText(str(provincia))

            self.statusBar().showMessage("Datos cargados correctamente")
        except Exception as e:
            self.statusBar().showMessage(f"Error al buscar datos: {e}")
        self.setup_search()

    def toggle_search_widget(self):
        if self.widget_bar.isVisible():
            self.hide_search_widget()
        else:
            self.show_search_widget()

    def show_search_widget(self):
        self.widget_bar.setVisible(True)
        self.timer.stop()  # Detener el temporizador si estaba corriendo
        # Aquí puedes agregar la animación para mostrar el widget

    def hide_search_widget(self):
        self.widget_bar.setVisible(False)
        self.timer.start(2000)  # Iniciar el temporizador para ocultar después de 2 segundos

    def update_display(self, text):
        for label in self.labels:
            if text.lower() in label.text().lower():
                label.show()
            else:
                label.hide()

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

    def actualizar_datos(self):
        # Puedes llamar a load_data con el nombre de la tabla que deseas actualizar
        self.load_data("empleados")  # Cambia "empleados" por la tabla que desees actualizar

    def load_data(self, table_name):
        query = f"SELECT * FROM {table_name}"  # Asegúrate de que 'table_name' es seguro
        print(f"Ejecutando consulta: {query}")

        try:
            columns, data = fetch_all_data(query)  # Llamada a tu función
            if not data:
                print(f"La tabla '{table_name}' está vacía.")
            self.display_data(columns, data)  # Metodo para mostrar los datos en tu tabla
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
    window = MenuWindow()
    window.show()
    app.exec()
