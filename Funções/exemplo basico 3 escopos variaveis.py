def teste():
    x = 8 # VARIAVEL LOCAL
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2 # VARIAVEL GLOBAL
print(f'No programa principal, n vale {n}')
teste()

