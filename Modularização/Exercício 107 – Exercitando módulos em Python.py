from exercicio107 import moeda

preco = float(input('Digite um preço: R$'))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(preco)}')
print(f'Reduzindo 13%, temos R${moeda.diminuir(preco)}')