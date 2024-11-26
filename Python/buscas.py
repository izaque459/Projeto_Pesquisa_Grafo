# classe Vertex será o vertice do grafo, tendo label=rotulo, conteudo=value ,neighbors=folhas
class Vertex:
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.neighbors = []

# o Grafo adicionara os vertices, arestas e ajudará na buscas dos algoritmo

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label, value=None):
        self.vertices[label] = Vertex(label, value)

    def add_edge(self, u, v):
        self.vertices[u].neighbors.append(v)
        self.vertices[v].neighbors.append(u)  # Para grafo não direcionado