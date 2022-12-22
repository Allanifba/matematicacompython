# Gerando um arquivo de saída do tipo txt
quadrado = open('quadrado.txt', 'w') #Cria um arquivo do tipo txt em branco

n = float(input('Digite um número para ver o seu quadrado: '))
print(f'O quadrado de {n} é {n**2}.')
quadrado.write(f'O quadrado de {n} é {n**2}.') #Escreve no arquivo txt de forma semelhante ao comando print
input('Digite Enter para sair!')
