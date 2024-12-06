lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batatas')

for contador in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]}')
print('Comi demais')

# x precisar da posicao do alimento
#for contador in range (0, len(lanche)):
    #print(f'Eu vou comer {lanche[contador]} na posicao {cont}')
#print('Comi demais')


# x mesma coisa de cima
#for pos, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} na posicao {pos}')


# x basico classico
#for comida in lanche:
    #print(f'Eu vou comer {comida}')
#print('Comi demais')

print(sorted(lanche)) # organiza em ordem alfabetica