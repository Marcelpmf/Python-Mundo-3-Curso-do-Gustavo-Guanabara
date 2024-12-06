def leiaint(num):

    while True:

        if num.isnumeric():
            print(f'Você acabou de digitar o número {num}.')
            break
        else:
            print(f'\033[33mErro! {num} não é válido. Digite um número inteiro.\033[m')
            num = str(input('Digite um número: '))


leiaint(str(input('Digite um número: ')))

