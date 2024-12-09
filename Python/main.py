import buscas
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
                
# Exemplo de uso
n = 20  # Número de elementos da sequência Fibonacci
fib_sequence = buscas.create_fibonacci_sequence(n)
graph, root = buscas.build_fibonacci_tree(n - 1, fib_sequence)  # A raiz é o último elemento da sequência

inicio = root.label
bfs(graph,inicio)