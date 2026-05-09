from abc import ABC, abstractmethod
from excepciones import ErrorValidacion


# =========================
# CLASE ABSTRACTA
# =========================
class Entidad(ABC):

    def __init__(self, id):
        self._id = id

    @abstractmethod
    def mostrar(self):
        pass


# =========================
# CLIENTE
# =========================
class Cliente(Entidad):

    def __init__(self, id, nombre):
        super().__init__(id)
        self.nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not isinstance(valor, str) or valor.strip() == "":
            raise ErrorValidacion("Nombre inválido")

        self._nombre = valor

    def mostrar(self):
        return f"Cliente: {self._nombre}"
