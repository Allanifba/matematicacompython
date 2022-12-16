# Gráfico de várias funções em uma mesma janela

import matplotlib.pyplot as plt
from pylab import arange

def f(x):
    return x**2

def g(x):
    return 2*x+1

x = arange(0,10,0.1) #(0,1), delta=0.1
plt.plot(x,f(x))
plt.plot(x,g(x))

plt.title('Reta x Parábola')
plt.xlabel('Tempo(s)')
plt.ylabel('Altura(m)')
plt.legend(['Parábola','Reta'])
plt.show()