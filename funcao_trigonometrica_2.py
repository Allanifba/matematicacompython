# Funções Trigonométricas
# 30 graus = pi/6 radianos
# sen(pi/6) = 0.5
# cos(pi/6) = 0.866025403
# tan(pi/6) = 0.577350269

from math import sin, cos, tan, pi, radians

xgr = 30 # Entrada em graus
xrad = radians(xgr)

s = sin(xrad)
c = cos(xrad)
t = tan(xrad)

print(round(s,9))
print(round(c,9))
print(round(t,9))
