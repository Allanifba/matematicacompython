# Funções Trigonométricas Inversas
# 30 graus = pi/6 radianos
# sen(pi/6) = 0.5
# cos(pi/6) = 0.866025403
# tan(pi/6) = 0.577350269

from math import asin, acos, atan, degrees

ys = 0.5
arc_s = degrees(asin(ys))
print(round(arc_s,2))

yc = 0.866025403
arc_c = degrees(acos(yc))
print(round(arc_c,2))

yt = 0.577350269
arc_t = degrees(atan(yt))
print(round(arc_t,2))
