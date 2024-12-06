lista = list()

while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)

    resp = str(input('Deseja continuar? [S/N] ')).upper()

    while resp not in 'SsNn':
        resp = str(input('Inválido. Tente novamente: [S/N] '))

        if resp in 'Nn':
            break

    if resp in 'Nn':
        break


print('-='*30)
print(f'Você digitou os números: {lista}')

print(f'Ao todo são {len(lista)} elementos')

lista.sort(reverse=True)
print(f'Números em ordem decrescente: {lista}')

if 5 in lista:
    print('O número 5 ESTÁ na lista')
else:
    print('O número 5 NÃO está na lista')

