def metade(n, show=False):
    divisao = n / 2
    if show:
        return f'R${divisao:.2f}'.replace('.', ',')
    else:
        return f'{divisao}'

def dobro(n, show=False):
    multi = n * 2
    if show:
        return f'R${multi:.2f}'.replace('.', ',')
    else:
        return f'{multi}'

def aumentar(n, taxa=0, show=False):
    aumento = n + (n * taxa / 100)
    if show:
        return f'R${aumento:.2f}'.replace('.', ',')
    else:
        return f'{aumento}'


def diminuir(n, taxa=0, show=False):
    diminui = n - (n * taxa / 100)
    if show:
        return f'R${diminui:.2f}'.replace('.', ',')
    else:
        return f'{diminui}'

def moeda(n):
    return f'R${n:.2f}'.replace('.',',')


def resumo(n, aumentop, diminuirp):

    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)

    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aumentop}% de aumento: \t{aumentar(n, aumentop, True)}')
    print(f'{diminuirp}% de redução: \t{diminuir(n, diminuirp, True)}')
    print('-' * 30)