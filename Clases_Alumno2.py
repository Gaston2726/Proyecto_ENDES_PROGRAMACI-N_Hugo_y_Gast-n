class Cliente():
    def __init__(self, nombre, apellido1, apellido2, telefono, identificador):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.telefono = telefono
        self.identificador = identificador

    def crear_cliente(self, lista_clientes):
        self.nombre = input("Escribe tu nombre o el nombre del cliente: ")
        self.apellido1 = input("Escribe el primer apellido: ")
        self.apellido2 = input("Escribe el segundo apellido: ")
        self.telefono = input("Escribe el numero de telefono: ")
        self.identificador = input("Escribe el identificador: ")
        
        lista_clientes[self.identificador] = {'nombre':self.nombre, 'apellido1':self.apellido1, 'apellido2':self.apellido2, 'Id':self.identificador}
        print("El cliente se ha creado")

    def mostrar_cliente(self, lista_clientes):
        if not lista_clientes:
            print("No hay clientes registrados")
        else:
            for self.identificador in lista_clientes:
                print(f"Id: {self.identificador}, Nombre: {self.nombre}, Apellidos: {self.apellido1, self.apellido2}")

    def eliminar_cliente(self, lista_clientes):
        self.identificador = input("Escriba el identificador del cliente: ")
        if self.identificador in lista_clientes:
            del lista_clientes[self.identificador]
            print("El cliente se ha retirado")
        else:
            print("El identificador no se ha encontrado")