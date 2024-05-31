import Clases_Alumno2 as Gestion_cliente
import Clases2_Alumno2 as Gestion_empleados
import Clase_Cancha1 as Gestion_cancha
import Clases_Reserva1 as Gestion_reserva

class Centro:
    def __init__(self, nombre_centro, direccion):
        self.nombre_centro = nombre_centro
        self.direccion = direccion
        self.lista_cancha = Gestion_cancha.Cancha.lista_cancha
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
                Centro.gestion_cancha(centro)
                print("Gestión de canchas no implementada aún.")
            elif op1_menu == 2:
                Centro.gestion_cliente(centro)
            elif op1_menu == 3:
                Centro.gestion_reserva(centro)
                print("Gestión de reserva no implementada aún.")
            elif op1_menu == 4:
                Centro.gestion_empleados(centro)
            elif op1_menu == 5:
                print("Se cierra el programa")
                break
            else:
                print("Opción no válida, por favor elige otra vez.")

    @staticmethod
    def gestion_cancha():
        if opcion == 1:
            cancha = crear_cancha()
            lista_canchas.append(cancha)
        elif opcion == 2:
            if lista_canchas:
                numero_cancha = int(input("Ingrese el número de cancha: "))
                if not any(cancha.numero_cancha == numero_cancha for cancha in lista_canchas):
                    nueva_cancha = crear_cancha()
                    lista_canchas.append(nueva_cancha)
                else:
                    print("La cancha ya está registrada en la lista.")
            else:
                print("Primero debes crear una cancha.")
        elif opcion == 3:
            Cancha.lista_canchas_deporte(lista_canchas)
        elif opcion == 4:
            Cancha.eliminar_cancha_de_centro(lista_canchas)
        else:
            print("Opción no válida, por favor elige otra vez.")
        
        opcion = int(input("Elige una opción: "))

    print("Saliendo del programa.")



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
    def menu_reservas():
        """
        Muestra un menú para la gestión de reservas.
        """
        print("\nMenú de Reservas")
        print("1. Crear una reserva")
        print("2. Listar reservas de una cancha")
        print("3. Listar reservas de un cliente")
        print("4. Registrar pago de un cliente")
        print("5. Mostrar saldo de un cliente")
        print("6. Salir")

        opcion = int(input("Elige una opción: "))

        while opcion != 6:
            if opcion == 1:
                Reserva.crear_reserva(lista_reservas, lista_clientes, lista_canchas)
            elif opcion == 2:
                Reserva.listar_reservas_cancha(lista_reservas, lista_canchas)
            elif opcion == 3:
                Reserva.listar_reservas_cliente(lista_reservas, lista_clientes)
            elif opcion == 4:
                Reserva.registrar_pago(lista_clientes)
            elif opcion == 5:
                Reserva.mostrar_saldo_cliente(lista_clientes)
            else:
                print("Opción no válida, por favor elige otra vez.")

            opcion = int(input("Elige una opción: "))

        print("Saliendo del menú de reservas.")
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