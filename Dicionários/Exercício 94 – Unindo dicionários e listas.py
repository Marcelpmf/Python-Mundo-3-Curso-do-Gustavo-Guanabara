pessoas = dict()
lista = list()
mulheres = list()
total = media = 0

while True:

    pessoas['Nome'] = str(input('Nome: ')).capitalize()

    sexo = str(input('Sexo: [M/F] ')).upper()
    pessoas['Sexo'] = sexo

    idade = int(input('Idade: '))
    total += idade
    pessoas['Idade'] = idade

    if pessoas['Sexo'] in 'F':
        mulheres.append(pessoas['Nome'])


    resposta = str(input('Quer continuar? [S/N] ').upper())
    lista.append(pessoas.copy())

    while resposta not in 'SsNn':
        resposta = str(input('Inválido. Tente novamente: [S/N] '))

    if resposta in 'Nn':
        break


media = total / len(lista)

print('-='*30)
print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média é de {media} anos')
print(f'- As mulheres cadastradas foram: {mulheres}')
print(f'- Lista das pessoas que estão acima da média da idade ({media:5.2f}): ')
print()

for pessoas in lista:
    if pessoas['Idade'] >= media:
        for chaves, valores in pessoas.items():
            print(f'{chaves} = {valores}; ', end='')
        print()



