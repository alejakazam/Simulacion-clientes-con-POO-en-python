import re
import logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    filename="errores.log",
    encoding="utf-8")
logger = logging.getLogger(__name__)
def pedir_opcion_int(mensaje, minimo, maximo):
    while True:
        try:
            opcion = int(input(mensaje))
            if minimo <= opcion <= maximo:
                return opcion
            else:
                logger.warning("valor ingresado fuera de rango")
                print("Opcion no válida, valor fuera de rango")             
        except ValueError:
            logger.warning("Opción no numérica ingresada")
            print("Opcion no válida, debe ser numérico")
class ClienteDuplicadoError(Exception):
    pass
class Validador:

    @staticmethod
    def rut(rut: str) -> bool:
        patron = r'^(\d{1,2}\.)?\d{3}\.\d{3}-[\dkK]$|^\d{7,8}-[\dkK]$'
        return bool(re.fullmatch(patron, rut))

    @staticmethod
    def email(email: str) -> str:
        patron = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
        if not re.fullmatch(patron, email):
            logger.error(f"Email inválido ingresado: {email}")
            raise ValueError("Email no válido")
        return email

    @staticmethod
    def telefono(telefono: str) -> bool:
        return telefono.isdigit() and len(telefono) >= 8