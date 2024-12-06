from random import sample
from time import sleep

lista = list(range(1,61))

print('-='*15)
print('     JOGO DA MEGA SENA       ')
print('-='*15)

jogos = int(input('Quantos jogos você quer jogar: '))

for j in range(1, jogos + 1):
    bilhete = sample(lista,6)
    sleep(1)
    print(f'Jogo {j}: {sorted(bilhete)}')