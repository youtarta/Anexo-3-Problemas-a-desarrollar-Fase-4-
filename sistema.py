from reserva import Reserva
from excepciones import ErrorSistema
from datetime import datetime


# =========================
# REGISTRO DE LOGS
# =========================
def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")


# =========================
# SISTEMA
# =========================
class Sistema:

    def __init__(self):

        self.clientes = []
        self.reservas = []

    # =========================
    # AGREGAR CLIENTE
    # =========================
    def agregar_cliente(self, cliente):

        self.clientes.append(cliente)

    # =========================
    # CREAR RESERVA
    # =========================
    def crear_reserva(self, cliente, servicio):

        try:
            reserva = Reserva(cliente, servicio)

            reserva.confirmar()

            self.reservas.append(reserva)

        except ErrorSistema as e:
            registrar_log(e)

    # =========================
    # MOSTRAR RESERVAS
    # =========================
    def mostrar_reservas(self):

        if not self.reservas:
            print("No hay reservas registradas")
            return

        for reserva in self.reservas:
            print(reserva.mostrar())
