from grafo import Vertex,Graph
from collections import deque

# bfs faz uma pesquisa em largura em um grafo a partir de um rotulo de um nó
def bfs(graph,s):

    visited = set()
    queue = deque([graph.vertices_label[s]])# Obtenha o objeto Vertex para depuração
    visited.add(s)
    
    while queue:
        v = queue.popleft()
        print(f"Visitando: {v.label}, valor fibonacci: {v.value} endereco: {id(v)}") # Para depuração
        for w in v.neighbors:
            if w.label not in visited:
                visited.add(w.label)
                queue.append(w)
    return None
               
# bfs_with_goal faz uma pesquisa em lagura em um grafo mas pode terminar antes desde qeu encontre um objetivo             
def bfs_with_goal(graph,s,goal):

    visited = set()
    queue = deque([graph.vertices_label[s]])# Obtenha o objeto Vertex para depuração
    visited.add(s)
    
    while queue:
        v = queue.popleft()
        if v.value == goal:
            return v # se o objetivo for encontrado retorna o nó
        for w in v.neighbors:
            if w.label not in visited:
                visited.add(w.label)
                queue.append(w)
    return None

# ucc_bfs calcula componentes conexas do grafo
def ucc_bfs(graph):
    cc = {}
    numCC = 0
    explored = set()
    
    for i in graph.vertices_label:
        if i not in explored:
            numCC += 1
            queue = deque([graph.vertices_label[i]])
            while queue:
                v = queue.popleft()
                if v.label not in explored:
                    explored.add(v.label)
                    cc[v.label] = numCC
                    for w in v.neighbors:
                        if w.label not in explored:
                            queue.append(w)
        
    return cc