# Função de várias variáveis (entradas)
# Exemplo: z = f(x,y) = x**2-2*y*x+1, (0,0),(1,-1),(2,3)

import math
import numpy as np

while True:
    z = input('Digite a função: ')
    entradas_x = eval(input('Digite abscissas, na ordem, separadas por vírgula: '))
    entradas_y = eval(input('Digite ordenadas, na ordem, separadas por vírgula: '))
    print('Os valores da função são dados a seguir: ')

    i = 0
    while i < len(entradas_x):
        x = entradas_x[i]
        y = entradas_y[i]
        def f(x,y):
            return eval(z)
        print(f'f({x},{y}) = {f(x,y)}')
        i = i + 1