boletim = dict()

boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input('Média: '))


print(f'Nome é igual: {boletim['nome']}')
print(f'Média é igual a {boletim['media']}')

if boletim['media'] >= 7:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')

