# Soluções de uma equação polinomial
# Exemplo 1: x**2 - 5*x + 6 = 0 >>> Digite assim: 1,-5,6
# Exemplo 2: x**2 + 1 = 0 >>> Digite assim: 1,0,1
# Exemplo 3: x**3 - 3*x + 1 = 0 >>> Digite assim: 1,0,-3,1

from numpy import roots

while True:
    coef = eval(input('Digite os coeficientes do polinômio separados por vírgugla: '))
    raizes = roots(coef)

    i=0
    for n in raizes:
        print(f'x{i+1} = {raizes[i]}')
        i = i + 1
