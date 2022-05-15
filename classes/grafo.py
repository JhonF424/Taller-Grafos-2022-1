from collections import deque
from copy import copy
from classes.arista import *
from classes.vertice import *


class grafo:
    def __init__(self):
        self.listaVertices = []
        self.listaAristas = []
        self.VisistadosCp = []
        self.VisistadosCa = []

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

    def fuentes(self):
        listX = []

        for v in self.listaVertices:
            for a in self.listaAristas:
                if v.getDato() == a.getDestino():
                    print(v.getDato(), "no es")
                    # PENDIENTE DE REVISAR ESTE EJERCICIO
                else:
                    listX.append(v.getDato())

        print(listX)

    def promPesos(self):
        cant = 0
        total = 0

        for p in self.listaAristas:
            cant = cant + 1
            total = total + p.getPeso()

        prom = total / cant

        print("Peso promedio de todas las aristas del grafo: ", prom)

    def mayorPeso(self):
        pesos = []
        for p in self.listaAristas:
            pesos.append(p.getPeso())
        mayor = max(pesos)
        # Revisar:  Se hace de esta forma para poder buscar la arista como objeto,
        #           si se emplea un bucle con posiciones de la lista, solo estaríamos
        #           iterando sobre una lista de números.
        for b in self.listaAristas:
            if mayor == b.getPeso():
                print("La arista con mayor peso es: ")
                print(f"{b.getOrigen()} - {b.getPeso()} - {b.getDestino()}")

    def menorPeso(self):
        pesos = []
        for p in self.listaAristas:
            pesos.append(p.getPeso())
        mayor = min(pesos)
        # Revisar:  Se hace de esta forma para poder buscar la arista como objeto,
        #           si se emplea un bucle con posiciones de la lista, solo estaríamos
        #           iterando sobre una lista de números.
        for b in self.listaAristas:
            if mayor == b.getPeso():
                print("La arista con menor peso es: ")
                print(f"{b.getOrigen()} - {b.getPeso()} - {b.getDestino()}")

    # -------------------

    def RecorridoProfundidad(self, dato):  # dato es en que vertice empieza el recorrido
        if dato in self.VisistadosCp:
            return
        else:
            Vertice = self.obtenerOrigen(dato)
            if Vertice is not None:
                self.VisistadosCp.append(Vertice.getDato())
                for dato in Vertice.getListaAdyacentes():
                    self.RecorridoProfundidad(dato)

    def getVisitadosp(self):
        return self.VisistadosCp

    def getVisitadosca(self):
        return self.VisistadosCa

    def obtenerOrigen(self, v):
        for n in self.listaVertices:
            if n == v:
                return n

    def Amplitud(self, origen):
        VisitadosA = []
        Cola = deque()
        Vertice = self.obtenerOrigen(origen)
        if Vertice is not None:
            VisitadosA.append(origen)
            Cola.append(Vertice)
            while Cola:
                elemento = Cola.popleft()
                for Adyacencia in elemento.getListaAdyacentes():
                    if Adyacencia not in VisitadosA:
                        Vertice = self.obtenerOrigen(Adyacencia)
                        VisitadosA.append(Adyacencia)
                        Cola.append(Vertice)
        return VisitadosA

    # Algoritmo de PRIM

    def Ordenar(self, Aristas):
        for i in range(len(Aristas)):
            for j in range(len(Aristas)):
                if Aristas[i].getPeso() < Aristas[j].getPeso():  # menor a mayor
                    temp = Aristas[i]
                    Aristas[i] = Aristas[j]
                    Aristas[j] = temp

    # Prim para grafos dirigidos un solo sentido
    def Prim(self):
        CopiaAristas = copy(self.listaAristas)  # copia de las aristas
        Conjunto = []
        AristaPrim = []  # creo una lista con las aristas
        AristasTemp = []  # Todas las adyacencias

        self.Dobles(CopiaAristas)

        self.Ordenar(CopiaAristas)  # ordeno las aristas
        # self.Repetidas(CopiaAristas)#elimino los caminos dobles, ya que no nos interesan las dobles conexiones

        menor = CopiaAristas[0]
        Conjunto.append(menor.getOrigen())
        pos = True
        while pos:  # nuevo
            for Vertice in Conjunto:
                self.Algoritmo(
                    CopiaAristas, AristaPrim, Conjunto, Vertice, AristasTemp, pos
                )
            if len(Conjunto) == len(self.listaVertices):  # nuevo
                pos = False  # nuevo
        print("los vertices visitados fueron: {0} ".format(Conjunto))

        for dato in AristasTemp:
            print(
                "temporal Origen: {0} destino: {1} peso: {2}".format(
                    dato.getOrigen(), dato.getDestino(), dato.getPeso()
                )
            )
        print("Aristas de prim")
        for dato in AristaPrim:
            print(
                "Origen: {0} destino: {1} peso: {2}".format(
                    dato.getOrigen(), dato.getDestino(), dato.getPeso()
                )
            )

    def Algoritmo(self, CopiaAristas, AristaPrim, Conjunto, Vertice, AristasTemp, pos):
        ciclo = False
        # lo debo buscar en la lista de arista en ambas direcciones
        self.AgregarAristasTemp(CopiaAristas, Vertice, Conjunto, AristasTemp)
        menor = self.BuscarmenorTemp(
            AristasTemp, AristaPrim, CopiaAristas
        )  # obtengo la arista menor de los nodos que he visitado
        if menor is not None:
            if (
                menor.getOrigen() in Conjunto and menor.getDestino() in Conjunto
            ):  # es porque cierra un ciclo
                ciclo = True

            if ciclo is False:  # si es falso es porq puede ingresar
                if not menor.getDestino() in Conjunto:
                    Conjunto.append(menor.getDestino())
                AristaPrim.append(menor)

    def AgregarAristasTemp(self, CopiaAristas, Vertice, Conjunto, AristasTemp):
        for Aristas in CopiaAristas:
            if Vertice == Aristas.getOrigen():
                if self.verificarTemp(Aristas, AristasTemp):  # si no esta
                    AristasTemp.append(Aristas)  # Agrego todas las aristas

    def BuscarmenorTemp(self, AristasTemp, AristaPrim, CopiaAristas):
        menor = CopiaAristas[
            len(CopiaAristas) - 1
        ]  # el mayor como esta ordenado, es el ultimo
        for i in range(len(AristasTemp)):
            if AristasTemp[i].getPeso() <= menor.getPeso():
                if self.BuscarPrim(AristaPrim, AristasTemp[i]) is False:
                    menor = AristasTemp[i]

        AristasTemp.pop(AristasTemp.index(menor))
        return menor

    def BuscarPrim(self, AristaPrim, menor):
        for Aristap in AristaPrim:
            if (
                Aristap.getOrigen() == menor.getOrigen()
                and Aristap.getDestino() == menor.getDestino()
            ):
                return True
            if (
                Aristap.getOrigen() == menor.getDestino()
                and Aristap.getDestino() == menor.getOrigen()
            ):
                return True

        return False

    def verificarTemp(self, Aristan, AristasTemp):
        for Arista in AristasTemp:
            if (
                Arista.getOrigen() == Aristan.getOrigen()
                and Arista.getDestino() == Aristan.getDestino()
            ):
                return False

        return True

        ##Elimina los repetidos porque en prim no toma en cuenta las direcciones del grafo, por consiguiente con un enlace es mas que suficiente

    def Repetidas(self, CopiaAristas):
        for elemento in CopiaAristas:
            for i in range(len(CopiaAristas)):
                if (
                    elemento.getOrigen() == CopiaAristas[i].getDestino()
                    and elemento.getDestino() == CopiaAristas[i].getOrigen()
                ):
                    CopiaAristas.pop(i)  # elimino
                    break

    def Dobles(self, CopiaAristas):
        # Este método convierte el grafo dirigido
        # a un grafo no dirigido
        doble = False
        for elemento in CopiaAristas:
            for i in range(len(CopiaAristas)):
                # Compara el destino con el origen
                # Y el origen con el destino
                if (
                    elemento.getOrigen() == CopiaAristas[i].getDestino()
                    and elemento.getDestino() == CopiaAristas[i].getOrigen()
                ):
                    doble = True
            # Si no hay doble arista
            # crea la arista en doble sentido (Invirtiendo origen y destino)
            if doble is False:
                CopiaAristas.append(
                    arista(
                        elemento.getDestino(), elemento.getOrigen(), elemento.getPeso()
                    )
                )
            doble = False
