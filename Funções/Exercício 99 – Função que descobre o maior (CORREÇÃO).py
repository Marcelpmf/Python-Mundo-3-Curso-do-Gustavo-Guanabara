from time import sleep

def maior(* num):

    contador = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.2)

        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1

    print(f'Foram informados {contador} valores ao todo')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
