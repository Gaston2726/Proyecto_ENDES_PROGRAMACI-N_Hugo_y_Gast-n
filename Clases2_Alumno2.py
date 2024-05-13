class Empleados():
    def __init__(self):
        self.lista_tareas = {}

    def registrar_empleado(self):
        nombre = input("Escribe tu nombre o el nombre del cliente: ")
        apellido1 = input("Escribe el primer apellido: ")
        apellido2 = input("Escribe el segundo apellido: ")
        desocupado = input("¿Está desocupado? (SI/NO): ").upper() == 'SI'
        
        self.lista_tareas[nombre] = {'nombre': nombre, 'apellido1': apellido1, 'apellido2': apellido2, 'desocupado': desocupado}
        print("El cliente se ha creado")

    def asignar_tarea(self):
        nombre = input("Escribe el nombre del empleado al que deseas asignar la tarea: ")
        if nombre in self.lista_tareas:
            tarea = input("Escribe la tarea que deseas asignar: ")
            if 'tareas' not in self.lista_tareas[nombre]:
                self.lista_tareas[nombre]['tareas'] = [tarea]
            else:
                self.lista_tareas[nombre]['tareas'].append(tarea)
            print(f"Tarea asignada a {nombre}: {tarea}")
        else:
            print("El empleado no está en la lista de tareas.")

    def mostrar_clientes(self):
        if not self.lista_tareas:
            print("No hay clientes registrados")
        else:
            for nombre, detalles in self.lista_tareas.items():
                print(f"Nombre: {nombre}, Apellidos: {detalles['apellido1']} {detalles['apellido2']}, Ocupado: {detalles['desocupado']}")

    def eliminar_empleado(self):
        nombre = input("Escribe el nombre del cliente que desea eliminar: ")
        if nombre in self.lista_tareas:
            del self.lista_tareas[nombre]
            print("El cliente se ha eliminado")
        else:
            print("El cliente no se ha encontrado")