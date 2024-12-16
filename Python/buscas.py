from grafo import Vertex,Graph
from collections import deque

# bfs faz uma pesquisa em largura em um grafo a partir de um rotulo de um nó
def bfs(graph,s):

    visited = set()
    queue = deque([s])
    visited.add(s)
    
    while queue:
        v = queue.popleft()
        vertex = graph.vertices_label[v]  # Obtenha o objeto Vertex para depuração
        print(f"Visitando: {v}, valor fibonacci: {vertex.value} endereco: {id(vertex)}") # Para depuração
        for w in graph.get_neighbors(v):
            if w not in visited:
                visited.add(w)
                queue.append(w)
    return None
               
# bfs_with_goal faz uma pesquisa em lagura em um grafo mas pode terminar antes desde qeu encontre um objetivo             
def bfs_with_goal(graph,s,goal):

    visited = set()
    queue = deque([s])
    visited.add(s)
    
    while queue:
        v = queue.popleft()
        vertex = graph.vertices_label[v]  # Obtenha o objeto Vertex para depuração
        if vertex.value == goal:
            return vertex # se o objetivo for encontrado retorna o nó
        for w in graph.get_neighbors(v):
            if w not in visited:
                visited.add(w)
                queue.append(w)
    return None