from time import sleep

def contador(inicio, fim, passo):

    if passo < 0: # ESSA VALIDAÇÃO TEM QUE SER AQUI EM CIMA PARA DAR CERTINHO NA MENSAGEM
        passo *= -1  # TRANSFORMA EM POSITIVO ISSO É UMA MULTIPLICAÇÃO

    if passo == 0:
        passo = 1

    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print('FIM!')

    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print('FIM!')



contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)