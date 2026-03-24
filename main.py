from modulos.cliente import *
from modulos.cliente_corporativo import *
from modulos.cliente_regular import *
from modulos.cliente_premium import *
from modulos.gestor_cliente import *
from modulos.validaciones import Validador, pedir_opcion_int, ClienteDuplicadoError

def menu():
    print(r"""
        ████████████████████████████████████
        █           Sistema GIC            █
        █          Menú Principal          █        
        ████████████████████████████████████

        [1] Agregar Cliente Persona Regular
        [2] Agregar Cliente Persona Premium
        [3] Agregar Cliente Corporativo
        [4] Listar Clientes
        [5] Eliminar Clientes  
        [6] ⏻ Salir

        ────────────────────────────────────
        """)

def solicitar_datos_persona():
    while True:
        try:
            identificador = int(input("ID: "))
            if identificador > 0:
                break
        except ValueError:
            print("ID inválido")
    while True:
        tarifa = input("Tarifa: ").strip()
        if tarifa:
            break
    while True:
        nombre = input("Nombre: ").strip()
        if nombre:
            break
    while True:
        rut = input("RUT: ").strip()
        if Validador.rut(rut):
            break
        print("RUT no válido")
    while True:
        try:
            email = Validador.email(input("Email: ").strip().lower())
            break
        except ValueError as e:
            print(e)
    while True:
        telefono = input("Teléfono: ").strip()
        if Validador.telefono(telefono):
            break
        print("Teléfono no válido")
    while True:
        direccion = input("Dirección: ").strip()
        if direccion:
            break
    return identificador, tarifa, nombre, rut, email, telefono, direccion
def solicita_datos_corporacion():
    while True:
        try:
            identificador = int(input("ID: "))
            if identificador > 0:
                break
        except ValueError:
            print("ID inválido")
    while True:
        tarifa = input("Tarifa: ").strip()
        if tarifa:
            break
    while True:
        razon = input("Razón Social: ").strip()
        if razon:
            break
    while True:
        rut = input("RUT: ").strip()
        if Validador.rut(rut):
            break
        print("RUT no válido")
    while True:
        try:
            email = Validador.email(input("Email: ").strip().lower())
            break
        except ValueError as e:
            print(e)
    while True:
        telefono = input("Teléfono: ").strip()
        if Validador.telefono(telefono):
            break
        print("Teléfono no válido")
    while True:
        direccion = input("Dirección: ").strip()
        if direccion:
            break
    return identificador, tarifa, razon, rut, email, telefono, direccion
def main():
    gestor = GestorCliente()
    gestor.importar_csv()
    while True:
        menu()
        opcion = pedir_opcion_int("Introduzca la opcion (1-6): ", 1, 6)

        match opcion:  #match para ahorrar ocupar elif 
            case 1:
                try:
                    instancia = Cliente_Regular(*solicitar_datos_persona())
                    gestor.agregar(instancia)
                    print("Cliente agregado correctamente")
                except ClienteDuplicadoError as e:
                    print(e)
                input("Presione enter para continuar")
            case 2:
                try:
                    instancia = Cliente_Premium(*solicitar_datos_persona())
                    gestor.agregar(instancia)
                    print("Cliente agregado correctamente")
                except ClienteDuplicadoError as e:
                    print(e)
                input("Presione enter para continuar")
            case 3:
                try:
                    instancia = Cliente_Corporativo(*solicita_datos_corporacion())
                    gestor.agregar(instancia)
                    print("Cliente agregado correctamente")
                except ClienteDuplicadoError as e:
                    print(e) 
                input("Presione enter para continuar")
            case 4:
                gestor.listar()
                input("Presione enter para continuar")
            case 5:
                try:
                    id_elim = int(input("Ingrese ID de cliente que desea eliminar: "))
                    eliminado = gestor.eliminar(id_elim)
                    if eliminado:
                        print("Éxito")
                except ValueError:
                    print("ID inválido, debe ser numérico")
                input("Presione enter para continuar")
            case 6:
                print("Saliendo - Gracias por usar el sistema")
                break





if __name__ == "__main__":
    main()
