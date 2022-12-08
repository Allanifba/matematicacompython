# Funções Trigonométricas
# 30 graus = pi/6 radianos
# sen(pi/6) = 0.5
# cos(pi/6) = 0.866025403
# tan(pi/6) = 0.577350269
# Caso utilize input, digite assim: xrad = eval(input('Digite o valor do ângulo: '))...

from math import sin, cos, tan, pi, radians

xrad = pi/6 # Entrada em radianos

s = sin(xrad)
c = cos(xrad)
t = tan(xrad)

print(round(s,9))
print(round(c,9))
print(round(t,9))