class Cancha:
    def __init__(self, numero_cancha, deporte, precio, habilitada):
        self.numero_cancha = numero_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.lista_reserva = []
        self.lista_empleado = []
    
    def agregar_cancha(self,lista_cancha):
        """ 
        Aqui se supone que se agregan los datos de cancha en la lista de centro
        """
        for cancha in lista_cancha:
            if cancha.numero_cancha==self.numero_cancha:
                print(f"La cancha que quieres introducir {self.numero_cancha},esta ya dentro de esta lista")
            lista_cancha.append(self)
            print(f"La cancha con el numero{self.numero_cancha}, esta agregada")
    
    def lista_canchas_deporte(listas_cancha,deporte):
        """ 
        Aqui listo las canchas según el deporte que sea
        """
        list_depor__cancha=[cancha for cancha in listas_cancha if cancha.deporte == deporte]#crea una lista segun deporte
        if list_depor__cancha:
            for cancha in list_depor__cancha:
                print(cancha)
        else:
            print("No hay canchas disponibles para el deporte:", deporte)
    
    def eliminar_cancha_de_centro(lista_cancha,numero_cancha):
        """ 
        Se elimina la cancha de la lista de centro de cancha, pero hay una condicion y es que si tiene reserva no 
        se elimina, pero si no tiene se puede eliminar.
        """
        for cancha in lista_cancha:
            if cancha.numero_cancha == numero_cancha:
                if cancha.lista_reserva:
                    print("No se puede quitar la cancha, ya tiene reserva el :", numero_cancha)
                else:
                    lista_cancha.remove(cancha)
                    print("Cancha eliminada de la lista", numero_cancha)
        else:
            print("No esta registrada")


def crear_cancha():
    numero_cancha = int(input("Dime el numero de la cancha: "))
    deporte = input("Dime el deporte que vas a realizar: ")
    precio = float(input("Dime el precio de la cancha: "))
    habilitada = input("Dime si esta habilitada diciendo si o no: ").strip().lower() == 'si'
    cancha = Cancha(numero_cancha, deporte, precio, habilitada)
    return cancha

def menu():

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
            print(f"Cancha creada: {nueva_cancha.numero_cancha}, {nueva_cancha.deporte}, Precio: {nueva_cancha.precio}, Habilitada: {nueva_cancha.habilitada}")

        elif opcion == '2':
            if 'nueva_cancha' in locals():
                nueva_cancha.agregar_cancha(lista_canchas)
            else:
                print("Primero debes crear una cancha.")

        elif opcion == '3':
            deporte = input("Dime el deporte para listar las canchas: ")
            Cancha.lista_canchas_deporte(lista_canchas, deporte)

        elif opcion == '4':
            numero_cancha = int(input("Dime el número de la cancha que quieres eliminar: "))
            Cancha.eliminar_cancha_de_centro(lista_canchas, numero_cancha)

        elif opcion == '5':
            print("Saliendo del programa.")
            break
    else:
        print("Sales del menu cancha")


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