# Data: 03/01/2025
# Esta classe Graph será diferente da implementada em grafo.py
# Pois ela contera arestas com peso

class Graph:

    def __init__(self):
        self.adjacencies = {}
        self.vertices_values = {}
        
    def add_vertex(self,label,value):
        if label in not self.adjacencies:
            self.adjacencies[label]={}
            self.vertice_values[label] = value
        else:
            print(f"vertice {label} ja existe")
     
    def add_edge(self,origin, destination, weight):
        if origin in self.adjacencies and destination in self.adjacencies:
            self.adjacencies[origin][destination] = weight
        else:
            print("Vertices de origem ou destino nao existem no grafo")

        

def dijkstra(graph):
    return None

