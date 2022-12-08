# Aba 1: nomeada como main1
def f(x):
    return x**2

def g(x):
    return 2*x-1

def h(x):
    return 3**x

# Aba 2: nomeada como main2

from main1 import f,g,h

while True:
    x = float(input('Digite a entrada: '))
    print(f(x))         # x**2
    print(g(x))         # 2*x-1
    print(h(x))         # 3**x