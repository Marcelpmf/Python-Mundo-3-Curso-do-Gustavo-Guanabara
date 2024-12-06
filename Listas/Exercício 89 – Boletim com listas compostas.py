ficha = list()

while True:

    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2

    ficha.append([nome, [nota1, nota2], media])

    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        break
    while resposta not in 'SsNn':
        resposta = str(input('Inválido. Tente novamente: [S/N] '))

print(ficha)
print('-=' * 30)
print('No.', end='')
print('  NOME ', end='')
print('  MEDIA')
print('-'*25)
for contador in range(len(ficha)):
    print(contador , end='')
    print(f'    {ficha[contador][0]} ', end='')
    print(f'    {ficha[contador][2]}')
print('-'*25)

while True:
    resposta2 = int(input('Digite qual aluno voce quer ver as notas: (999 interrompe) '))
    if resposta2 == 999:
        print('FINALIZANDO...')
        break

    print(f'As notas de {ficha[resposta2][0]} são {ficha[resposta2][1]}')
    print('-' * 30)



