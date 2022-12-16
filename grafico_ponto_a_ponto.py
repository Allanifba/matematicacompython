# Gráfico ponto a ponto

import matplotlib.pyplot as plt

x = [1,3,5,9,10]
y = [-1,2,3,1,0] #(1,-1), (3,2), (5,3),...

# plt.plot(x,y)
# plt.plot(x,y,'*')
plt.plot(x,y,'d')
plt.title('Título')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.show()
