class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


raiz = Nodo("Producto")

raiz.izquierda = Nodo("Tecnología")
raiz.derecha = Nodo("Hogar")


raiz.izquierda.izquierda = Nodo("Laptos")
raiz.izquierda.derecha = Nodo("Celulares")

raiz.derecha.izquierda = Nodo("Cocina")
raiz.derecha.derecha = Nodo("Muebles")

def es_hoja(nodo):
    return nodo.izquierda == None and nodo.derecha == None


print(f"Laptop es hoja: {es_hoja(raiz.izquierda.izquierda)}")
print(f"Tecnología es hoja: {es_hoja(raiz.izquierda)}")