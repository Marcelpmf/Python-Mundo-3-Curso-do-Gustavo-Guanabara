expressao = str(input('Digite a expressão: '))
pilha = []

for simbolo in expressao:

    if simbolo == '(':
        pilha.append('(') # cada vez que tiver um parentese aberto

    elif simbolo == ')':
        if len(pilha) > 0: # nao esta vazio
            pilha.pop() # remove ultimo elemento da pilha
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão é inválida!')