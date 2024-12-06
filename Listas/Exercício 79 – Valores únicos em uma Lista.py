lista = list()

for contador in range (0, 5):
    numero = int(input('Digite um numero: '))

    if contador == 0 or numero > lista[-1]:  # se primeiro valor for o maior ou se o numero for maior que o ultimo
        lista.append(numero)
        print('Adicionado ao final da lista')


    else:
        posicao = 0
        while posicao < len(lista): # posicao for menor que o tamanho de lista (0 ate ultima posicao)
            if numero <= lista[posicao]: # ver se o numero é maior ou igual a ele (posicao especifica)
                lista.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1


print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')