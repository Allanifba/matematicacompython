# Gráfico de uma função

import matplotlib.pyplot as plt
from pylab import arange

def f(x):
    return x**2

x = arange(0,1,0.1) #(0,1), delta=0.1
y = f(x)

# plt.plot(x,y)
# plt.plot(x,y,'*')
plt.plot(x,y,'d')
plt.title('Parábola y = x**2')
plt.xlabel('Tempo(s)')
plt.ylabel('Altura(m)')
plt.show()
