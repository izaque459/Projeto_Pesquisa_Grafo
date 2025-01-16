# Data: 03/01/2025
# Esta classe Graph será diferente da implementada em grafo.py
# Pois ela conterah arestas com peso

from collections import deque
import heapq

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

        

def dijkstra(graph, s):
    dist = {v: float('inf') for v in graph.adjacencies}
    dist[s] = 0
    priority_queue = [(0, s)]  # Fila de prioridade: (distância, vértice)

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        # Se já processamos um caminho mais curto para este vértice, ignoramos
        if current_dist > dist[current_vertex]:
            continue

        for neighbor, weight in graph.adjacencies[current_vertex].items():
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return dist




# Exemplo de uso
graph = Graph()

# Adicionando vértices (capitais) com valores (população - valores fictícios/aproximados para demonstração)
capitais = {
    "Rio de Janeiro": 6748000,
    "São Paulo": 12325000,
    "Belo Horizonte": 2521000,
    "Vitória": 360000,
    "Salvador": 2886000,
    "Brasília": 3039441,
    "Campo Grande": 890574,
    "Curitiba": 1953000,
    "Florianópolis": 506000,
    "Goiânia": 1537000,
    "João Pessoa": 805000,
    "Manaus": 2205553,
    "Belém": 1499641,
    "Fortaleza": 2686612,
    "Recife": 1661000,
    "Porto Alegre": 1488000,
    "Cuiabá": 612547,
    "Natal": 884122,
    "Teresina": 861442,
    "Porto Velho": 548952,
    "Macapá": 512981,
    "Rio Branco": 413418,
    "Boa Vista": 399210,
    "Aracaju": 657000,
    "Maceió": 1029000,
    "São Luís": 1101000,
    "Palmas": 306296
}

for capital, populacao in capitais.items():
    graph.add_vertex(capital, populacao)




