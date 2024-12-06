# algo.append('oi') -> adiciona um novo item a lista
# algo.insert(0,'oi') -> adiciona uma posicao no zero e aumenta os demais +1
# del algo[3] -> deleta o item na posicao 3
# algo.pop(3) -> mesma coisa mas geralmente usa pra tirar o ultimo e redirecionam os outros ou algo.pop() -> ultimo
# algo.remove('oi') -> voce indica o valor e nao a posicao e redirecionam os outros


# if 'oi' in algo
#   algo.remove('oi')

# valores = list(range(4, 11)) -> declara uma lista com valores de 4 ate 10 ou (4,11,2) pulando de 2

# valores = [8,2,5,4,9,3,0]
#   valores.sort() -> ordena os valores
#   valores.sort(reverse=True) -> ordem inversa
#   len(valores) -> tamanho da lista

num = list(range(0,11))
# num.append(11) # adicionar valor
# num.insert(2,0) # inserir o numero 0 na posicao 2
# num.pop() # tira o ultimo numero

#if 4 in num:  # procurar um valor na lista e apagar ele
    #num.remove(4)
#else:
    #print('Não achei')
#print(num)

print(f'Essa lista tem {len(num)} elementos')
