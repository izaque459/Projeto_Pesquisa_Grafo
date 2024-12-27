from buscas import bfs,bfs_with_goal,ucc_bfs,dfs, ucc_dfs
from grafo import create_fibonacci_sequence,build_fibonacci_tree_undirected, build_fibonacci_tree_directed
# Exemplo de uso
n = 20  # Número de elementos da sequência Fibonacci
fib_sequence = create_fibonacci_sequence(n)
graph_undirected, root_undirected = build_fibonacci_tree_undirected(n, fib_sequence)  # A raiz é o último elemento da sequência

print("\n Usando um grafo não direcionado \n")
print("\n Grafo Não Direcionado: \n")
for i in range(5):
    vizinhos = [vizinho.label for vizinho in graph_undirected.vertices_label[str(i)].neighbors]
    print(f"Vizinhos de {i}: {vizinhos}")
    
print("\n usando a função bfs \n")
bfs(root_undirected)
print("\n usando a função dfs \n")
dfs(root_undirected) # uso do dfs com grafo e a sua raiz
objetivo= 5
if bfs_with_goal(root_undirected,objetivo) :
    print (f'\n encontrado valor {objetivo} \n')
    
print("\n função de calculo de componentes conectado usando  busca em largura\n")
cc_bfs = ucc_bfs(graph_undirected)
print(cc_bfs)
print("\n função de calculo de componentes conectados usando busca em profundidade \n")
cc_dfs = ucc_dfs(graph_undirected)
print(cc_dfs)

print("\n Usando um grafo direcionado")
n = 20  # Número de elementos da sequência Fibonacci
fib_sequence = create_fibonacci_sequence(n)
graph_directed, root_directed = build_fibonacci_tree_directed(n, fib_sequence)  # A raiz é o último elemento da sequência

print("\nGrafo Direcionado:\n")
for i in range(5):
    vizinhos = [vizinho.label for vizinho in graph_directed.vertices_label[str(i)].neighbors]
    print(f"Vizinhos de {i}: {vizinhos}")

print("\n usando a função bfs \n")
bfs(root_directed)
print("\n usando a função dfs \n")
dfs(root_directed) # uso do dfs com grafo e a sua raiz
objetivo= 5
if bfs_with_goal(root_directed,objetivo) :
    print (f'\n encontrado valor {objetivo} \n')
    
print("\n função de calculo de componentes conectado usando  busca em largura\n")
cc_bfs1 = ucc_bfs(graph_directed)
print(cc_bfs1)
print("\n função de calculo de componentes conectados usando busca em profundidade \n")
cc_dfs = ucc_dfs(graph_directed)
print(cc_dfs)

