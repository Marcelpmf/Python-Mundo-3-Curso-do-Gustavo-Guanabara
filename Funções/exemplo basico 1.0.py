def contador(i,f,p):
    """
    :param i: inicio
    :param f: final
    :param p: passo
    :return: sem retorno
    Função criada por anteteguemon
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador)