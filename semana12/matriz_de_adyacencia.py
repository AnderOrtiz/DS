vertices = ["A", "B", "C", "D"]

matriz = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

aristas = [
    ("A",  "B"),
    ("A",  "C"),
    ("B",  "C"),
    ("B",  "D"),
    ("C",  "D"),
]


for origen, destino in aristas:
    i = vertices.index(origen)
    j = vertices.index(destino)
    matriz[i][j] = 1
    matriz[j][i ] = 1

print(" ", *vertices)
for i, fila in enumerate(matriz):
    print(vertices[1], fila)