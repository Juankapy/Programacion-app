from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QGridLayout
)
from Base import insert_or_update_data  # Importar la función desde base.py


class EmpleadoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Empleados")
        self.setGeometry(200, 200, 800, 600)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QVBoxLayout()
        search_layout = QHBoxLayout()
        form_layout = QGridLayout()
        button_layout = QHBoxLayout()

        # Buscador
        self.search_input = QLineEdit()
        self.search_button = QPushButton("Buscar")
        search_layout.addWidget(QLabel("Buscar DNI:"))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        # Campos de empleado
        self.fields = {}
        labels = ["DNI", "Nombre", "Titulacion", "Email", "Tipo de via",
                  "Años Experiencia", "CP", "Nombre via", "Localidad", "Provincia"]

        for i, label in enumerate(labels):
            lbl = QLabel(label)
            input_field = QLineEdit()
            self.fields[label.lower()] = input_field
            form_layout.addWidget(lbl, i // 2, (i % 2) * 2)
            form_layout.addWidget(input_field, i // 2, (i % 2) * 2 + 1)

        # Botón Insertar/Actualizar
        self.insert_button = QPushButton("Insertar/Actualizar")
        button_layout.addWidget(self.insert_button)

        # Agregar layouts principales
        main_layout.addLayout(search_layout)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        central_widget.setLayout(main_layout)

        # Conexiones
        self.insert_button.clicked.connect(self.insert_update_employee)

    def insert_update_employee(self):
        # Preparar datos del formulario para la base de datos
        data = {key.replace(" ", "_"): field.text().strip() for key, field in self.fields.items()}
        try:
            insert_or_update_data("empleados", data)  # Llama a la función importada
            print("Datos insertados/actualizados en la base de datos.")
        except Exception as e:
            print(f"Error al insertar/actualizar datos: {e}")

    def clear_fields(self):
        for field in self.fields.values():
            field.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = EmpleadoWindow()
    window.show()
    app.exec()
