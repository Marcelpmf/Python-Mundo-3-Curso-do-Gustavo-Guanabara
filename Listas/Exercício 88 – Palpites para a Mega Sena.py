from random import randint
from time import sleep

jogo = list()
lista = list()
total = 0

print('-'*30)
print('JOGO DA MEGA SENA')
print('-'*30)

quantidade = int(input('Quantos jogos você quer q eu jogue? '))

while total <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    total += 1
print('-='*3, f' SORTEANDO {quantidade} JOGOS ', '-='*3)

for i, l in enumerate(jogo):
    print(f'Jogo {i}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE! >', '-='*5)







