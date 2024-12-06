def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! "{entrada}" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)

# se quiser
def leiaInt(msg):
    valido = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            valido = True
        else:
            print(f'\033[0;31mERRO! Digite um númer inteiro válido!\033[m')
        if valido:
            break
    return valor