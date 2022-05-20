import random

def ordenacao_selecao(A):
    n = len(A)
    # Percorre o arranjo A.
    for i in range(n):
        # Encontra o elemento mínimo em A.
        minimo = i
        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j
        # Coloca o elemento mínimo na posição correta.
        A[i], A[minimo] = A[minimo], A[i]

A = random.sample(range(-10, 10), 10)

print("\n \nArranjo não ordenado: \t", A)

ordenacao_selecao(A)
print("Arranjo ordenado: \t", A)
#
#
#
##################################################
import random

def ordenacao_insercao(A):
    n = len(A)
    # Percorre o arranjo A.
    for j in range(1, n):
        chave = A[j]
        i = j - 1
        # Insere o elemento A[j] na posição correta.
        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave

A = random.sample(range(-10, 10), 10)

print("\n \nArranjo não ordenado: \t", A)

ordenacao_insercao(A)

print("Arranjo ordenado: \t", A)
#
#
#
#######################################
import random

def ordenacao_bolha(A):
    n = len(A)

    for i in range(n):
        for j in range (0,len(A)-1):  
            if (A[j]>A[j+1]):
                temp = A[j]  
                A[j] = A[j+1]  
                A[j+1] = temp

A = random.sample(range(-10, 10), 10)
print("\n \nArranjo não ordenado: \t", A)

ordenacao_bolha(A)

print("Arranjo ordenado: \t", A)

