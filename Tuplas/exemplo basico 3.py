a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # concatenou as tuplas

print(c)
print(c.count(4)) # ver quantas vezes apareceu algum elemento
print(c.index(8)) # em que posição está o elemento
print(c.index(2, 4)) # em que posição está o elemento a partir da posição evita a repitação (Deslocamento)
print(c.index(5, 1)) # começa da posição 1