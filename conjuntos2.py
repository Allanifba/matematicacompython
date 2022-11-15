#Tamanho de um conjunto
A={1,2,3,4,5}
D={1,3,5}
E={1,3,6}
F={1,3,2,4,5}
Bruno={'Casa','Terreno','Carro'}
print(f'O número de elementos do conjunto A é {len(A)}.')
print(f'Bruno tem {len(Bruno)} bens.')

#n-upla
B=[1,2,3,4,5]
G=[1,2,4,3,5]
print(f'B={B}')
print(B[3])

#Função 'set()'
C=set(B)
print(f'C={C}')

#Relação de inclusão
print(D < A)
print(E < A)

#Igualdade de conjuntos//n-uplas
print(F==A)
print(G==B)



