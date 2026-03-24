from modulos.cliente import Cliente

class Cliente_Premium(Cliente):
    def __init__(self, identificador, tarifa, nombre, rut, email, telefono, direccion):
        super().__init__(identificador, tarifa, nombre, rut, email, telefono, direccion, descuento=0.05)

    def beneficio_exclusivo(self):
        print("Descuento permanente del 5% en el servicio.\n""Beneficio adicional: 50% de descuento en la tercera entrada en Cine Hoyts.")