# Adicionando arestas (fronteiras e distâncias em linha reta - medidas obtidas a partir do rotamapas)
graph.add_edge("Rio de Janeiro", "São Paulo", 358)  # Distância aproximada em km
graph.add_edge("Rio de Janeiro", "Belo Horizonte", 342)
graph.add_edge("Rio de Janeiro", "Vitória", 415)
graph.add_edge("Vitória", "Salvador", 839)
graph.add_edge("Vitória", "Belo Horizonte", 380)
graph.add_edge("Vitória", "Rio de Janeiro", 415)
graph.add_edge("Salvador", "Vitória", 839)
graph.add_edge("Salvador", "Belo Horizonte", 964)
graph.add_edge("Salvador", "Goiânia", 1228)
graph.add_edge("Salvador", "Palmas", 1115)
graph.add_edge("Salvador", "Teresina", 995)
graph.add_edge("Salvador", "Recife", 676)
graph.add_edge("Salvador", "Aracaju", 277)
graph.add_edge("Salvador", "Maceió", 475)
graph.add_edge("Salvador", "Brasília", 1062)
graph.add_edge("Aracaju", "Salvador", 475)
graph.add_edge("Aracaju","Maceió", 201)
graph.add_edge("Maceió","Aracaju", 201)
graph.add_edge("Maceió","Salvador", 475)
graph.add_edge("Maceió","Recife", 203)
graph.add_edge("Recife","Maceió", 203)
graph.add_edge("Recife","Salvador", 676)
graph.add_edge("Recife","Teresina", 935)
graph.add_edge("Recife","Fortaleza", 629)
graph.add_edge("Recife","João Pessoa", 104)
graph.add_edge("João Pessoa","Recife", 104)
graph.add_edge("João Pessoa","Fortaleza", 555)
graph.add_edge("João Pessoa","Natal", 152)
graph.add_edge("Natal","João Pessoa", 152)
graph.add_edge("Natal","Fortaleza", 437)
graph.add_edge("Fortaleza","Recife", 629)
graph.add_edge("Fortaleza","João Pessoa", 555)
graph.add_edge("Fortaleza","Natal", 437)
graph.add_edge("Fortaleza","Teresina", 497)
graph.add_edge("Teresina","Salvador", 995)
graph.add_edge("Teresina","Recife", 935)
graph.add_edge("Teresina","Fortaleza", 497)
graph.add_edge("Teresina","São Luís", 328)
graph.add_edge("Teresina","Palmas", 838)
graph.add_edge("São Luís","Teresina", 828)
graph.add_edge("São Luís","Palmas", 967)
graph.add_edge("São Luís","Belém", 483)
graph.add_edge("Belém","São Luís", 483)
graph.add_edge("Belém","Palmas", 977)
graph.add_edge("Belém","Cuiabá", 1780)
graph.add_edge("Belém","Manaus", 1294)
graph.add_edge("Belém","Macapá", 331)
graph.add_edge("Belém","Boa Vista", 1436)
graph.add_edge("Manaus","Belém", 1294)
graph.add_edge("Manaus","Cuiabá", 1453)
graph.add_edge("Manaus","Porto Velho", 760)
graph.add_edge("Manaus","Rio Branco", 1150)
graph.add_edge("Manaus","Boa Vista", 665)
graph.add_edge("Rio Branco","Manaus", 1150)
graph.add_edge("Rio Branco","Porto Velho", 451)
graph.add_edge("Macapá","Belém", 331)
graph.add_edge("Boa Vista","Belém", 1436)
graph.add_edge("Boa Vista","Manaus", 665)
graph.add_edge("Porto Velho","Rio Branco", 451)
graph.add_edge("Porto Velho","Manaus", 760)
graph.add_edge("Porto Velho","Cuiabá", 1139)
graph.add_edge("Cuiabá","Porto Velho", 1139)
graph.add_edge("Cuiabá","Manaus", 760)
graph.add_edge("Cuiabá","Belém", 1780)
graph.add_edge("Cuiabá","Palmas", 1029)
graph.add_edge("Cuiabá","Brasília", 875)
graph.add_edge("Cuiabá","Goiânia", 740)
graph.add_edge("Cuiabá","Campo Grande", 561)
graph.add_edge("Palmas","Goiânia", 724)
graph.add_edge("Palmas","Brasília", 618)
graph.add_edge("Palmas","Belém", 977)
graph.add_edge("Palmas","São Luís", 967)
graph.add_edge("Palmas","Teresina", 838)
graph.add_edge("Palmas","Salvador", 1115)
graph.add_edge("Palmas","Cuiabá", 1029)
graph.add_edge("Goiânia","Brasília", 175)
graph.add_edge("Goiânia","Campo Grande", 703)
graph.add_edge("Goiânia","Cuiabá", 740)
graph.add_edge("Goiânia","Palmas", 724)
graph.add_edge("Goiânia","Belo Horizonte", 668)
graph.add_edge("Goiânia","Salvador", 1228)
graph.add_edge("Belo Horizonte","Vitória", 380)
graph.add_edge("Belo Horizonte","Rio de Janeiro", 342)
graph.add_edge("Belo Horizonte","São Paulo", 491)
graph.add_edge("Belo Horizonte","Goiânia", 668)
graph.add_edge("Belo Horizonte","Brasília", 625)
graph.add_edge("Belo Horizonte","Campo Grande", 1118)
graph.add_edge("Belo Horizonte","Salvador", 964)
graph.add_edge("São Paulo","Campo Grande", 892)
graph.add_edge("São Paulo","Curitiba", 338)
graph.add_edge("São Paulo","Belo Horizonte", 491)
graph.add_edge("São Paulo","Rio de Janeiro", 358)
graph.add_edge("Curitiba","São Paulo", 338)
graph.add_edge("Curitiba","Campo Grande", 779)
graph.add_edge("Curitiba","Florianópolis", 252)
graph.add_edge("Campo Grande","Curitiba", 779)
graph.add_edge("Campo Grande","São Paulo", 892)
graph.add_edge("Campo Grande","Goiânia", 703)
graph.add_edge("Campo Grande","Brasília", 878)
graph.add_edge("Campo Grande","Cuiabá", 561)
graph.add_edge("Brasília","Goiânia", 175)
graph.add_edge("Florianópolis","Curitiba", 252)
graph.add_edge("Florianópolis","Porto Alegre", 375)
graph.add_edge("Porto Alegre","Florianópolis", 375)
graph.add_edge("Brasília", "Belo Horizonte", 625)
graph.add_edge("Brasília", "Rio de Janeiro", 935)
graph.add_edge("Brasília", "São Paulo", 873)
graph.add_edge("Brasília", "Campo Grande", 878)

graph.print_graph()

# Tentando adicionar um vértice já existente
graph.add_vertex("Rio de Janeiro", 0)

# Tentando adicionar uma aresta com vértice inexistente
graph.add_edge("Rio de Janeiro", "Miami", 0)

distancias = dijkstra(graph,"Rio de Janeiro")

for cidade, distancia in distancias.items():
    print(f"Distância do Rio de Janeiro para {cidade}: {distancia}")

