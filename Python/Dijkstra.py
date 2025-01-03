# Data: 03/01/2025
# Esta classe Graph será diferente da implementada em grafo.py
# Pois ela conterah arestas com peso

class Graph:

    def __init__(self):
        self.adjacencies = {}
        self.vertices_values = {}
        
    def add_vertex(self,label,value):
        if label not in self.adjacencies:
            self.adjacencies[label]={}
            self.vertices_values[label] = value
        else:
            print(f"vertice {label} ja existe")
     
    def add_edge(self,origin, destination, weight):
        if origin in self.adjacencies and destination in self.adjacencies:
            self.adjacencies[origin][destination] = weight
        else:
            print("Vertices de origem ou destino nao existem no grafo")
           
    def print_graph(self):
        for vertex, adjacents in self.adjacencies.items():
            print(f"Vértice: {vertex}")
            for adjacent, weight in adjacents.items():
                print(f"  -> {adjacent}: {weight}")

        

def dijkstra(graph):
    return None




# Exemplo de uso
graph = Graph()

# Adicionando vértices (capitais) com valores (ex: população - valores fictícios para demonstração)
graph.add_vertex("Rio de Janeiro", 6748000)
graph.add_vertex("São Paulo", 12325000)
graph.add_vertex("Belo Horizonte", 2521000)
graph.add_vertex("Vitória", 360000)
graph.add_vertex("Salvador", 2886000)


# Adicionando arestas (fronteiras e distâncias - valores fictícios para demonstração)
graph.add_edge("Rio de Janeiro", "São Paulo", 430)  # Distância aproximada em km
graph.add_edge("Rio de Janeiro", "Belo Horizonte", 440)
graph.add_edge("Rio de Janeiro", "Vitória", 520)
graph.add_edge("Vitória", "Salvador", 1200)
graph.add_edge("Vitória", "Belo Horizonte", 510)

graph.print_graph()

# Tentando adicionar um vértice já existente
graph.add_vertex("Rio de Janeiro", 0)

# Tentando adicionar uma aresta com vértice inexistente
graph.add_edge("Rio de Janeiro", "Manaus", 0)