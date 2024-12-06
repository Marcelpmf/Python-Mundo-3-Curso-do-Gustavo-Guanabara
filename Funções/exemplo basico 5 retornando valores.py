def somar(a=0,b=0,c=0): # = 0 é um parametro opcional ou seja se faltar vai dar no mesmo

    """
    -> Faz a soma de tres valores e mostra o resultado em tela.
    :param a: Primeiro valor
    :param b: Segundo Valor
    :param c: Terceiro Valor
    :return: retorna a soma
    """
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')

