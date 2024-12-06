def ficha(jog='<desconhecido>', gol=0): # por padrão pra deixar opcional tem q deixar assim
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
n = str(input("Nome do Jogador: "))
g = str(input("Número de Gols: "))

if g.isnumeric(): # ver se é númerico
    g = int(g) # g vira int
else:
    g = 0

if n.strip() == '': # se tirou todos os espaços e mesmo assim ficou vazio
    ficha(gol=g) # passa somente a quantidade de gols (g) pra a func ficha(gol) SE tiver vazio
else:
    ficha(n,g) # passa o gol e o nome para a ficha (FAZ A CHAMADA)


# solução 2

#def ficha(nome=0, gols=0):
    #nome = input('Nome: ')
    #gols = input('Gols: ')
    #if nome == 0 or nome == '':
        #nome = '<desconhecido>'
    #if gols.isnumeric():
        #gols = int(gols)
    #else:
        #gols = 0
    #print(f'O jogador {nome} fez {gols} gols no  campeonato.')


#ficha()


# solução 3 (MAIS ENTENDIVEL)

#def ficha(nome, gols):
    #if not nome:
        #nome = '<desconhecido>'
    #if gols.isnumeric():
        #gols = int(gols)
    #else:
        #gols = 0
    #return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


#nome = str(input('Nome do jogador: ')).strip()
#gols = str(input('Número de gols: '))
#print(ficha(nome, gols))

