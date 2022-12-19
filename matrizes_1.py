# Inserção de uma matriz
'''
Exemplo: A = [1 2 3
              2 1 0
              3 4 1]
         A^t = [1 2 3
                2 1 4
                3 0 1

'''

import numpy as np

A = np.matrix([[1,2,3],
               [2,1,0],
               [3,4,1]])
# print(A)


# Dimensão de uma matriz
d = A.shape
# print(d)

# Consultando elementos, linhas e colunas
print(A[0,2]) # Mostra o elemento da linha 0, coluna 2
print(A[1]) # Mostra a linha 2
print(A.transpose()[1]) # Mostra a coluna 2


