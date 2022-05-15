from classes.grafo import *

G = grafo()

G.ingresarVertice("Manizales")
G.ingresarVertice("Pereira")
G.ingresarVertice("Armenia")
G.ingresarVertice("Medellin")
G.ingresarVertice("Quimbaya")
# G.mostrarVertices()
G.ingresarAristas("Manizales", "Pereira", 4)
G.ingresarAristas("Manizales", "Medellin", 8)
G.ingresarAristas("Medellin", "Armenia", 6)
G.ingresarAristas("Pereira", "Armenia", 2)
G.ingresarAristas("Medellin", "Quimbaya", 4)
# G.mostrarAristas()
# G.mostrarAdyacencias()
# G.mostrarPozos()
# print(G.verificarFuente("Manizales"))

# G.ordenarAristas()
# G.obtenerGrado()
# G.fuentes()
# G.promPesos()
# G.mayorPeso()
# G.menorPeso()

G.Prim()
