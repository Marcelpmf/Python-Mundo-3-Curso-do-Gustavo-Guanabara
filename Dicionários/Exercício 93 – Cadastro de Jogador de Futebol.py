ficha = dict()
gols = list()
quantidade = 0

ficha['Nome'] = str(input('Nome do jogador: ')).capitalize()
ficha['Partidas'] = int(input(f'Quantas partidas {ficha['Nome']} jogou? '))


for contador in range  (ficha['Partidas']):
    numero = int(input(f'Quantos gols na partida {contador+1}? '))
    quantidade += numero
    gols.append(numero)
    ficha['Gols'] = gols
    ficha['Total'] = quantidade

print('-='*30)

print(ficha)
print('-='*30)

for chaves,valores in ficha.items():
    print(f'o campo {chaves} tem valor {valores}')
print('-='*30)

print(f'O jogador {ficha['Nome']} jogou {ficha['Partidas']} partidas. ')

for contador in range(ficha['Partidas']):
        print(f'   => Na partida {contador+1}, fez {ficha['Gols'][contador]} gols.')
print(f'Foi um total de {ficha['Total']} gols.')


