import csv
from modulos.cliente import Cliente
from modulos.validaciones import *

class GestorCliente:
    def __init__(self):
        self.__clientes = []

    def agregar(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("Objeto inválido, no es un Cliente")

        for c in self.__clientes:
            if c.get_identificador() == cliente.get_identificador():
                raise ClienteDuplicadoError(
                    f"Ya existe un cliente con ID {cliente.get_identificador()}")

        self.__clientes.append(cliente)

    def listar(self):
        if self.__clientes:
            print(r"""
████████████████████████████████████
█              Lista de            █
█              Clientes            █        
████████████████████████████████████
""")
            for item in self.__clientes:
                print(item)
        else:
            print("No hay clientes")

    def eliminar(self, id_cliente):
        for i, item in enumerate(self.__clientes):
            if item.get_identificador() == int(id_cliente):
                print("Coincidencia de cliente encontrada:")
                print(item)

                confirmacion = input(
                    "¿Está seguro de querer eliminar este cliente? (si/no): "
                ).strip().lower()

                if confirmacion in ("si", "sí"):
                    self.__clientes.pop(i)
                    print("Cliente eliminado correctamente")
                    return True
                else:
                    print("Eliminación cancelada")
                    return False

        print("Cliente no encontrado")
        return False

    def importar_csv(self):
        with open("modulos/clientes.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                cliente = Cliente(int(fila["identificador"]),fila["tarifa"],fila["nombre"],fila["rut"],fila["email"],fila["telefono"],fila["direccion"],fila["descuento"])
                self.agregar(cliente)
