from buscas import bfs,bfs_with_goal,ucc_bfs
from grafo import create_fibonacci_sequence,build_fibonacci_tree
# Exemplo de uso
n = 20  # Número de elementos da sequência Fibonacci
fib_sequence = create_fibonacci_sequence(n)
graph, root = build_fibonacci_tree(n - 1, fib_sequence)  # A raiz é o último elemento da sequência

inicio = root.label
bfs(graph,inicio)

objetivo= 5
if bfs_with_goal(graph,inicio,objetivo) :
    print (f'encontrado valor {objetivo}')
    
cc = ucc_bfs(graph)
print(cc)