class Reserva():
    def __init__(self,numero_reserva,fecha):
        self.numero_reserva=numero_reserva
        self.fecha=fecha
    

    def comprobar_cliente(self):
        saldo = int(input("Dime tu saldo: "))
        if saldo <= -2000:
            print("No puedes reservar.")
            return False
        else:
            print("Puedes reservar.")
            return True
        
    def listar_reservas(self):
        

def crear_reserva():
    numero_reserva=int(input("Dime el numero de reserva: "))
    fecha=input("Dime una fecha de reserva: ")
    reserva=Reserva(numero_reserva,fecha)
    if not cancha.habilitada:
        print("La cancha no está habilitada para reservas.")
        return
    if cancha.lista_reserva:
        print("La cancha ya tiene una reserva.")
        return
    reserva = Reserva(cancha.numero_cancha, cancha.deporte, cancha.precio, cancha.habilitada, numero_reserva, fecha)
    cancha.lista_reserva.append(reserva)
    print("Reserva creada exitosamente.")

