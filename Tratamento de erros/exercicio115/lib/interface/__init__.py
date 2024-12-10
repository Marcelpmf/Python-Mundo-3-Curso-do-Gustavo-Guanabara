def leiaint(num):

    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('\nO usuário decidiu não dar mais continuidade ao programa.')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opc = leiaint('\033[33mSua opção: \033[m')
    return opc



