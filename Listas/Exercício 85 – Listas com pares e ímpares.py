valores = list() # []
pares = list() # []
impares = list() # []

for contador in range (0, 7):
    numero = int(input(f'Digite o {contador + 1}º número: '))
    valores.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('-='*30)
pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impares}')


