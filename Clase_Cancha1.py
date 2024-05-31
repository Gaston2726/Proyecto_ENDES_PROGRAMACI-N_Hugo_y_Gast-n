class Cancha:
    def __init__(self, numero_cancha, deporte, precio, habilitada):
        self.numero_cancha = numero_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.lista_reserva = []
        self.lista_empleado = []

    def __str__(self):
        return f"Cancha creada: Número {self.numero_cancha}, Deporte: {self.deporte}, Precio: {self.precio}, Habilitada: {self.habilitada}"
    
    def agregar_cancha(self, lista_cancha):
        """
        Agrega una cancha a la lista de canchas.
        """
        for cancha in lista_cancha:
            if cancha.numero_cancha == self.numero_cancha:
                print(f"La cancha {self.numero_cancha} ya está en la lista.")
                return
        lista_cancha.append(self)
        print(f"La cancha {self.numero_cancha} ha sido agregada.")

    @staticmethod
    def lista_canchas_deporte(lista_canchas):
        """
        Lista las canchas según el deporte especificado.
        """
        deporte = input("Dime el deporte para listar las canchas: ")
        canchas_deporte = [cancha for cancha in lista_canchas if cancha.deporte == deporte]
        if canchas_deporte:
            for cancha in canchas_deporte:
                print(f"Número de Cancha: {cancha.numero_cancha}, Deporte: {cancha.deporte}, Precio: {cancha.precio}, Habilitada: {cancha.habilitada}")
        else:
            print(f"No hay canchas disponibles para el deporte: {deporte}")

    @staticmethod
    def eliminar_cancha_de_centro(lista_canchas):
        """
        Elimina una cancha de la lista de canchas del centro.
        """
        numero_cancha = int(input("Dime el número de la cancha que quieres eliminar: "))
        for cancha in lista_canchas:
            if cancha.numero_cancha == numero_cancha:
                if cancha.lista_reserva:
                    print(f"No se puede eliminar la cancha {numero_cancha}, tiene reservas.")
                else:
                    lista_canchas.remove(cancha)
                    print(f"Cancha {numero_cancha} eliminada de la lista.")
                return
        print("La cancha no está registrada.")


def crear_cancha():
    """
    Crea una nueva instancia de Cancha.
    """
    numero_cancha = int(input("Dime el número de la cancha: "))
    deporte = input("Dime el deporte que se va a realizar: ")
    precio = float(input("Dime el precio de la cancha: "))
    habilitada = input("Dime si está habilitada (sí o no): ").strip().lower() == 'si'
    cancha=Cancha(numero_cancha, deporte, precio, habilitada)
    print("La cancha creada es:", cancha)

def menu_cancha():
    """
    Muestra un menú para la gestión de las canchas.
    """
    lista_canchas = []
    print("\nMenú de Opciones")
    print("1. Crear una cancha")
    print("2. Agregar una cancha a la lista del centro")
    print("3. Listar las canchas totales según un tipo de deporte")
    print("4. Quitar una cancha de la lista del centro")
    print("5. Salir")
    opcion =int( input("Elige una opción: "))

    while opcion!=5:
        if opcion == 1:
            nueva_cancha = crear_cancha()
            lista_canchas.append(nueva_cancha)
        elif opcion == 2:
            if lista_canchas:
                nueva_cancha.agregar_cancha(lista_canchas)
            else:
                print("Primero debes crear una cancha.")
        elif opcion == 3:
            Cancha.lista_canchas_deporte(lista_canchas)
        elif opcion == 4:
            Cancha.eliminar_cancha_de_centro(lista_canchas)
        elif opcion == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor elige otra vez.")
        opcion = int(input("Elige una opción: "))

menu_cancha()

