from modulos.cliente import Cliente

class Cliente_Regular(Cliente):
    def __init__(self, identificador, tarifa, nombre, rut, email, telefono, direccion):
        super().__init__(identificador,tarifa,nombre,rut, email, telefono, direccion, descuento=0)

    def beneficio_exclusivo(self):
        print("Actualmente no dispone de beneficios")