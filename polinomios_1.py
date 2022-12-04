# Soluções de uma equação polinomial
# Exemplo: x**2 - 5*x + 6 = 0

from numpy import roots

coef = [1,-5,6]
raizes = roots(coef)
print(raizes[0])
print(raizes[1])


