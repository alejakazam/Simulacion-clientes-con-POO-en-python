from modulos.cliente import Cliente
import os
print(os.getcwd())
class Cliente_Corporativo(Cliente):
    def __init__(self, identificador, tarifa, razon_social, rut, email, telefono, direccion):
        super().__init__(identificador,tarifa,razon_social,rut,email,telefono,direccion,descuento=0.10)

    def __str__(self):
        return f"""
████████████████████████████████████
█             Sistema GIC          █
█          Cliente Corporativo     █
████████████████████████████████████
[Razón Social]: {self._nombre}
[ID]: {self.get_identificador()}
[Tarifa]: {self._tarifa}
[RUT]: {self._rut}
[E-mail]: {self._email}
[Teléfono]: +56 {self._telefono}
[Domicilio]: {self._direccion}
[Descuento]: {self._descuento * 100:.0f} %
"""


    def beneficio_exclusivo(self):
        print("Descuento permanente del 10% en el servicio.\n""Beneficio adicional: 15% de descuento los martes en Farmacias Zahúnada.")