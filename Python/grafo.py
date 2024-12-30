# classe Vertex será o vertice do grafo, tendo label=rotulo, conteudo=value ,neighbors=folhas
class Vertex:
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.neighbors = []

# o Grafo adicionará os vertices, arestas e ajudará na buscas dos algoritmo
class Graph:
    def __init__(self):
        self.vertices_label = {}
        self.vertices_value = {}

    def add_vertex(self, label, value=None):

        if value in self.vertices_value:# Reutiliza vértices se o valor já existe
            vertex = self.vertices_value[value]
        else:
            vertex = Vertex(label,value)
            self.vertices_value[value] = vertex
        self.vertices_label[label]= vertex

    def add_edge_undirected(self, u, v):
        self.vertices_label[u].neighbors.append(self.vertices_label[v])
        self.vertices_label[v].neighbors.append(self.vertices_label[u])  # Para grafo não direcionado

    def add_edge_directed(self,u,v):
        self.vertices_label[u].neighbors.append(self.vertices_label[v])  # Para grafo direcionado

        
# A função a seguir criará a sequencia de fibonacci dado um numero de elementos
def create_fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
        
# esta funcao build_fibonacci_tree construirá o grafo não direcionado a partir de uma lista com sequencia de fibonacci
def build_fibonacci_tree_undirected(n, fib_sequence):
    graph = Graph()

    for i in range(n):# Adiciona vértices com rótulos e valores de Fibonacci
        graph.add_vertex(str(i), fib_sequence[i])

    for i in range(2, n):# Adiciona arestas para conectar os vértices de acordo com a sequência de Fibonacci
        graph.add_edge_undirected(str(i), str(i-1))
        graph.add_edge_undirected(str(i), str(i-2))

    return graph, graph.vertices_label[str(n-1)]  # Retorna o grafo e o nó raiz

# esta funcao build_fibonacci_tree construirá o grafo direcionado a partir de uma lista com sequencia de fibonacci
def build_fibonacci_tree_directed(n, fib_sequence):
    graph = Graph()

    for i in range(n):# Adiciona vértices com rótulos e valores de Fibonacci
        graph.add_vertex(str(i), fib_sequence[i])

    for i in range(2, n):# Adiciona arestas para conectar os vértices de acordo com a sequência de Fibonacci
        graph.add_edge_directed(str(i), str(i-1))
        graph.add_edge_directed(str(i), str(i-2))

    return graph, graph.vertices_label[str(n-1)]  # Retorna o grafo e o nó raiz

def reverse_graph(original_graph):
    
    graph_reversed = Graph()
    
    # Adiciona os vertices ao grafo reverso
    for label, vertex in original_graph.vertices_label.items():
        graph_reversed.add_vertex(label, vertex.value)
        
    # Inverte as arestas
    for label, vertex in original_graph.vertices_label.items():
        for neighbor in vertex.neighbors:
            graph_reversed.add_edge_directed(neighbor.label, label) #Inverte a direção da aresta

    return graph_reversed
    
    return graph