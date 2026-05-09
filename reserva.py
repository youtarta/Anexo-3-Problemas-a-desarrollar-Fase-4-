from cliente import Cliente
from servicio import Servicio
from excepciones import ErrorReserva


# =========================
# RESERVA
# =========================
class Reserva:

    def __init__(self, cliente, servicio):

        if not isinstance(cliente, Cliente):
            raise ErrorReserva("Cliente no válido")

        if not isinstance(servicio, Servicio):
            raise ErrorReserva("Servicio no válido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def mostrar(self):

        return (
            f"{self.cliente.nombre} - "
            f"{self.servicio.descripcion()} - "
            f"{self.estado}"
        )
