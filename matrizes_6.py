# Resolução de sistemas lineares nxn usando matrizes
'''
Exemplo:      4x + 3y -  z =  8
               x - 2y + 3z = -4
             -2x + 4y +  z =  1
             sol = (1,1,-1)^t
'''


import numpy as np

A = np.matrix([[4,3,-1],
               [1,-2,3],
               [-2,4,1]], dtype = 'float')

B = np.matrix([[8],
               [-4],
               [1]], dtype = 'float')

inv_A = np.linalg.inv(A)
sol = inv_A*B
print(sol)