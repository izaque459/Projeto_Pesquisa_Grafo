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
        # Reutiliza vértices se o valor já existe

        if value in self.vertices_value:
            vertex = self.vertices_value[value]
        else:
            vertex = Vertex(label,value)
            self.vertices_value[value] = vertex
        self.vertices_label[label]= vertex

    def add_edge(self, u, v):
        self.vertices_label[u].neighbors.append(v)
        self.vertices_label[v].neighbors.append(u)  # Para grafo não direcionado
        
    def get_neighbors(self,u):
        return self.vertices_label[u].neighbors

        
# esta função criará a sequencia de fibonacci dado um numero de elementos
def create_fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
        
# esta funcao build_fibonacci_tree construirá o grafo a partir de uma lista com sequencia de fibonacci
def build_fibonacci_tree(n, fib_sequence):
    graph = Graph()

    # Adiciona vértices com rótulos e valores de Fibonacci
    for i in range(n):
        graph.add_vertex(str(i), fib_sequence[i])

    # Adiciona arestas para conectar os vértices de acordo com a sequência de Fibonacci
    for i in range(2, n):
        graph.add_edge(str(i), str(i-1))
        graph.add_edge(str(i), str(i-2))

    return graph, graph.vertices_label[str(n-1)]  # Retorna o grafo e o nó raiz

