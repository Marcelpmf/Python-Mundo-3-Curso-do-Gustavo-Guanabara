valores = list()
maior = menor = 0
posicao_maior = []
posicao_menor = []

for contador in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {contador}: ')))

# OPC 1
    #if contador == 0:
        #maior = menor = valores[contador]
    #else:
        #if valores[contador] > maior:
            #maior = valores[contador]
        #if valores[contador] < menor:
            #menor = valores[contador]


# OPC 2
#for posicao, valor in enumerate(valores):
    #if valores == max(valores):
        #posicao_maior.append(posicao)
    #if valor == min(valores):
        #posicao_menor.append(posicao)

print('=-'*20)

print(f'Você digitou os valores {valores}')

# OPC 3
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{posicao}... ', end='')

print()

print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{posicao}... ', end='')




