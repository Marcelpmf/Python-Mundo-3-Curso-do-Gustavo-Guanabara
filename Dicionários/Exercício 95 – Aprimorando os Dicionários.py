ficha = dict()
gols = list()
listona = list()

while True:

    ficha['Nome'] = str(input('Nome do jogador: ')).capitalize()
    quantas = int(input(f'Quantas partidas {ficha['Nome']} jogou? '))

    for contador in range(quantas):
        gols.append(int(input(f'Quantos gols na partida {contador}? ')))
    ficha['Gols'] = gols[:]
    ficha['Total'] = sum(gols)
    listona.append(ficha.copy())

    resposta = str(input('Quer continuar? [S/N] ')).upper()

    while resposta not in 'SsNn':
        resposta = str(input(f'{resposta} é inválido. Tente novamente: [S/N] '))
    if resposta in 'Nn':
        break
    ficha.clear() # pra na repetir nas listas
    gols.clear() # mesma coisa

print('-='*30)
print('Cod.nome ', end='')
print(' Gols', end='')
print('     Total')
print('-'*25)

contador = 0
for ficha in listona:
    contador += 1
    print(contador, end='')
    print(ficha['Nome'],end='')
    print(ficha['Gols'], end='')
    print(ficha['Total'])
print('-'*25)

while True:

    resposta2 = int(input('Digite o código do jogador que você quer ver: (999 para)'))
    if resposta2 == 999:
        break
    #if resposta > len(listona):
        #print(f'Erro! Não existe jogador com codigo {resposta2}')
    else:
        print(f'Levantamento do jogador {listona[resposta2]['Nome']}')
        for chaves, valores in enumerate(listona[resposta2]['Gols']):
            print(f'    No jogo {chaves} fez {valores} gols')
    print('-' * 25)
print('Acabou')


