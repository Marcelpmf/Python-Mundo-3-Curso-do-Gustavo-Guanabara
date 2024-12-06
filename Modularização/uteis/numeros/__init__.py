def fatorial(n):

    f = 1 # valor de retorno (tem q ser por 1 por conta de que qualquer num x 0 é igual a 0)
    for contador in range (1, n+1): # n + 1 pq n é 0
        f *= contador
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n *3