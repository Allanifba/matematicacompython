# Operações com polinômios
# Polinômios: x**2-5*x+6,x**2+3*x-1,x+4,x-3,x-2,x+1

from numpy import polyadd,polysub,polymul,polydiv

# Soma
pol_1 = [1,-5,6]
pol_2 = [1,3,-1]
soma = polyadd(pol_1,pol_2)
print(soma)

# Subtração
sub = polysub(pol_1,pol_2)
print(sub)

# Multiplicação
pol_3 = [1,4]
pol_4 = [1,-3]
mult = polymul(pol_3,pol_4)
print(mult)

# Divisão
pol_5 = [1,-2]
pol_6 = [1,1]
div_1 = polydiv(pol_1,pol_5)
div_2 = polydiv(pol_1,pol_6)
print(div_1)
print(div_2)