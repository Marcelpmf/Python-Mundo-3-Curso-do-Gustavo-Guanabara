matriz = []
temporaria = []

for contador in range (0,3):
    temporaria.append(int(input(f'Digite um valor para [{contador}, 0]: '))) # vai fazer 3 vezes de cada append
    temporaria.append(int(input(f'Digite um valor para [{contador}, 1]: ')))
    temporaria.append(int(input(f'Digite um valor para [{contador}, 2]: ')))
    matriz.append(temporaria[:])
    temporaria.clear()


print(f'[  {matriz[0][0]}  ]', end='')
print(f'[  {matriz[0][1]}  ]', end='')
print(f'[  {matriz[0][2]}  ]', end='')
print()
print(f'[  {matriz[1][0]}  ]', end='')
print(f'[  {matriz[1][1]}  ]', end='')
print(f'[  {matriz[1][2]}  ]', end='')
print()
print(f'[  {matriz[2][0]}  ]', end='')
print(f'[  {matriz[2][1]}  ]', end='')
print(f'[  {matriz[2][2]}  ]', end='')
