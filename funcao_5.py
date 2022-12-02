# Função aplicada a vários valores (diversos)

x = [1,3,8]
i = 0
while i < len(x):
    def f(x):
        return x**2-1
    print(f'f({x[i]}) = {f(x[i])}')
    i = i + 1