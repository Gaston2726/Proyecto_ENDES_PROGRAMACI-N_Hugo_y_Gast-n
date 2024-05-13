#Clase Cancha y de mas.
class Cancha:
    def __init__(self, numero_cancha, deporte, precio, habilitada):
        self.numero_cancha = numero_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.lista_reserva = []
        self.lista_empleado = []
        self.lista_cancha = []

    def agre_reser(self, reserva):
        self.lista_reserva.append(reserva)

    @staticmethod
    def crear_cancha():
        cancha = Cancha(
            int(input("Dime el numero de la cancha: ")),
            input("Dime que deporte se practica en la cancha: "),
            int(input("Dime el precio de la cancha: ")),
            True  # Puedes cambiar esto si quieres
        )
        return cancha

    def agregar_lista(self, numero_cancha):
        if numero_cancha not in self.lista_cancha:
            self.lista_cancha.append(numero_cancha)
            for n in self.lista_cancha:
                print(n)
        else:
            print("Cancha ya existente")
    
class Centro():
    def __init__(self,nom_centr,dir_centro,)
"""
# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la clase Cancha
    cancha1 = Cancha.crear_cancha()

    # Agregar la cancha a la lista de canchas
    cancha1.agregar_lista(cancha1.numero_cancha)

class Reserva(Cancha):
    def __init__(self, numero_cancha, deporte, precio, habilitada):
        super().__init__(numero_cancha, deporte, precio, habilitada)
     

def menu():
    lista_cancha=[]
    print("1 -.crear cancha")
    print("2 .-Agregar cancha")
    print("3 .- lista de canchas")
    print("4 .-eliminar una cancha del centro")
    print("5 .- Salir del menu")
    elecion=int(input("Dime la eleccion que quieres coger: "))
    while elecion!=5:
        elecion=int(input("Dime la eleccion que quieres coger: "))
        if elecion == 1:

            
        if elecion ==2 :

        if elecion==3:


menu()
"""