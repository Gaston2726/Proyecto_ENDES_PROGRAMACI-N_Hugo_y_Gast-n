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
                return
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
