# Classificação de uma proposição

import ttg

prop1 = ttg.Truths(['p'],['p or ~p'])
classificacao1 = prop1.valuation()
# print(prop1)
# print(classificacao1)

prop2 = ttg.Truths(['p'],['p and ~p'])
classificacao2 = prop2.valuation()
# print(prop2)
# print(classificacao2)

prop3 = ttg.Truths(['p','q'],['p => q'])
classificacao3 = prop3.valuation()
print(prop3)
print(classificacao3)
