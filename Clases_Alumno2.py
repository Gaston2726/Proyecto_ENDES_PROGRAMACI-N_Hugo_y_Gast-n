class Cliente:
    lista_clientes = {}
    lista_morosos = []

    def __init__(self, nombre="", apellido1="", apellido2="", telefono="", identificador=""):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.telefono = telefono
        self.identificador = identificador

    def crear_cliente(self):
        self.nombre = input("Escribe tu nombre o el nombre del cliente: ")
        self.apellido1 = input("Escribe el primer apellido: ")
        self.apellido2 = input("Escribe el segundo apellido: ")
        self.telefono = input("Escribe el numero de telefono: ")
        self.identificador = input("Escribe el identificador: ")
        
        Cliente.lista_clientes[self.identificador] = {
            'nombre': self.nombre,
            'apellido1': self.apellido1,
            'apellido2': self.apellido2,
            'telefono': self.telefono,
            'identificador': self.identificador
        }
        print("El cliente se ha creado")

    def mostrar_clientes_morosos(self):
        if not Cliente.lista_morosos:
            print("No hay clientes morosos registrados")
        else:
            for identificador in Cliente.lista_morosos:
                cliente = Cliente.lista_clientes.get(identificador, {})
                if cliente:
                    print(f"Id: {identificador}, Nombre: {cliente['nombre']}, Apellidos: {cliente['apellido1']} {cliente['apellido2']}")

    def eliminar_cliente(self):
        identificador = input("Escriba el identificador del cliente: ")
        if identificador in Cliente.lista_clientes:
            del Cliente.lista_clientes[identificador]
            if identificador in Cliente.lista_morosos:
                Cliente.lista_morosos.remove(identificador)
            print("El cliente se ha retirado")
        else:
            print("El identificador no se ha encontrado")

    @staticmethod
    def agregar_cliente_centro():
        identificador = input("Escriba el identificador del cliente a agregar al centro: ")
        if identificador in Cliente.lista_clientes:
            Cliente.lista_morosos.append(identificador)
            print("El cliente ha sido agregado a la lista de morosos")
        else:
            print("El identificador no se ha encontrado")

def menu():
    print("Bienvenido a la gestión de clientes")
    print("1.- Crear cliente")
    print("2.- Mostrar clientes morosos")
    print("3.- Eliminar cliente")
    print("4.- Agregar cliente a la lista de morosos")
    print("5.- Salir")

    cliente = Cliente()
    while True:
        opcion = int(input("Escoge una opción: "))
        if opcion == 1:
            cliente.crear_cliente()
        elif opcion == 2:
            cliente.mostrar_clientes_morosos()
        elif opcion == 3:
            cliente.eliminar_cliente()
        elif opcion == 4:
            Cliente.agregar_cliente_centro()
        elif opcion == 5:
            print("Adiós")
            break
        else:
            print("Opción no válida, por favor elige otra vez.")