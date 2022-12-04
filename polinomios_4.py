# Fatorando polinômios
# Exemplo 1: x**2- 5*x + 6
# Exemplo 2: x**3-x**2-x+1
# Exemplo 3: x**3-x**2+x-1

from sympy.abc import x
from sympy import factor

pol = input('Digite o polinômio: ')
pol_fat = factor(pol)
print(pol_fat)
