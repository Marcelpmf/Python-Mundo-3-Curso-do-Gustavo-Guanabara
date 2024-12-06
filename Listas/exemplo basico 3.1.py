galera = list()
dado = list() # lista secundaria
totalmaior = totalmenor = 0

for contador in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # tem que sempre ser copiado (lista secundaria)
    dado.clear() #

# print(galera)

for pessoa in galera:
    if pessoa[1] > 21:
        print(f'{pessoa[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade')
        totalmenor += 1

print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade')
