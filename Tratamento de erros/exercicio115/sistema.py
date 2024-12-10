from exercicio115.lib.interface import *
from exercicio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
#if arquivoExiste(arq):
    #print('Arquivo encontrado com sucesso')
#else:
    #print('Arquivo não encontrado')
    #criarArquivo(arq)

if not arquivoExiste(arq): # se nao existir, cria
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)


