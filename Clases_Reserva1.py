class Reserva():
    def __init__(self, numero_cancha, deporte, precio, habilitada, numero_reserva, fecha):
        super().__init__(numero_cancha, deporte, precio, habilitada)
        self.numero_reserva=numero_cancha
        self.fecha=fecha
def crear_reserva(cancha):
    numero_reserva=int(input("Dime el numero de la reserva: "))
    fecha=input("Dime para que fecha quieres la reserva: ")
    reserva = Reserva(numero_reserva, fecha)
    cancha.lista_reserva.append(reserva)

def comprobar_cliente(cliente):
    saldo=int(input("Dime tu saldo: "))
    if saldo <= -2000:
        print("No puedes reservar: ")
    else:
        print("Si puedes reservar")

crear_reserva(nueva_cancha)