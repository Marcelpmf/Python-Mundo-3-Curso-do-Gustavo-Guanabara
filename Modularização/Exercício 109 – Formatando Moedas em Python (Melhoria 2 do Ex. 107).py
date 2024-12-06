from exercicio109 import moeda

# True mostra o numero formatado e False mostra o numero normal
preco = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, True)}')