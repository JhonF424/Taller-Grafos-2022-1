from classes.arista import *
from classes.vertice import *


class grafo:
    def __init__(self):
        self.listaVertices = []
        self.listaAristas = []

    def ingresarVertice(self, dato):
        if not self.verificarExisteV(dato):
            self.listaVertices.append(vertice(dato))

    def verificarExisteV(self, dato):
        for i in self.listaVertices:
            if dato == i.getDato():
                return True
        return False

    def mostrarVertices(self):
        for i in self.listaVertices:
            print(i.getDato())

    def ingresarAristas(self, origen, destino, peso):
        if not self.verificarListaA(origen, destino):
            if self.verificarExisteV(origen) and self.verificarExisteV(destino):
                self.listaAristas.append(arista(origen, destino, peso))
                self.obtenerVertice(origen).getListaAdyacentes().append(destino)

    def obtenerVertice(self, dato):
        for i in self.listaVertices:
            if dato == i.getDato():
                return i

    def verificarListaA(self, origen, destino):
        for i in self.listaAristas:
            if origen == i.getOrigen() and destino == i.getDestino():
                return True
        return False

    def mostrarAristas(self):
        for i in self.listaAristas:
            print(f"{i.getOrigen()} - {i.getPeso()} - {i.getDestino()}")

    def mostrarAdyacencias(self):
        for i in self.listaVertices:
            print(f"Vertice: {i.getDato()} - Adyacencias: {i.getListaAdyacentes()}")

    # TODO: CREAR UN MÉTODO QUE ME MUESTRE POZOS.
    def mostrarPozos(self):
        for i in self.listaVertices:
            if len(i.getListaAdyacentes()) == 0:
                print(i.getDato())

    # TODO: CREAR UN MÉTODO QUE DETERMINE SI UN VÉRTICE ES FUENTE.
    def verificarFuente(self, vertice):
        vertice = self.obtenerVertice(vertice)
        if len(vertice.getListaAdyacentes()) != 0:
            for i in self.listaAristas:
                if i.getDestino() == vertice.getDato():
                    return False
            return True

    def ordenarAristas(self):
        listaOrdenada = []
        for p in self.listaAristas:
            listaOrdenada.append(p.getPeso())

        long = len(listaOrdenada)

        for i in range(long):
            for current in range(long - 1):
                next = current + 1
                if listaOrdenada[current] > listaOrdenada[next]:
                    listaOrdenada[next], listaOrdenada[current] = (
                        listaOrdenada[current],
                        listaOrdenada[next],
                    )

        print("Lista de aristas ordenadas de menor a mayor: ", listaOrdenada)

    def obtenerGrado(self):
        listNodos = []
        for n in self.listaVertices:
            grado = 0
            listNodos.append(n.getDato())
            for a in self.listaAristas:
                if n.getDato() == a.getDestino() or n.getDato() == a.getOrigen():
                    grado = grado + 1

            print("Grado del nodo", n.getDato(), ":", grado)

    def mayorGrado(self):
        self.obtenerGrado()