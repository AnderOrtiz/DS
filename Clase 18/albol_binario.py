class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)
n4 = Nodo(4)
n5 = Nodo(5)
n6 = Nodo(6)
n7 = Nodo(7)
n8 = Nodo(8)
n9 = Nodo(9)
n10 = Nodo(10)

n1.izquierda = n2
n1.derecha = n3

n2.izquierda = n4
n2.derecha = n5

n5.derecha = n8

n3.izquierda = n6
n3.derecha = n7

n7.izquierda = n9
n7.derecha = n10

raiz = n1


def recorrer_preorden(nodo):
    if nodo is None:
        return

    print(nodo.valor, end=" ")

    recorrer_preorden(nodo.izquierda)
    recorrer_preorden(nodo.derecha)


def contar_nodos(nodo):
    if nodo is None:
        return 0
    return (
        1
        + contar_nodos(nodo.izquierda)
        + contar_nodos(nodo.derecha)
    )


def altura(nodo):
    if nodo is None:
        return 0
    altura_izq = altura(nodo.izquierda)
    altura_der = altura(nodo.derecha)

    return 1 + max(altura_izq, altura_der)


print(" Información del árbol ")

print("\n Recorrido del árbol: ")
recorrer_preorden(raiz)
print()

total_nodos = contar_nodos(raiz)
print("\n Cantidad total de nodos: ", total_nodos)

altura_arbol = altura(raiz)
print("Altura del árbol: ", altura_arbol)