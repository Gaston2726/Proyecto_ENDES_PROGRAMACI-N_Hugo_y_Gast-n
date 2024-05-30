class Reserva:
    def __init__(self, numero_cancha, deporte, precio, habilitada, numero_reserva, fecha):
        self.numero_cancha = numero_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.numero_reserva = numero_reserva
        self.fecha = fecha

    def comprobar_cliente(self):
        saldo = int(input("Dime tu saldo: "))
        if saldo <= -2000:
            print("No puedes reservar.")
            return False
        else:
            print("Puedes reservar.")
            return True

def crear_reserva(cancha, numero_reserva, fecha):
    if not cancha.habilitada:
        print("La cancha no está habilitada para reservas.")
        return
    if cancha.lista_reserva:
        print("La cancha ya tiene una reserva.")
        return
    reserva = Reserva(cancha.numero_cancha, cancha.deporte, cancha.precio, cancha.habilitada, numero_reserva, fecha)
    cancha.lista_reserva.append(reserva)
    print("Reserva creada exitosamente.")

# Suponiendo que `nueva_cancha` ya está definida y habilitada
numero_reserva = int(input("Dime el número de la reserva: "))
fecha_reserva = input("Dime para qué fecha quieres la reserva: ")
crear_reserva(nueva_cancha, numero_reserva, fecha_reserva)

def menu():
    while True:
        print("\nOpciones:")
        print("1. Crear reserva")
        print("2. Listar reservas de una cancha")
        print("3. Registrar pago del cliente")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            numero_reserva = int(input("Dime el número de la reserva: "))
            fecha_reserva = input("Dime para qué fecha quieres la reserva: ")
            crear_reserva(nueva_cancha, numero_reserva, fecha_reserva)
        elif opcion == "2":
            nueva_cancha.listar_reservas()  # Suponiendo que tienes un método 'listar_reservas' en la clase Cancha
        elif opcion == "3":
            # Suponiendo que 'cliente' es una instancia de la clase Cliente
            monto_pago = float(input("Ingrese el monto del pago: "))
            cliente.aumentar_saldo(monto_pago)  # Suponiendo que tienes un método 'aumentar_saldo' en la clase Cliente
            print("Pago registrado exitosamente.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, elige nuevamente.")

menu()
