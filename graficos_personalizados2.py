# Gráficos personalizados - Parte 2

import matplotlib.pyplot as plt
from pylab import arange
from numpy import sin, pi

def f(x):
    return x**2

def g(x):
    return 2*x+1

def h(x):
    return sin(x)

x = arange(0,1,0.1) #(0,1), delta=0.1
plt.plot(x,f(x),'-b')
plt.plot(x,g(x),'-.r')
plt.plot(x,h(x),':k')

plt.title('Parábola, Reta, Seno')
plt.xlabel('Tempo(s)')
plt.ylabel('Altura(m)')
plt.legend(['Parábola','Reta','Seno'])
plt.grid()
plt.axhline(0,color = 'k')
plt.axvline(0,color = 'k')
plt.show()


'''
MARCADORES (Gráfico ponto a ponto)

COMANDO		FORMA DO PONTO
.		    ponto
*		    asterisco
d		    losango
v		    triângulo 1
^		    triângulo 2
s		    quadrado
p		    pentágono
h		    hexágono
+		    cruz
x		    letra x


LINHA (Gráfico contínuo)

COMANDO		FORMA DA LINHA
-		    contínua
--		    tracejada
:		    pontilhada
-.		    traço-ponto


CORES

COMANDO		COR
b		    azul
r		    vermelho
g		    verde
c		    ciano
m		    magenta
y 		    amarelo
k		    preto
w		    branco

'''




