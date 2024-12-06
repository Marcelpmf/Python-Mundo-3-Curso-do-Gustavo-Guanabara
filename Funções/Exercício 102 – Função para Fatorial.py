def fatorial(n,show=False):

    """

    :param n: Número
    :param show: Mostrar ou não o cálculo (True mostra e False não mostra)
    :return: Retorna o resultado
    """

    fat = 1
    for contador in range(n, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        fat *= contador
    return fat




resultado = fatorial(5,show=True)
print(resultado)

