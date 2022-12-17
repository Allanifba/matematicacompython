# Gráfico do tipo histograma

import matplotlib.pyplot as plt

idades=[15,26,67,50,37,73,1,58,2,12,42,12,75,25,13,61,41,
	    24,95,3,71,63,24,23,47,83,38,19,32,71,86,45,6,99,
	    4,76,27,50,18,58,61,53,72,14,78,36,89,6,91,68,69,
	    27,34,48,41,81,83,22,22,36,44,16,58,20,28,55,21,
	    26,23,41,21,95,18,63,55,2,61,81,39,20,39,17,66,60,
	    73,26,54,16,76,83,9,15,15,35,54,11,7,61]

plt.hist(idades,6,rwidth=0.9,color = 'blue', alpha = 0.5,edgecolor = 'red')
plt.title('Idades de Pessoas de Uma Família', fontsize = 15, color = 'red')
plt.xlabel('Idade', fontsize = 10, color = 'black')
plt.ylabel('Frequência', fontsize = 10, color = 'black')
plt.tick_params(labelsize=10)


plt.show()