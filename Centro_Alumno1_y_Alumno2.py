import Clases_Alumno2 as Gestion_cliente
import Clases2_Alumno2 as Gestion_empleados

class Centro:
    def __init__(self, nombre_centro, direccion):
        self.nombre_centro = nombre_centro
        self.direccion = direccion
        self.lista_cancha = []
        self.lista_clientes = Gestion_cliente.Cliente.lista_clientes
        self.lista_empleados = Gestion_empleados.Empleados().lista_tareas

    @staticmethod
    def menu():
        nombre_centro = input("Dime el nombre del centro: ")
        direccion = input("Dime la dirección del centro: ")
        centro = Centro(nombre_centro, direccion)

        print("Elige una de las opciones siguientes:")
        print("1 .- Gestión de canchas")
        print("2 .- Gestión de cliente")
        print("3 .- Gestión de reserva")
        print("4 .- Gestión de empleado")
        print("5 .- Salir del programa")

        while True:
            op1_menu = int(input("Dime qué opción eliges del menú: "))
            if op1_menu == 1:
                # Gestión de canchas
                print("Gestión de canchas no implementada aún.")
            elif op1_menu == 2:
                Centro.gestion_cliente(centro)
            elif op1_menu == 3:
                print("Gestión de reserva no implementada aún.")
            elif op1_menu == 4:
                Centro.gestion_empleados(centro)
            elif op1_menu == 5:
                print("Se cierra el programa")
                break
            else:
                print("Opción no válida, por favor elige otra vez.")

    @staticmethod
    def gestion_cliente(centro):
        print("1.- Crear cliente")
        print("2.- Mostrar clientes morosos")
        print("3.- Eliminar cliente")
        print("4.- Agregar cliente a la lista de morosos")
        print("5.- Volver al menú principal")

        cliente = Gestion_cliente.Cliente()
        while True:
            opcion = int(input("Escoge una opción: "))
            if opcion == 1:
                cliente.crear_cliente()
            elif opcion == 2:
                cliente.mostrar_clientes_morosos()
            elif opcion == 3:
                cliente.eliminar_cliente()
            elif opcion == 4:
                Gestion_cliente.Cliente.agregar_cliente_centro()
            elif opcion == 5:
                break
            else:
                print("Opción no válida, por favor elige otra vez.")

    @staticmethod
    def gestion_empleados(centro):
        print("1.- Registrar empleado")
        print("2.- Asignar tarea")
        print("3.- Mostrar empleados desocupados")
        print("4.- Eliminar empleado")
        print("5.- Volver al menú principal")

        empleados = Gestion_empleados.Empleados()
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
                break
            else:
                print("Opción no válida, por favor elige otra vez.")

Centro.menu()