import sys

print("------ Números enteros ------")
print(f"Tamaño de un entero es: {sys.getsizeof(0)} bytes")
numero = 10 ** 100
print(numero)

print("------ Números decimales ------")
print(f"Tamaño maximo de un decimale es: {sys.float_info.max} bytes")
print(f"Tamaño minimo de un decimale es: {sys.float_info.min} bytes")
print(1.25**100)

print("------ Valor booleano ------")
print(True)
print(False)
print(type(False))

print(int(True))
