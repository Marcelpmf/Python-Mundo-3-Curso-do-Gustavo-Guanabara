from time import sleep

c =     ('\33[m',           #0 sem cor
        '\33[30;41m',       #1 vermeho
        '\33[33;44m',       #2 amarelo fundo azul
        '\33[35;43m',       #3 roxo fundo amarelo
        '\33[30;42m',       #4 branco fundo verde
        '\033[7m')          #5 branco

def ajuda(com):
    titulo(f'Acessando o manual do comando {com}', 4)
    print(c[5])
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0], end='')



comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)