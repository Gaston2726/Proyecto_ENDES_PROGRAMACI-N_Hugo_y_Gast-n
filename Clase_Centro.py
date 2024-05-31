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
        opcion = input("Elige una opción: ")
        while opcion!=5:
            print("\nMenú de Opciones")
            print("1. Crear una cancha")
            print("2. Agregar una cancha a la lista del centro")
            print("3. Listar las canchas totales según un tipo de deporte")
            print("4. Quitar una cancha de la lista del centro")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                nueva_cancha = crear_cancha()
                lista_cancha.append(nueva_cancha)
            elif opcion == '2':
                if lista_cancha:
                    nueva_cancha.agregar_cancha(lista_cancha)
                else:
                    print("Primero debes crear una cancha.")
            elif opcion == '3':
                Cancha.lista_canchas_deporte(lista_cancha)
            elif opcion == '4':
                Cancha.eliminar_cancha_de_centro(lista_cancha)
            elif opcion == '5':
                print("Saliendo del programa.")
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
    def menu_reservas():
        print("1. Crear reserva")
        print("2. Listar reservas actuales de una cancha")
        print("3. Listar reservas de un cliente")
        print("4. Mostrar saldo de un cliente")
        print("5. Salir del menú")
        opcion = int(input("Selecciona una opción: "))
        while opcion != 5:

            if opcion == 1:
                crear_reserva(lista_reservas, lista_clientes, lista_canchas)
            elif opcion == 2:
                numero_cancha = int(input("Ingrese el número de la cancha: "))
                cancha_encontrada = None
                for cancha in lista_canchas:
                    if cancha.numero_cancha == numero_cancha:
                        cancha_encontrada = cancha
                        break
                if cancha_encontrada:
                    Reserva.listar_reservas(cancha_encontrada.lista_reserva)
                else:
                    print("No se encontró la cancha.")
            elif opcion == 3:
                identificador_cliente = input("Ingrese el identificador del cliente: ")
                cliente = lista_clientes.get(identificador_cliente)
                if cliente:
                    Reserva.listar_reservas([reserva for reserva in lista_reservas if reserva.cliente == cliente])
                else:
                    print("No se encontró el cliente.")
            elif opcion == 4:
                identificador_cliente = input("Ingrese el identificador del cliente: ")
                cliente = lista_clientes.get(identificador_cliente)
                if cliente:
                    print(f"Saldo del cliente {cliente.identificador}: {cliente.saldo}")
                else:
                    print("No se encontró el cliente.")
            elif opcion == 5:
                print("Saliendo del menú...")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
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