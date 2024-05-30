class Cancha:
    def __init__(self, numero_cancha, deporte, precio, habilitada):
        self.numero_cancha = numero_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.lista_reserva = []
        self.lista_empleado = []
"""
    def __str__(self):
        estado_habilitada = "Habilitada" if self.habilitada else "No habilitada"
        return (f"Número de Cancha: {self.numero_cancha}\nDeporte: {self.deporte}\n"
                f"Precio: {self.precio}\nEstado: {estado_habilitada}\n"
                f"Reservas pendientes: {len(self.lista_reserva)}")

    def agregar_cancha(self, lista_cancha):
        for c in lista_cancha:
            if c.numero_cancha == self.numero_cancha:
                print(f"La cancha número {self.numero_cancha} ya está registrada.")
                return
        lista_cancha.append(self)
        print(f"Cancha número {self.numero_cancha} agregada.")

    @staticmethod
    def listar_canchas_por_deporte(lista_cancha, deporte):
        canchas_deporte = [cancha for cancha in lista_cancha if cancha.deporte == deporte]
        if canchas_deporte:
            for cancha in canchas_deporte:
                print(cancha)
        else:
            print(f"No hay canchas disponibles para el deporte {deporte}.")

    @staticmethod
    def quitar_cancha(lista_cancha, numero_cancha):
        for cancha in lista_cancha:
            if cancha.numero_cancha == numero_cancha:
                if cancha.lista_reserva:
                    print(f"No se puede quitar la cancha número {numero_cancha} porque tiene reservas pendientes.")
                    return
                lista_cancha.remove(cancha)
                print(f"Cancha número {numero_cancha} quitada.")
                return
        print(f"La cancha número {numero_cancha} no está registrada.")

def crear_cancha():
    numero_cancha = int(input("Dime el numero de la cancha: "))
    deporte = input("Dime el deporte que vas a realizar: ")
    precio = float(input("Dime el precio de la cancha: "))
    habilitada = input("Dime si esta habilitada diciendo si o no: ").strip().lower() == 'si'
    cancha = Cancha(numero_cancha, deporte, precio, habilitada)
    return cancha

def menu_canchas():
    lista_cancha = []
    while True:
        print("\nOpciones:")
        print("1. Crear cancha")
        print("2. Listar canchas por deporte")
        print("3. Quitar cancha")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            cancha = crear_cancha()
            cancha.agregar_cancha(lista_cancha)
        elif opcion == "2":
            deporte = input("Dime el deporte: ")
            Cancha.listar_canchas_por_deporte(lista_cancha, deporte)
        elif opcion == "3":
            numero_cancha = int(input("Dime el número de la cancha a quitar: "))
            Cancha.quitar_cancha(lista_cancha, numero_cancha)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, elige nuevamente.")

# Iniciar el menú
menu_canchas()
"""
