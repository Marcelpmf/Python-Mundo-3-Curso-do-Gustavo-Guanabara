estado = dict()
brasil = list()

for contador in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # TEM QUE FAZER ISSO PARA NAO DAR PROBLEMA SERVE COMO [:] FATIAMENTO

# print(brasil)

#for estado in brasil:
    #print(estado)

#for estado in brasil:
    #for chaves, valores in estado.items():
        #print(f'O campo {chaves} tem valor {valores}')

print(brasil)
print()
for estado in brasil:
    for valores in estado.items():
        print(valores, end=' ')
    print()