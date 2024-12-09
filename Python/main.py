import buscas

# Exemplo de uso
n = 100  # Número de elementos da sequência Fibonacci
fib_sequence = buscas.create_fibonacci_sequence(n)
root = buscas.build_fibonacci_tree(n - 1, fib_sequence)  # A raiz é o último elemento da sequência
