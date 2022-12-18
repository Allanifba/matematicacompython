# Gráfico do tipo barras horizontais

import matplotlib.pyplot as plt

classes = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']
frequencias = [30,25,22,23,40,42,35]

plt.barh(classes,frequencias,color = 'blue',edgecolor = 'red')
plt.title('Ocorrências de Pessoas na Emergência de um Hospital', fontsize = 15, color = 'black')
plt.xlabel('Dia da Semana', fontsize = 10, color = 'black')
plt.ylabel('Número de Ocorrências', fontsize = 10, color = 'black')
plt.tick_params(labelsize=10)

plt.show()