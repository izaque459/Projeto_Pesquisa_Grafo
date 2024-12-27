from buscas import bfs,bfs_with_goal,ucc_bfs,dfs
from grafo import create_fibonacci_sequence,build_fibonacci_tree
# Exemplo de uso
n = 20  # Número de elementos da sequência Fibonacci
fib_sequence = create_fibonacci_sequence(n)
graph, root = build_fibonacci_tree(n - 1, fib_sequence)  # A raiz é o último elemento da sequência

print("\n usando a função bfs \n")
bfs(root)
print("\n usando a função dfs recursiva \n")
dfs(root) # uso do dfs com grafo e a sua raiz
objetivo= 5
if bfs_with_goal(root,objetivo) :
    print (f'\n encontrado valor {objetivo} \n')
    
print("\n função de calculo de componentes conectado usando  busca em largura\n")
cc_bfs = ucc_bfs(graph)
print(cc_bfs)
print("\n função de calculo de componentes conectados usando busca em profundidade \n")
#cc_dfs = ucc_dfs(graph)
#print(cc_dfs)



