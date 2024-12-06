def somar(a=0,b=0,c=0): # = 0 é um parametro opcional ou seja se faltar vai dar no mesmo

    """
    -> Faz a soma de tres valores e mostra o resultado em tela.
    :param a: Primeiro valor
    :param b: Segundo Valor
    :param c: Terceiro Valor
    :return:
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4) # pq n recebu C ent caso n tenha vai valer igual a 0
somar()
somar(b = 5, c = 3) 
