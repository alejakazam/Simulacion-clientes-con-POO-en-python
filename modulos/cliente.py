class Cliente:
    def __init__(self,identificador,tarifa, nombre,rut, email,telefono, direccion, descuento):
        self._nombre=nombre
        self.__identificador= identificador
        self._rut = rut
        self._tarifa=tarifa
        self._email=email
        self._telefono=telefono
        self._direccion=direccion
        self._descuento= descuento

    def get_identificador(self):
        return self.__identificador
    
    def mostrar_info(self):
        print(self)  

    def __str__(self):
        return f"""
████████████████████████████████████
█             Sistema GIC          █
█              Clientes            █
████████████████████████████████████
[Nombre]: {self._nombre}
[ID]: {self.__identificador}
[Tarifa]: {self._tarifa}
[RUT]: {self._rut}
[E-mail]: {self._email}
[Teléfono]: +56 {self._telefono}
[Domicilio]: {self._direccion}
[Descuento]: {self._descuento} %
"""