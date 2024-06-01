from datetime import datetime

class Reserva:
    def __init__(self, numero_reserva, fecha, cliente, cancha):
        self.numero_reserva = numero_reserva
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha

    def __str__(self):
        return f"Número de Reserva: {self.numero_reserva}, Fecha: {self.fecha}, Cliente: {self.cliente}, Cancha: {self.cancha}"

    @staticmethod
    def crear_reserva(lista_reservas, cliente, cancha, fecha):
        """
        Crea una reserva.
        """
        if not cliente.habilitado:
            print("El cliente no está habilitado para realizar reservas.")
            return False
        if not cancha.habilitada:
            print("La cancha no está habilitada para reservas.")
            return False
        if not cancha.esta_desocupada_en_fecha(fecha):
            print("La cancha no está desocupada en esa fecha.")
            return False
        if cliente.saldo < -2000:
            print("El cliente tiene un saldo negativo mayor a -2000, no puede realizar más reservas.")
            return False

        nueva_reserva = Reserva(len(lista_reservas) + 1, fecha, cliente, cancha)
        lista_reservas.append(nueva_reserva)
        cliente.saldo -= cancha.precio
        print("Reserva creada exitosamente.")
        return True

    @staticmethod
    def listar_reservas_cancha(lista_reservas, cancha):
        """
        Lista las reservas de una cancha.
        """
        reservas_cancha = [reserva for reserva in lista_reservas if reserva.cancha == cancha]
        if reservas_cancha:
            for reserva in reservas_cancha:
                print(reserva)
        else:
            print("No hay reservas para esta cancha.")

    @staticmethod
    def listar_reservas_cliente(lista_reservas, cliente):
        """
        Lista las reservas de un cliente.
        """
        reservas_cliente = [reserva for reserva in lista_reservas if reserva.cliente == cliente]
        if reservas_cliente:
            for reserva in reservas_cliente:
                print(reserva)
        else:
            print("El cliente no tiene reservas.")

    @staticmethod
    def registrar_pago(cliente, monto):
        """
        Registra el pago del cliente.
        """
        cliente.saldo += monto
        print("Pago registrado exitosamente.")

    @staticmethod
    def mostrar_saldo_cliente(cliente):
        """
        Muestra el saldo del cliente.
        """
        print(f"Saldo del cliente {cliente}: {cliente.saldo}")

    @staticmethod
    def buscar_cliente_por_nombre(lista_clientes, nombre):
        """
        Busca un cliente por nombre en la lista de clientes.
        """
        for cliente in lista_clientes:
            if cliente.nombre == nombre:
                return cliente
        return None

    @staticmethod
    def buscar_cancha_por_numero(lista_canchas, numero):
        """
        Busca una cancha por número en la lista de canchas.
        """
        for cancha in lista_canchas:
            if cancha.numero_cancha == numero:
                return cancha
        return None

    @staticmethod
    def validar_fecha(fecha):
        """
        Valida el formato de fecha.
        """
        try:
            return datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            return None

def menu_reserva(lista_reservas, lista_clientes, lista_canchas):
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
