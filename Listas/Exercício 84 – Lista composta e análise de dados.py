pessoas = [] # principal
temporario = []
menor = maior = 0

while True:

    #nome = str(input('Nome: ')).capitalize() SE DEIXAR ASSIM TEM Q BOTAR GAMBIARRA DE MENOR = 999
    #peso = float(input('Peso: '))
    #pessoas.append([nome, peso])

    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < maior:
            menor = temporario[1]

    pessoas.append(temporario[:])
    temporario.clear()

    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
    while resp not in 'SsNn':
        resp = str(input('Inválido. Tente novamente: [S/N] '))


#for p in pessoas:
    #if p[1] == 0:
        #maior = menor = p[1]
    #else:
        #if p[1] > maior:
            #maior = p[1]
        #if p[1] < menor:
            #menor = p[1]

print('-='*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for nPESO in pessoas:
    if nPESO[1] == maior:
        print(f'[{nPESO[0]}] ', end='')

print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for nPESO in pessoas:
    if nPESO[1] == menor:
        print(f'[{nPESO[0]}] ', end='')


