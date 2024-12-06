from random import sample

# Converter numeros para a tupla botar randint pra cada numero (1,10)
# fazer um numero == (randint(1,10)), ()...
tuplaleatoria = tuple(sample(range(10), 5))

print(f'Os valores sorteados foram: {tuplaleatoria}')

# max e min

print(f'O maior valor foi {max(tuplaleatoria)}')
print(f'O menor valor foi {min(tuplaleatoria)}')

