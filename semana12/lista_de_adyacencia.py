grafo = [
    "A",
    "B",
    "C",
    "D",
]

aristas = [
    ("A",  "B"),
    ("A",  "C"),
    ("B",  "C"),
    ("B",  "D")
    ("C",  "D")
]

for origen, destino in aristas:
    grafo[origen].append(destino)
    grafo[destino].append(origen)

for vertice, vecinos in grafo.items():
    print(vertice, ":" , vecinos)