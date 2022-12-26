# Construção de tabelas verdade

import ttg

tabela1 = ttg.Truths(['p','q'],['p => q'])
# print(tabela1)
tabela2 = ttg.Truths(['p','q'],['p or q'])
# print(tabela2)
tabela3 = ttg.Truths(['p','q'],['p and q','p or q','p => q','p = q'])
# print(tabela3)
tabela4 = ttg.Truths(['p','q','r','s'],['((p and q) => ~r) = (p or s)'])
print(tabela4)
