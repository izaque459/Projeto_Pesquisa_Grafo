from buscas import Vertex,Graph,create_fibonacci_sequence,build_fibonacci_tree
from collections import deque

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
# Exemplo de uso
n = 20  # Número de elementos da sequência Fibonacci
fib_sequence = create_fibonacci_sequence(n)
graph, root = build_fibonacci_tree(n - 1, fib_sequence)  # A raiz é o último elemento da sequência

inicio = root.label
bfs(graph,inicio)

objetivo= 5
if bfs_with_goal(graph,inicio,objetivo) :
    print (f'encontrado valor {objetivo}')