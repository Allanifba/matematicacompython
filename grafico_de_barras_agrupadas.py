# Gráfico do tipo barras agrupadas

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)

receita = [10,13,6]
lucro = [4,6,2]

plt.bar(x-0.2,receita,width = 0.2,color = 'blue',alpha = 0.5,edgecolor = 'black')
plt.bar(x,lucro,width = 0.2,color = 'green',alpha = 1,edgecolor = 'black')

plt.title('Receita x Lucro', fontsize = 15,color = 'red')
plt.xticks(x,['Janeiro','Fevereiro','Março'])
plt.xlabel('Meses',fontsize = 10, color = 'black')
plt.ylabel('Valor em milhares de reais', fontsize = 10, color = 'black')
plt.legend(['Receita','Lucro'], fontsize = 10)

plt.show()