# 1. Escreva uma função em Python chamada matriz_para_dicionario que
# receba como parâmetro qualquer Matriz de Adjacência nxn de um grafo não orientado e retorne o
# Dicionário de Adjacência correspondente.
def matriz_para_dicionario(matriz_adj):
    return {
        i: [j for j, val in enumerate(linha) if val == 1]
        for i, linha in enumerate(matriz_adj)
    }


matrizAdjacencia = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

dicionario = matriz_para_dicionario(matrizAdjacencia)
for chave, valor in dicionario.items():
    print(f"Vertice: {chave}, Aresta: {valor}")

# 2 .Considere a seguinte Matriz de Incidência referente a um grafo não orientado com 4
# vértices e 4 arestas, onde as linhas representam os vértices 0, 1, 2, 3 e as colunas
# representam as arestas e0, e1, e2, e3. Identifique e imprima quais são os dois vértices
# conectados pela aresta e2.

matriz_incidencia = [[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]

aresta = 2

vertices = [v for v, linha in enumerate(matriz_incidencia) if linha[aresta] == 1]
print(f"A aresta e{aresta} conecta os vértices {vertices[0]} e {vertices[1]}")

#Possivel resolução da questão se pudesse usar Classes
# class Grafo:
#    def __init__(self, vertices):
#      self.vertices = vertices
#      self.listaAdjacencia = {i: [] for i in range(vertices)}
#    def gerarListaAdj(self, matriz_adj):
#      for i in range(self.vertices):
#        for j in range(self.vertices):
#          if matriz_adj[i][j] == 1:
#            self.listaAdjacencia[i].append(j)
#
#      return self.listaAdjacencia