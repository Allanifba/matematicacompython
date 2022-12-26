# Construção de tabela verdade
# No terminal use o comando 'pip install truth-table-generator' para instalar o pacote de geração de tabelas verdade

import ttg
                                                    # Exemplo de inserção de dados:
a = input('Digite as proposições simples: ')        # p,q -> ['p','q']
b = input('Digite as proposições compostas: ')      # p -> q -> ['p => q']

resultado = ttg.Truths(eval(a),eval(b))
print(resultado)
