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


def leiafloat(num):

    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número real válido.')
        except KeyboardInterrupt:
            print('\nO usuário decidiu não dar mais continuidade ao programa.')
            return 0
        else:
            return n


n1 = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o real {n2}')




