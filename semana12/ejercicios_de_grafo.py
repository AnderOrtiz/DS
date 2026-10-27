class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []

    def agregar_arista(self, origen, destino):
        self.agregar_arista(origen, destino)
        self.agregar_arista(origen)
        self.agregar_arista(destino)
        if destino not in self.adyacencia[origen]:
            self.adyacencia[origen].append(destino)
        
        if origen not in self.adyacencia[destino]:
            self.adyacencia[destino].append(origen)