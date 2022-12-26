# Valor lógico de uma proposição usando os operadores condicional e bicondicional

# Atribuindo valores lógicos
p = True
q = False
r = False

# Operador condicional (p -> q = not(p) or r)
s = not(p) or q     #p -> q = V -> F = F
t = not(q) or r     #q -> r = F -> F = V
# print(f'O valor lógico de s é {s}.')
# print(f'O valor lógico de t é {t}.')

# Operador bicondicional (p <-> q = p==q)
u = p == q      # p <-> q = V <-> F = F
v = q == r      # q <-> r = F <-> F = V
# print(f'O valor lógico de u é {u}.')
# print(f'O valor lógico de v é {v}.')

# Juntando tudo: ((p -> q) and (q or r)) <-> (q -> p)
z = ((not(p) or q) and (q or r)) == (not(q) or p)   # ((p -> q) and (q or r)) <-> (q -> p)
print(f'O valor lógico de z é {z}.')                # ((V -> F) and (F or F)) <-> (F -> V)
                                                    # (F and F) <-> V = F <-> V = F