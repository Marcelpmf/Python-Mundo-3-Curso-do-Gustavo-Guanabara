# sempre que ficar () é tupla

#numeros = (int(input('Digite o 1º numero: ')),
           #int(input('Digite o 2º numero: ')),
           #int(input('Digite o 3º numero: ')),
           #int(input('Digite o 4º numero: ')))

# ou

numeros = tuple(int(input(f'Digite o {contador}º número: '))for contador in range(1, 5))


print(f'Você digitou os números {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram ', end=' ')

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')



