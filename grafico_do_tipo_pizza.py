# Gráfico do tipo pizza

import matplotlib.pyplot as plt
import numpy as np

candidatos = ['Candidato A', 'Candidato B', 'Candidato C', 'Candidato D']
votos = np.array([35.822,37.998,18.083,6.150])

cores = ['blue','red','green','yellow']

destaque = (0,0.2,0,0)

plt.pie(votos,explode=destaque,labels=candidatos,colors = cores,autopct='%0.2f%%',shadow=True,startangle=90)

plt.title('Votos Válidos', fontsize = 15,color = 'black')
plt.legend(candidatos,bbox_to_anchor = (1.3,1.3),loc = 'upper right')
plt.axis('equal')
plt.tight_layout()
plt.tick_params(labelsize=10)

plt.show()