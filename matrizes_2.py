# Matrizes especiais

import numpy as np

# Matriz nula
A0 = np.zeros((2,3), dtype = 'int')
# print(A0)


# Matriz unitária
A1 = np.zeros((3,3), dtype = 'float')
# print(A1)

# Matriz identidade
ident = np.identity(5, dtype = 'float')
# print(ident)


# Matriz transposta
A = np.matrix([[1,2,3],[2,1,0],[3,4,1]])
print(f'A = {A}')
B = A.transpose()
print(f'A^t = {B}')