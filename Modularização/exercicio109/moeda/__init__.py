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

def aumentar(n, show=False):
    aumento10 = n * 1.10
    if show:
        return f'R${aumento10:.2f}'.replace('.', ',')
    else:
        return f'{aumento10}'


def diminuir(n, show=False):
    diminuir13 = n * 0.87
    if show:
        return f'R${diminuir13:.2f}'.replace('.', ',')
    else:
        return f'{diminuir13}'

def moeda(n):
    return f'R${n:.2f}'.replace('.',',')