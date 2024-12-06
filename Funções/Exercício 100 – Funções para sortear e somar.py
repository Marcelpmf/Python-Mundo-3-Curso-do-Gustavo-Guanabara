import random

def sorteia():
    print(f'Sorteando 5 valores da lista: {sortear} ', end='')
    print('PRONTO!')

def somapar():

    pares = list()
    somapares = 0
    for valores in sortear:
        if valores % 2 == 0:
            somapares = valores + somapares
            pares.append(valores)

    print(f'Somando os valores pares de {sortear}, temos {somapares}')


numeros = list()
contador = 0

while contador != 12:
    num = int(random.randint(1,12))
    numeros.append(num)
    contador += 1

sortear = random.sample(numeros, 5)
print(f'Lista --> {numeros}')
print('-='*30)
sorteia()
somapar()




