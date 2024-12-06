tupla = ('Aprender', 'Olhar', 'Animal', 'Chifres', 'Borboletas', 'Peixes', 'Python', 'Bola', 'Arvore', 'Multa')

for contador in tupla:
    print(f'\nNa palavra {contador} temos ', end='')

    for letra in contador:
        if letra.lower() in 'aeiou': # vogais
            print(letra, end=' ')