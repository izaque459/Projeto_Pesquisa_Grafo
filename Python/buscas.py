from grafo import Vertex,Graph
from collections import deque

# bfs faz uma pesquisa em largura em um grafo a partir de um rotulo de um nó
def bfs(s):

    explored = set()
    queue = deque([s])  # Obtenha o objeto Vertex para depuração
    explored.add(s)     #explored.add(s.label)
    
    while queue:
        v = queue.popleft()
        print(f"Visitando: {v.label}, valor fibonacci: {v.value} endereco: {id(v)}") # Para depuração
        for w in v.neighbors:
            if w not in explored:   #if w.label not in explored:
                explored.add(w)        #explored.add(w.label)
                queue.append(w)
    return None
               
# bfs_with_goal faz uma pesquisa em lagura em um grafo mas pode terminar antes desde qeu encontre um objetivo             
def bfs_with_goal(s,goal):

    explored = set()
    queue = deque([s])# Obtenha o objeto Vertex para depuração
    explored.add(s)
    
    while queue:
        v = queue.popleft()
        if v.value == goal:
            return v # se o objetivo for encontrado retorna o nó
        for w in v.neighbors:
            if w not in explored:
                explored.add(w)
                queue.append(w)
    return None

# ucc_bfs rotula componentes conexas do grafo usando um busca em largura
def ucc_bfs(graph):
    cc = {}
    numCC = 0
    explored = set()
    
    for i in graph.vertices_label:
        if graph.vertices_label[i] not in explored:
            numCC += 1
            queue = deque([graph.vertices_label[i]]) #usando uma fila
            while queue:
                v = queue.popleft()
                if v not in explored:
                    explored.add(v)
                    cc[v.label] = numCC
                    for w in v.neighbors:
                        if w not in explored:
                            queue.append(w)
        
    return cc
    
# funcao a seguir implementa a busca em profundidade de um grafo a partir de rotulo s de um nó versao iterativa

def dfs(s):

    explored = set()
    queue = deque([s])# Obtenha o objeto Vertex para depuração
    
    while queue:
        v = queue.pop()
        if v not in explored:
            explored.add(v) #explored.add(v.label)
            print(f"Visitando: {v.label}, valor fibonacci: {v.value} endereco: {id(v)}") # Para depuração
            for w in v.neighbors:
                queue.append(w)

    return None

#def ucc_dfs(graph):
#    cc = {}
#    numCC = 0
#    explored = set()

#    for i in graph.vertices_label:
#       if i not in explored:
#            numCC += 1
#            queue = deque([graph.vertices_label[i]]) #usando uma pilha
 #           while queue:
#                v = queue.pop()
#                if v.label not in explored:
#                    explored.add(v.label)
#                    cc[v.label] = numCC
#                    for w in v.neighbors:
#                        if w.label not in explored:
#                            queue.append(w)
            
#    return cc
    

#def dfs(s):
#    explored = set()

#    def dfs_recursive(v):
#        explored.add(v)
#        print(f"Visitando: {v.label}, valor fibonacci: {v.value}, endereco: {id(v)}")  # Para depuração

#        for w in v.neighbors:
#           if w not in explored:
#                dfs_recursive(w)

    # usando dfs_recursive como parametro um vertice-nó
#    dfs_recursive(s)

#    return None

def ucc_dfs(graph):
    cc = {}
    numCC = 0
    explored = set()
    
    def ucc_dfs_recursive(v):
        explored.add(v)
        cc[v.label] = numCC
        for w in v.neighbors:
            if w not in explored:
                ucc_dfs_recursive(w)
    
    for i in graph.vertices_label:
        if graph.vertices_label[i] not in explored:
            numCC+=1
            ucc_dfs_recursive(graph.vertices_label[i])
    
    return cc
 # a funcao TopoSort calcula a ordem topologica do grafo, efeito pratico verifica se há precedentes
def TopoSort(graph):
    explored =  set()
    curLabel = len(graph.vertices_label)
    ordering = {}
    
    def DFS_Topo(v):
        nonlocal curLabel
        explored.add(v)
        for w in v.neighbors:
            if w not in explored:
                DFS_Topo(w)
        ordering[v.label] = curLabel
        curLabel -= 1
        
    for label in graph.vertices_label:
        if graph.vertices_label[label] not in explored:
            DFS_Topo(graph.vertices_label[label])
    
    return ordering