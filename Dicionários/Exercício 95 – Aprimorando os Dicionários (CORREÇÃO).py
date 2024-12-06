jogador = dict()
partidas = list()
time = list()

while True:

    jogador.clear()  # TEM QUE APAGAR PQ A CADA LAÇO ELE VAI LER UM NOVO
    jogador['nome'] = str((input('Nome do jogador: '))).capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear() # ESVAZIAR ESSE TAMBEM

    for contador in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {contador+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print('cod. ', end='')
for elemento in jogador.keys():
    print(f'{elemento:<15}', end='')
print()
print('-' * 40)

for chaves, valores in enumerate(time):
    print(f'{chaves:>3} ', end='') # esse :> é pra centralizar a direita
    for dado in valores.values():
        print(f'{str(dado):<15}', end='') # esse :< 15 é pra aninhar a direita
    print()
print('-' *40)

while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for indice, gols in enumerate(time[busca]['gols']):
            print(f'    No jogo {indice+1} fez {gols} gols')
    print('-' * 40)

print('<< VOLTE SEMPRE >>')


