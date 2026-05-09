from abc import ABC, abstractmethod
from excepciones import ErrorValidacion


# =========================
# CLASE ABSTRACTA SERVICIO
# =========================
class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ErrorValidacion("Nombre del servicio inválido")

        if not isinstance(precio_base, (int, float)) or precio_base <= 0:
            raise ErrorValidacion("Precio inválido")

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# =========================
# RESERVA DE SALA
# =========================
class ReservaSala(Servicio):

    def calcular_costo(self, horas=1):

        if horas <= 0:
            raise ErrorValidacion("Horas inválidas")

        return self.precio_base * horas

    def descripcion(self):
        return "Reserva de sala"


# =========================
# ALQUILER DE EQUIPOS
# =========================
class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias=1):

        if dias <= 0:
            raise ErrorValidacion("Días inválidos")

        return self.precio_base * dias

    def descripcion(self):
        return "Alquiler de equipos"


# =========================
# ASESORÍA
# =========================
class Asesoria(Servicio):

    def calcular_costo(self, horas=1):

        if horas <= 0:
            raise ErrorValidacion("Horas inválidas")

        return self.precio_base * horas * 1.2

    def descripcion(self):
        return "Asesoría especializada"
