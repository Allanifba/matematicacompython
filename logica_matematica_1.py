# Valor lógico de uma proposição usando os operadores not, and e or

# Atribuindo valores lógicos
p = True
q = False
r = False

# Operador not (negação ou '~')
s = not(p)      # ~V = F
# print(f'O valor lógico de s é {s}.')

# Conectivo and (conjunção ou 'e')
t = p and q     # V e F = F
# print(f'O valor lógico de t é {t}.')

# Conectivo or (disjunção ou 'ou')
u = p or r      # V ou F = V
# print(f'O valor lógico de u é {u}.')

# Cálculo do valor lógico de uma proposição composta mais complexa
v = (p and q) or (r and not(p)) # (V e F) ou (F and ~V) = F ou (F and F) = F ou F = F
print(f'O valor lógico de v é {v}.')
