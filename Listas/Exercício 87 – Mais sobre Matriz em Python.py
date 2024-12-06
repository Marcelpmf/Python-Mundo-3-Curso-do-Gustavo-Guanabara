matriz = [[0,0,0], [0,0,0], [0,0,0]]
somapares = pares = somaTerceiraColuna = maiorValorSegundaLinha = 0


for linha in range (0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print(matriz)
print('-='*30)

for linha in range (0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[coluna][linha] % 2 == 0:
            somapares += matriz[coluna][linha]
            pares += 1
    print()

print('-='*30)

#somaTerceiraColuna = matriz[0][2] + matriz [1][2] + matriz [2][2]
for linha in range(0,3):
    somaTerceiraColuna += matriz[linha][2]

for coluna in range(0,3):
    if coluna == 0:
        maiorValorSegundaLinha = matriz[1][coluna]
    elif matriz[1][coluna] > maiorValorSegundaLinha:
        maiorValorSegundaLinha = matriz[1][coluna]

# terceira coluna = [0][2], [1][2], [2][2]
# segunda linha = [1][0], [1][1], [1][2]

print(f'A soma dos valores pares ({pares} valores) é {somapares}')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é {maiorValorSegundaLinha}')