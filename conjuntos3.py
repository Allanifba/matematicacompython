#Conjuntos
A={1,2,3,4,5}
B={1,2,5,7,8}

#União de conjuntos | ou .union()
print(f'A união dos conjuntos A e B é dada por {A|B}.')
print(A.union(B))

#Interseção de conjuntos & ou .intersection()
print(f'A interseção dos conjuntos A e B é dada por {A&B}.')
print(f'A interseção dos conjuntos A e B é dada por {A.intersection(B)}.')

#Diferença de conjuntos - ou .difference()
print(f'A diferença A-B é dada por {A-B}')
print(f'A diferença B-A é dada por {B.difference(A)}')

#Diferença simétrica de dois conjuntos ^ ou .symetric_difference()
print(f'A diferença simétrica de A e B é {A.symmetric_difference(B)}')


