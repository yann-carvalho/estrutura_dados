# 1. Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o algoritmo de seleção.

def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        # vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]
        aux = vetor[i]
        vetor[i] = vetor[indice_minimo]
        vetor[indice_minimo] = aux

vetor=[5,7,4,3]
selecao_ordenacao(vetor)
print(vetor)