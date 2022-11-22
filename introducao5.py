# Arredondamento de variáveis reais ou float
import math

x = 3.75469

# Arredondamento para baixo = maior inteiro menor ou igual a x
inf_x = math.floor(x)
# print(f'O maior inteiro menor ou igual {x} é igual a {inf_x}.')

# Arredondamento para cima = menor inteiro maior ou igual a x
sup_x = math.ceil(x)
# print(f'O menor inteiro maior ou igual {x} é igual a {sup_x}.')

# Arredondamento padrão para o inteiro próximo
arred_x = round(x)
# print(f'O arredondamento padrão de {x} para o inteiro mais próximo é {arred_x}.')

# Arredondamento padrão com n casas decimais
n_casas = 3
arred_xn = round(x,n_casas)
print(f'O arredondamento padrão de {x} com {n_casas} decimais é {arred_xn}.')
