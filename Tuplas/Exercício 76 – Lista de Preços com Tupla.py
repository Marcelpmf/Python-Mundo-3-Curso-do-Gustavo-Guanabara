listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Compasso', 9.99, 'Mochila', 120.90, 'Canetas', 15.50, 'Transferidor', 4.20)

contador = 0

print('-'*40)
print(f'{"Listagem de preços":^40}') # 40 espaços centralizados
print('-'*40)

for contador in range (0, len(listagem)):

    if contador % 2 == 0: # se posicao for par (todos os produtos sao na posicao par 0 = lapis, 2 == borracha...
        print(f'{listagem[contador]:.<30}', end = '') # pontos aninhados a esquerda e nao quebrar linha

    else:
        print(f'R${listagem[contador]:>7.2f}') # aninhar para esquerda e 2 casas decimais


#for contador in range(0, len(listagem), 2):
    #print(f'{listagem[contador]:.<30}R${listagem[contador + 1]:7.2f}')

