import buscas
from collections import deque

def bfs(grafh,s):

    visited = set()
    queue = deque([s])
    visited.add(s)
    
    while queue:
        v = queue.popleft()
        print(f"Visitando: {v}")
        for w in grafh.get_neighbors(v):
            if w not in visited:
                visited.add(w)
                queue.append(w)
    return None
                
# Exemplo de uso
n = 20  # Número de elementos da sequência Fibonacci
fib_sequence = buscas.create_fibonacci_sequence(n)
grafh, root = buscas.build_fibonacci_tree(n - 1, fib_sequence)  # A raiz é o último elemento da sequência

inicio = root.label
bfs(grafh,inicio)