from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from sistema import Sistema
from excepciones import ErrorValidacion


# =========================
# PRUEBAS DEL SISTEMA
# =========================
def pruebas():

    sistema = Sistema()

    try:

        # =========================
        # CLIENTE VÁLIDO
        # =========================
        cliente1 = Cliente(1, "Juan")
        sistema.agregar_cliente(cliente1)

        # =========================
        # CLIENTE INVÁLIDO
        # =========================
        try:
            Cliente(2, "")
        except ErrorValidacion as e:
            print(e)

        # =========================
        # SERVICIOS
        # =========================
        servicio1 = ReservaSala("Sala VIP", 100)
        servicio2 = AlquilerEquipo("Proyector", 50)
        servicio3 = Asesoria("Consultoría", 200)

        # =========================
        # RESERVAS VÁLIDAS
        # =========================
        sistema.crear_reserva(cliente1, servicio1)
        sistema.crear_reserva(cliente1, servicio2)
        sistema.crear_reserva(cliente1, servicio3)

        # =========================
        # RESERVAS INVÁLIDAS
        # =========================
        sistema.crear_reserva(None, servicio1)
        sistema.crear_reserva(cliente1, None)

        # =========================
        # MOSTRAR RESERVAS
        # =========================
        sistema.mostrar_reservas()

    except Exception as e:
        print("Error general:", e)


# =========================
# EJECUCIÓN PRINCIPAL
# =========================
if __name__ == "__main__":
    pruebas()
