coordenadas = (13.7, -89.2)
# Acceder

print(coordenadas[0])  # 13.7

# Contar y encontrar índice

print(coordenadas.count(13.7))

print(coordenadas.index(-89.2))

frutas = ("manzana", "banana", "uva", "manzana")


print(frutas)


# Acceder a la segunda fruta a comprar

print(frutas[1])  # banana

# recibe un mensaje donde te consultan cuantas frutas traerás

print(len(frutas))

# Crear una tupla

empresa = (
    "Manguito",
    "San Miguel",
    ("Helados", "mangoneada"),
    1981
)

print(empresa[2])
print(empresa[2][1])