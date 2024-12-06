valores = list()
resp = ''

while resp != 'N':

    numero = int(input('Digite um valor: '))

    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Número duplicado, nao vou adicionar')

    resp = str(input('Deseja continuar? [S/N] ')).upper()

    while resp not in 'SsNn':
        resp = str(input('Invalido Tente novamente: [S/N] '))

print('-='*30)
valores.sort()
print(f'Você digitou os valores {valores}')

