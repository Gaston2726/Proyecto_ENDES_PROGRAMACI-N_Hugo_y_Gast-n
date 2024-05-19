#Clase Cancha y de mas.

lista_cancha=[]
class Cancha:
    def __init__(self, numero_cancha, deporte, precio, habilitada):
        self.numero_cancha = numero_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.lista_reserva = []
        self.lista_empleado = []
    def __str__(self):
        estado_habilitada = "Habilitada" if self.habilitada else "No habilitada"
        return f"Número de Cancha: {self.numero_cancha}\nDeporte: {self.deporte}\nPrecio: {self.precio}\nEstado: {estado_habilitada}\n"
def crear_cancha():
    numero_cancha=int(input("Dime el numero de la cancha: "))
    deporte=input("Dime el deporte que vas a realizar: ")
    precio=input("Dime el precio de la cancha: ")
    habilitada=input("Dime si esta habilitada dicendo si o no: ")
    if habilitada.lower() == "si":
        habilitada = True
    else:
        habilitada = False
    cancha = Cancha(numero_cancha, deporte, precio, habilitada)
    return cancha
def añadir_a_lista_cancha(cancha):
    lista_cancha.append(cancha)
    print("EN la lista de canchas hay: ",len(lista_cancha))

class Reserva(Cancha):
    def __init__(self, numero_cancha, deporte, precio, habilitada, numero_reserva, fecha):
        super().__init__(numero_cancha, deporte, precio, habilitada)
        self.numero_reserva=numero_cancha
        self.fecha=fecha
def crear_reserva(cancha):
    numero_reserva=int(input("Dime el numero de la reserva: "))
    fecha=input("Dime para que fecha quieres la reserva: ")
    reserva = Reserva(numero_reserva, fecha)
    cancha.lista_reserva.append(reserva)

nueva_cancha = crear_cancha()
print("Cancha habilitada:", nueva_cancha.habilitada)#dice si esta habilitada o no 
añadir_a_lista_cancha(nueva_cancha)
crear_reserva(nueva_cancha)






"""
class Reserva():
    def __init__(self, num_reserva, fecha, cliente, cancha):
        self.num_reserva=num_reserva
        self.fecha=fecha
        self.cliente=cliente
        self.cancha=cancha
    def __str__(self):
        return f"Reserva {self.num_reserva} - Fecha: {self.fecha}, Cliente: {self.cliente.nombre}, Cancha: {self.cancha.numero_cancha}"
def crear_reserva():
    reserva=Reserva
    num_reserva=int(input("Dime el numero de la reserva: "))
    fecha=input("Dime la fecha que quieres que sea la reserva: ")
"""
"""
class Centro():
    def __init__(self, nombre_centro,dir_centro ):
        self.nombre_centro=nombre_centro
        self.dir_centro=dir_centro
        self.canchas=[]
        self.clientes=[]

    def agregar_cancha(self, cancha):
        self.canchas.append(cancha)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

# Ejemplo de uso
if __name__ == "__main__":
    nueva_cancha = crear_cancha()
    print("Cancha habilitada:", nueva_cancha.habilitada)

    centro = Centro("Centro Deportivo XYZ", "Calle Principal 123")
    centro.agregar_cancha(nueva_cancha)
    print("Número de canchas en el centro:", len(centro.canchas))
"""
"""
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
    
    #hola hugo
class Centro():
    def __init__(self,nom_centr,dir_centro,)
"""
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