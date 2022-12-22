# Destaques pontuais no gráfico de uma função

import matplotlib.pyplot as plt
from pylab import arange, annotate

def f(x):
    return x**2

x = arange(-3,3,0.1)
y = f(x)

# plt.plot(x,y)
# plt.plot(x,y,'*')
plt.plot(x,y,'d')
plt.title('Parábola y = x**2')
plt.xlabel('Tempo(s)')
plt.ylabel('Altura(m)')
plt.grid()
annotate('Mínimo',xy = (0,f(0)),xytext = (1,3), arrowprops=dict(facecolor = 'r', shrink = 0))
plt.show()