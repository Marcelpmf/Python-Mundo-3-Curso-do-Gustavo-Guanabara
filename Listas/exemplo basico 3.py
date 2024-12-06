a = [2, 3, 5, 6]
b = a[:] # nao cria ligacao e sim uma copia pq ta fatiado :
b[2] = 8 # muda so a da lista B

print(f'Lista A: {a}')
print(f'Lista B: {b}')