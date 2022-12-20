# Autovalores e autovetores

import numpy as np

A = np.matrix([[4,3],
               [1,2]], dtype = 'float')

autov_A = np.linalg.eig(A)
# print(autov_A) # Apresenta tanto autovalores quanto autovetores
# print(autov_A[0]) # Apresenta os autovalores
# print(autov_A[0][0]) # Exibe o primeiro autovalor
# print(autov_A[0][1]) # Exibe o segundo autovalor
# print(autov_A[1]) # Exibe os autovetores
# print(autov_A[1][:,0]) # Exibe o primeiro autovetor
# print(autov_A[1][:,0]/autov_A[1][1,0]) # Exibe o primeiro autovetor normalizado
# print(autov_A[1][:,1]) # Exibe o segundo autovetor
print(autov_A[1][:,1]/autov_A[1][1,1]) # Exibe o primeiro autovetor normalizado