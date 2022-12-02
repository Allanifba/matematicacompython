# Definindo uma função
import math
import numpy as np

x = float(input('Digite o valor de x: '))
def f(x):
    return np.cos(x)
print(f'f({x}) = {f(x)}')