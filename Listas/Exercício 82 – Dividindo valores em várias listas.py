lista = list()
pares = list()
impares = list()

while True:

    numero = int(input('Digite um número: '))
    lista.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 == 1:
        impares.append(numero)

    resp = str(input('Deseja continuar? [S/N] ')).upper()

    while resp not in 'SsNn':
        resp = str(input('Inválido. Deseja continuar? [S/N] '))

        if resp in 'Nn':
            break

    if resp in 'Nn':
        break

print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
