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
def agregar_cancha(cancha):
    for c in lista_cancha:
        if c.numero_cancha == cancha.numero_cancha:
            print(f"La cancha número {cancha.numero_cancha} ya está registrada.")
            return
    lista_cancha.append(cancha)
    print(f"Cancha número {cancha.numero_cancha} agregada.")

def listar_canchas_por_deporte(deporte):
    canchas_deporte = [cancha for cancha in lista_cancha if cancha.deporte == deporte]
    if canchas_deporte:
        for cancha in canchas_deporte:
            print(cancha)
    else:



nueva_cancha = crear_cancha()
print("Cancha habilitada:", nueva_cancha.habilitada)#dice si esta habilitada o no 
añadir_a_lista_cancha(nueva_cancha)



class Centro():
    def __init__(self,nombre_centro,direccion  ):
        self.nombre_centro=nombre_centro
        self.direccion=direccion
        lista_cancha1=[]
        lista_clientes=[]
"""
def menu():
    centro=Centro
    centro.nombre_centro=input("Dime el nombre del centro: ")
    centro.direccion=input("Dime la direccion del centro: ")
    print("Elige una de las opciones siguientes:\n1 .-Gestión de canchas\n2 .-Gestión de cliente\n3 .-Gestión de reserva\n 4 .-Gestión de empleado\n5 .-Salir del programa ")
    op1_menu=int(input("Dime que opcion eliges del menu: "))
    while op1_menu!= 5:
        if op1_menu==1:
            print("1 .-Crear cancha\n2 .-Agregar cancha\n3 .-Listar canchas según el tipo de deporte\n4 .-Quitar cancha de lista centro")
            op2_menu=int(input("Dime que opcione eliges del submenu canchas: "))
            if op2_menu==1:
                crear_cancha()
            elif op2_menu==2:
                añadir_a_lista_cancha()
            elif op2_menu==3:
                pass
            elif op2_menu==4:
                pass
        elif op1_menu==2:
            pass
        elif op1_menu==3:
            print("1 .-Crear reserva\n2 .-Listar reserva actuales de cancha\n3 .-Listar reservas de un cliente\n4 .-Mostrar saldo de un cliente")
            op4_menu=int(input("Dime que opcion eliges del submenu reservas: "))
            if op2_menu==1:
                crear_reserva()
            elif op2_menu==2:
                comprobar_cliente()
            elif op2_menu==3:
                pass
            elif op2_menu==4:
                pass           
        elif op1_menu==4:
            pass
        elif op1_menu==5:
            print("Se cierra el programa")
            break

#ac
"""
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