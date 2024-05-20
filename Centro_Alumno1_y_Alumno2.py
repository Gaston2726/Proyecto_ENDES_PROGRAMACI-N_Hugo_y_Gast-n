class Centro():
    def __init__(self, nombre_centro, direccion):
        self.nombre_centro=nombre_centro
        self.direccion=direccion
        lista_cancha = []
        lista_clientes = []
    
    def menu():
        centro = Centro
        centro.nombre_centro = input("Dime el nombre del centro: ")
        centro.direccion = input("Dime la direccion del centro: ")
        print("Elige una de las opciones siguientes:\n1 .-Gestión de canchas\n2 .-Gestión de cliente\n3 .-Gestión de reserva\n 4 .-Gestión de empleado\n5 .-Salir del programa ")
        op1_menu = int(input("Dime que opcion eliges del menu: "))
        while op1_menu != 5:
            if op1_menu == 1:
                pass
            elif op1_menu == 2:
                pass
            elif op1_menu == 3:
                pass
            elif op1_menu == 4:
                pass
            elif op1_menu == 5:
                print("Se cierra el programa")
                break
Centro.menu()