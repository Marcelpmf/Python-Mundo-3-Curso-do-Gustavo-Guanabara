teste = list()

teste.append('Gustavo')
teste.append(40)

galera = list()

galera.append(teste[:]) # tem que ter copia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)