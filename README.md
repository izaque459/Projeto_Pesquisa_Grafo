# Projeto_Pesquisa_Grafo
Um projeto de pesquisa em largura e profundidade em grafo.

## Descrição
Um grafo será criado com conteudo a partir da sequencia de fibonacci. O conteúdo da  raiz será a soma de suas folhas
, assim sucessivamente onde cada conteudo folha será a soma dos seus antecessores, seguindo a regra de criação de
sequencia de fibonacci. Seria natural pensar em uma arvore para guardar esses conteudos, mas em algum momento eles se 
repetiram, então a ideia de usar um grafo para economia de memória, onde os conteudos já criados serão sempre 
reutilizados.