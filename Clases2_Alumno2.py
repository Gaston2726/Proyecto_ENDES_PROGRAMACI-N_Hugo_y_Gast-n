class Empleados:
    def __init__(self):
        self.lista_tareas = {}

    def registrar_empleado(self):
        nombre = input("Escribe tu nombre o el nombre del cliente: ")
        apellido1 = input("Escribe el primer apellido: ")
        apellido2 = input("Escribe el segundo apellido: ")
        desocupado = input("¿Está desocupado? (SI/NO): ").upper() == 'SI'
        
        self.lista_tareas[nombre] = {
            'nombre': nombre,
            'apellido1': apellido1,
            'apellido2': apellido2,
            'desocupado': desocupado,
            'tareas': []
        }
        print("El cliente se ha creado")

    def asignar_tarea(self):
        nombre = input("Escribe el nombre del empleado al que deseas asignar la tarea: ")
        if nombre in self.lista_tareas:
            tarea = input("Escribe la tarea que deseas asignar: ")
            self.lista_tareas[nombre]['tareas'].append(tarea)
            print(f"Tarea asignada a {nombre}: {tarea}")
        else:
            print("El empleado no está en la lista de tareas.")

    def mostrar_empleados_desocupados(self):
        if not self.lista_tareas:
            print("No hay clientes registrados")
        else:
            for nombre, detalles in self.lista_tareas.items():
                desocupado_str = "SI" if detalles['desocupado'] else "NO"
                print(f"Nombre: {nombre}, Apellidos: {detalles['apellido1']} {detalles['apellido2']}, Ocupado: {desocupado_str}")

    def eliminar_empleado(self):
        nombre = input("Escribe el nombre del cliente que desea eliminar: ")
        if nombre in self.lista_tareas:
            del self.lista_tareas[nombre]
            print("El cliente se ha eliminado")
        else:
            print("El cliente no se ha encontrado")

def menu():
    empleados = Empleados()
    print("Bienvenido a la gestión de empleados")
    print("1.- Registrar empleado")
    print("2.- Asignar tarea")
    print("3.- Mostrar empleados desocupados")
    print("4.- Quitar empleado")
    print("5.- Salir")
    try:
        while True:
            opcion = int(input("Escoge una opción: "))
            if opcion == 1:
                empleados.registrar_empleado()
            elif opcion == 2:
                empleados.asignar_tarea()
            elif opcion == 3:
                empleados.mostrar_empleados_desocupados()
            elif opcion == 4:
                empleados.eliminar_empleado()
            elif opcion == 5:
                print("Adiós")
                break
            else:
                print("Opción no válida, por favor elige otra vez.")
    except ValueError as err:
        print("La opción debe ser un entero", err)