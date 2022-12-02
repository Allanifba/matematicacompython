# Função aplicada a vários valores igualmente espaçados

a = 0
b = 1
delta = 0.1
while a <= b:
    def f(x):
        return x**2-1
    print(f'f({round(a,2)}) = {round(f(a),1)}')
    a = a + delta