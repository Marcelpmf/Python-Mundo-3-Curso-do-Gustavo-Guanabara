pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.keys()) # cada chave
#print(pessoas.values()) # cada valor
#print(pessoas.items()) # tudo uma lista e as tuplas para cada coisinha ()

# del pessoas[sexo] # da pra tirar o item e ele tira tudo (apaga o elemento)
# pessas['nome'] = 'leandro' # troca
# pessoas['peso'] = 98.5 # adiciona um novo elemento (FAZ A MESMA COISA DO APPEND) 

#for chave in pessoas.keys(): # mostra as chaves (os nomes)
    #print(chave)

#for valores in pessoas.values(): # os valores (os valores de cada nome)
    #print(valores)

for chaves, valores in pessoas.items(): # faz a mesma coisa que o enumerate
    print(f'{chaves} = {valores}')