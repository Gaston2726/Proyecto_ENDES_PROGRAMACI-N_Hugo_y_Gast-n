class Reserva:
    def __init__(self, numero_reserva, fecha, cliente, cancha):
        self.numero_reserva = numero_reserva
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha
        cliente.saldo -= cancha.precio

    def comprobar_cliente(self, cliente):
        if cliente.saldo <= -2000:
            print("No puedes reservar.")
            return False
        else:
            print("Puedes reservar.")
            return True

    @staticmethod
    def listar_reservas(lista_reservas):
        if not lista_reservas:
            print("No hay reservas.")
        else:
            for reserva in lista_reservas:
                print(f"Reserva {reserva.numero_reserva}: Fecha {reserva.fecha}, Cliente {reserva.cliente.identificador}, Cancha {reserva.cancha.numero_cancha}")


def crear_reserva(lista_reservas, lista_clientes, lista_canchas):
    numero_reserva = int(input("Dime el numero de reserva: "))
    fecha = input("Dime una fecha de reserva: ")
    identificador_cliente = input("Dime el identificador del cliente: ")
    numero_cancha = int(input("Dime el número de la cancha: "))
    
    cliente = lista_clientes.get(identificador_cliente)#si no encuentra al cleinte dira que es none
    cancha = None
    for cancha in lista_canchas:
        if cancha.numero_cancha == numero_cancha:
            cancha = cancha
            break

    if cliente is None:
        print("Cliente no encontrado.")
    elif cancha is None:
        print("Cancha no encontrada.")
    elif not cancha.habilitada:
        print("La cancha no está habilitada para reservas.")
    elif not Reserva().comprobar_cliente(cliente):
        print("El cliente no puede hacer una reserva.")
    else:
        return None

    reserva = Reserva(numero_reserva, fecha, cliente, cancha)
    lista_reservas.append(reserva)
    cancha.lista_reserva.append(reserva)
    print("Reserva creada exitosamente.")
def menu_reservas():
 
    print("1. Crear reserva")
    print("2. Listar reservas actuales de una cancha")
    print("3. Listar reservas de un cliente")
    print("4. Mostrar saldo de un cliente")
    print("5. Salir del menú")
    pcion = int(input("Selecciona una opción: "))

    while opcion !=5:
        opcion = int(input("Selecciona una opción: "))

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

menu_reservas()

"""
def menu_reservs():
    print("1 .-Crear reserva\n2 .-Listar reservas actuales de una cancha\n3 .-Listar reservas de un cliente\n 4.-Mostrar saldo de un cliente\5 salir del menu ")
    opcion=int(input("Dime una de las opciones: "))
    while opcion!=5:
        if opcion==1:
            crear_reserva()
        elif opcion==2:
            Reserva.listar_reservas()
        elif opcion==3:
        elif opcion==4:
        elif opcion==5:
"""
