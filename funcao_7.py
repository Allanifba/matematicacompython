# Construindo uma função imputável e gerando um arquivo do tipo .exe
# Pode ser necessário instalar o pacote pyinstaller >>> No terminal digite: pip install pyinstaller
# Pode ser necessário instalar o módulo numpy >>> No terminal digite: pip install numpy
# Para construir um executável digite, no terminal, o comando: pyinstaller --onefile nome_do_arquivo.py

import math
import numpy as np

while True:
    y = input('Digite a função: ')
    entradas = eval(input('Digite as entradas separadas por vírgula: '))
    print('Os valores da função são dados a seguir: ')

    i = 0
    while i < len(entradas):
        x = entradas[i]
        def f(x):
            return eval(y)
        print(f'f({x}) = {f(x)}')
        i = i + 1
