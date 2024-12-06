valores = list()

for contador in range (1, 5):
    valores.append(int(input('Digite um valor: ')))


#valores = [] adicionar valores manuais com append

#valores.append(3)
#valores.append(5)
#valores.append(9)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')