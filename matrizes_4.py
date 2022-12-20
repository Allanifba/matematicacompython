# + Operações com matrizes

import numpy as np

A = np.matrix([[1,2,1],
               [2,3,6],
               [-1,1,4]], dtype = 'float')

B = np.matrix([[1,-1,2],
               [4,1,2],
               [-1,2,2]], dtype = 'float')

# Soma de um elemento a uma matriz
C = A + 4
# print(C)

# Potência de uma matriz termo a termo
pot = np.power(A,3)
# print(pot)

# Divisão de matrizes termo a termo
div = A/B
# print(div)

# Maior e menor elementos de uma matriz, linha ou coluna
max_A = A.max() # Exibe o maior valor de A
maxc_A = A.max(0) # Exibe o maior valor de cada coluna de A
maxl_A = A.max(1) # Exibe o maior valor de cada linha de A
min_A = A.min() # Exibe o menor valor de A
minc_A = A.min(0) # Exibe o menor valor de cada coluna de A
minl_A = A.min(1) # Exibe o menor valor de cada linha de A
# print(max_A)
# print(maxc_A)
# print(maxl_A)
# print(min_A)
# printo(minc_A)
# print(minl_A)

# Soma dos elementos de uma matriz, linha ou coluna
soma_A = A.sum() # Soma todos os elementos de A
somac_A = A.sum(0) # Soma todos os elementos das colunas
somal_A = A.sum(1) # Soma todos os elementos das linhas
# print(soma_A)
# print(somac_A)
print(somal_A)


