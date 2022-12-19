# Operações com matrizes

import numpy as np

A = np.matrix([[1,2],[2,3]], dtype = 'float')
B = np.matrix([[-1,0],[1,2]], dtype = 'float')

# Soma de matrizes
soma = A + B
# print(soma)

# Produto de matrizes
prod = A*B # prod = np.dot(A,B)
# print(A*B)

# Produto de uma matriz por um escalar
prod_esc = 2*A
# print(prod_esc)

# Produto de matrizes termo a termo
mult = np.multiply(A,B)
# print(mult)

# Inversa de uma matriz
inv_A = np.linalg.inv(A)
# print(inv_A) # Teste print(A*inv_A) = identidade


# Determinante de uma matriz
det_A = np.linalg.det(A)
print(det_A)