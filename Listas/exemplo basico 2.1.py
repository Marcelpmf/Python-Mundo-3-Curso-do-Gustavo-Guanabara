galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(galera[0]) # pega os dois itens do bloco
print(galera[0][0]) # pega so o primeiro item
print(galera)

for p in galera:
    #print(p[0]) # so os nomes (so os primeiros itens)
    #print(p[1]) # so a idade (so os segundos itens)
    print(f'{p[0]} tem {p[1]} anos de idade')