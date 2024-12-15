import mysql.connector
print("Bienvenido al programa CRUD de Empleados.")

# Conexión a la Base de Datos
def conectar_bd():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="prototipos",
            port="3307",
            collation = "utf8mb4_general_ci"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None


# Crear un nuevo empleado
def insertar_empleado():
    connection = conectar_bd()
    if connection:
        cursor = connection.cursor()
        try:
            dni = input("Ingresa el DNI: ")
            nombre = input("Ingresa el nombre: ")
            titulacion = input("Ingresa la titulación: ")
            email = input("Ingresa el email: ")
            anios_experiencia = int(input("Ingresa los años de experiencia: "))
            tipo_via = input("Ingresa el tipo de vía (calle, avenida, plaza): ")
            nombre_via = input("Ingresa el nombre de la vía: ")
            codigo_postal = input("Ingresa el código postal: ")
            localidad = input("Ingresa la localidad: ")
            provincia = input("Ingresa la provincia: ")

            query = """
                INSERT INTO empleados (
                    DNI, Nombre, Titulacion, email, Años_experiencia, 
                    tipo_via, nombre_via, codigo_postal, localidad, provincia
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (dni, nombre, titulacion, email, anios_experiencia,
                                   tipo_via, nombre_via, codigo_postal, localidad, provincia))
            connection.commit()
            print("Empleado agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al insertar datos: {err}")
        finally:
            cursor.close()
            connection.close()


# Leer empleados
def leer_empleados():
    connection = conectar_bd()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM empleados")
            results = cursor.fetchall()
            print(
                "ID | DNI | Nombre | Titulación | Email | Años de Experiencia | Tipo de Vía | Nombre de Vía | Código Postal | Localidad | Provincia")
            print("-" * 120)
            for row in results:
                print(row)
        except mysql.connector.Error as err:
            print(f"Error al leer los datos: {err}")
        finally:
            cursor.close()
            connection.close()


# Actualizar empleado
def actualizar_empleado():
    fields = [
        "DNI", "Nombre", "Titulacion", "email", "Años_experiencia",
        "tipo_via", "nombre_via", "codigo_postal", "localidad", "provincia"
    ]
    connection = conectar_bd()
    if connection:
        cursor = connection.cursor()
        try:
            emp_id = int(input("Ingrese el ID del empleado que desea actualizar: "))
            print("Ingrese los campos que desea actualizar:")
            print(", ".join(f"{index + 1}. {field}" for index, field in enumerate(fields)))
            selected_fields = input("Elija los campos separados por coma (ejemplo: 1,2,5): ").split(",")
            updates = {}

            for index in selected_fields:
                try:
                    field_index = int(index.strip()) - 1
                    if field_index < 0 or field_index >= len(fields):
                        print(f"Opción inválida: {index}")
                        continue
                    field_name = fields[field_index]
                    new_value = input(f"Ingrese el nuevo valor para {field_name}: ")
                    updates[field_name] = new_value
                except ValueError:
                    print(f"Opción inválida: {index}")

            # Removed line

            query_parts = [f"{field} = %s" for field in updates.keys()]
            query = f"UPDATE empleados SET {', '.join(query_parts)} WHERE ID = %s"
            values = list(updates.values()) + [emp_id]
            cursor.execute(query, values)
            connection.commit()

            if cursor.rowcount > 0:
                print("Empleado actualizado correctamente.")
            else:
                print("Empleado no encontrado.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar los datos: {err}")
        finally:
            cursor.close()
            connection.close()


# Eliminar empleado
def eliminar_empleado():
    connection = conectar_bd()
    if connection:
        cursor = connection.cursor()
        try:
            emp_id = int(input("Ingrese el ID del empleado que desea eliminar: "))

            query = "DELETE FROM empleados WHERE ID = %s"
            cursor.execute(query, (emp_id,))
            connection.commit()

            if cursor.rowcount > 0:
                print("Empleado eliminado correctamente.")
            else:
                print("Empleado no encontrado.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar los datos: {err}")
        finally:
            cursor.close()
            connection.close()


# Menú principal
def main_menu():
    while True:
        print("\n--- MENÚ CRUD EMPLEADOS ---")
        print("1. Crear nuevo empleado")
        print("2. Leer empleados")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("5. Salir")
        choice = input("Selecciona una opción (1-5): ")

        if choice == "1":
            insertar_empleado()
        elif choice == "2":
            leer_empleados()
        elif choice == "3":
            actualizar_empleado()
        elif choice == "4":
            eliminar_empleado()
        elif choice == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    main_menu()