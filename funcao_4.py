# Definindo uma função
import math
import numpy as np

# pi no PyCharm é dado por np.pi
x = input('Digite o valor de x: ')
xs = eval(x)
def f(xs):
    return np.cos(xs)
print(f'f({xs}) = {f(xs)}')