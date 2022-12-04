# Expandindo polinômios
# Exemplo 1: x*(x+1)
# Exemplo 2: x*(x-y) - y*(x+y)

from sympy.abc import x,y
from sympy import expand

pol = input('Digite o polinômio: ')
pol_exp = expand(pol)
print(pol_exp)
