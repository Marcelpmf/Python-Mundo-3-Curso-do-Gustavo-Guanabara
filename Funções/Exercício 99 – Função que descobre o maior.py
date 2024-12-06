def maior(* num):
    print('-='*20)
    print('Analisando os valores passados...')
    tamanho = len(num)
    print(f'{num} foram informados {tamanho} valores ao todo')

    contador = maiorv = 0

    for valores in num:
        if contador == 0:
            maiorv = valores

        if valores > maiorv:
            maiorv = valores

        contador += 1


    print(f'O maior valor foi o {maiorv}')


maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

