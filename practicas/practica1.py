class Email:
    def __init__(self, direccion):
        # el correo tiene que tener @ y .
        if "@" not in direccion or "." not in direccion:
            raise ValueError("Dirección de correo inválida")
        self.direccion = direccion


class Edad:
    def __init__(self, valor):
        # la edad no puede ser menor a 0 o mayor a 120
        if not isinstance(valor, int) or valor < 0 or valor > 120:
            raise ValueError("Edad fuera del rango permitido (0-120)")
        self.valor = valor


class Nota:
    def __init__(self, calificacion):
        # la calificación tiene que ser entre 0 y 10.
        if not (0.0 <= calificacion <= 10.0):
            raise ValueError("La nota debe estar entre 0.0 y 10.0")
        self.calificacion = calificacion


class Contraseña:
    def __init__(self, contraseña):
        # La contraseña debe tener al menos 8 caracteres,
        # una letra mayúscula y un número.
        if len(contraseña) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")

        if not any(caracter.isupper() for caracter in contraseña):
            raise ValueError(
                "La contraseña debe contener al menos una mayúscula")

        if not any(caracter.isdigit() for caracter in contraseña):
            raise ValueError("La contraseña debe contener al menos un número")

        self.contraseña = contraseña


class Telefono:
    def __init__(self, numero):
        # El teléfono debe contener exactamente 8 dígitos.
        if not numero.isdigit() or len(numero) != 8:
            raise ValueError("El teléfono debe contener exactamente 8 dígitos")

        self.numero = numero


try:
    e = Email("usuario@dominio.com")
    ed = Edad(20)
    n = Nota(8.5)
    c = Contraseña("Password123")
    t = Telefono("71234567")

    print("Objetos creados exitosamente")

except ValueError as err:
    print("Error:", err)

try:
    # La contraseña no tiene una letra mayúscula ni un número.
    c_invalido = Contraseña("password")
except ValueError as err:
    print("Capturado:", err)

try:
    # El teléfono tiene menos de 8 dígitos.
    t_invalido = Telefono("123456")
except ValueError as err:
    print("Capturado:", err)

try:
    # El correo no contiene el símbolo @.
    e_invalido = Email("correo_sin_arroba.com")
except ValueError as err:
    print("Capturado:", err)

try:
    # La edad es menor que 0.
    ed_invalido = Edad(-20)
except ValueError as err:
    print("Capturado:", err)

try:
    # La calificación es mayor que 10.
    n_invalido = Nota(11)
except ValueError as err:
    print("Capturado:", err)
