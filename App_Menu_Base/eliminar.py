from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QLineEdit, QPushButton, QHBoxLayout, QLabel
)
from Base import fetch_all_data, get_database_connection


class EmpleadoWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Empleados")
        self.setGeometry(200, 200, 800, 600)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QVBoxLayout()

        # Layout para búsqueda
        search_layout = QHBoxLayout()
        label_dni = QLabel("DNI/NIF:")
        self.search_input = QLineEdit()
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.search_by_dni)  # Conecta el botón de búsqueda a la acción

        search_layout.addWidget(label_dni)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        # Tabla visual para empleados
        self.employee_table = QTableWidget()
        self.employee_table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows)  # Selección por filas completas

        # Botón para eliminar registros
        self.delete_button = QPushButton("Eliminar Seleccionado")
        self.delete_button.clicked.connect(self.handle_delete_selected)  # Acción de eliminación

        # Añadir widgets al layout principal
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.employee_table)
        main_layout.addWidget(self.delete_button)

        central_widget.setLayout(main_layout)

        # Cargar todos los empleados al inicio
        self.show_all_employees()

    def show_all_employees(self):
        """
        Carga todos los registros de la tabla empleados y los muestra con todas las columnas.
        """
        query = "SELECT * FROM empleados"
        try:
            columns, data = fetch_all_data(query)  # Obtén todas las columnas y datos

            if not data:
                print("No hay registros en la tabla empleados.")
                self.employee_table.setRowCount(0)  # Limpiamos la tabla si no hay datos
                return

            # Configurar el número de columnas en la tabla con base en las columnas obtenidas de la consulta
            self.employee_table.setColumnCount(len(columns))
            self.employee_table.setHorizontalHeaderLabels(columns)

            # Rellenar la tabla con los datos obtenidos
            self.employee_table.setRowCount(len(data))
            for row_num, row_data in enumerate(data):
                for col_num, cell_data in enumerate(row_data):
                    self.employee_table.setItem(row_num, col_num, QTableWidgetItem(str(cell_data)))

        except Exception as e:
            print(f"Error al cargar los datos de los empleados: {e}")

    def search_by_dni(self):
        """
        Busca un empleado en la base de datos usando el DNI/NIF y muestra los resultados.
        """
        dni = self.search_input.text().strip()
        if not dni:
            print("Por favor, introduce un DNI/NIF válido.")
            return

        query = "SELECT * FROM empleados WHERE dni = %s"
        try:
            columns, data = fetch_all_data(query, (dni,))  # Filtra los datos usando el campo DNI/NIF

            if not data:
                print(f"No se encontró ningún registro con el DNI/NIF: {dni}.")
                self.employee_table.setRowCount(0)  # Limpiar tabla si no hay datos
                return

            # Actualiza la tabla con los datos encontrados
            self.employee_table.setColumnCount(len(columns))
            self.employee_table.setHorizontalHeaderLabels(columns)
            self.employee_table.setRowCount(len(data))
            for row_num, row_data in enumerate(data):
                for col_num, cell_data in enumerate(row_data):
                    self.employee_table.setItem(row_num, col_num, QTableWidgetItem(str(cell_data)))

        except Exception as e:
            print(f"Error al realizar la búsqueda por DNI/NIF: {e}")

    def handle_delete_selected(self):
        """
        Elimina la fila seleccionada de la base de datos usando el valor de la columna DNI/NIF.
        """
        selected_row = self.employee_table.currentRow()
        if selected_row == -1:
            print("Selecciona un registro para eliminar.")
            return

        # Obtener el DNI/NIF de la fila seleccionada (columna especificada)
        dni = self.employee_table.item(selected_row, 2).text()  # La columna 2 es `dni`
        if not dni:
            print("No se encontró un DNI/NIF en la fila seleccionada.")
            return

        try:
            conn = get_database_connection()
            cursor = conn.cursor()

            # Ejecutar consulta para eliminar registros con un DNI/NIF específico
            query = "DELETE FROM empleados WHERE dni = %s"
            cursor.execute(query, (dni,))
            conn.commit()

            print(f"Se eliminó el registro con DNI/NIF: {dni}.")
            self.show_all_employees()  # Recargar tabla después de eliminar un registro

        except Exception as e:
            print(f"Error al eliminar el registro: {e}")

        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    app = QApplication([])
    window = EmpleadoWindow2()
    window.show()
    app.exec()