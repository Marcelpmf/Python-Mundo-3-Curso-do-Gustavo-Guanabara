from time import sleep

def contador():
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(0,11,1):
        print(c,end=' ')
        sleep(0.2)
    print('FIM!')

    print('-='*20)
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.2)
    print('FIM!')

def escolher():
    print('-='*20)
    print('Agora é sua vez de personalizar a contagem! ')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

#def iniciomaiorquefim():
    if inicio > fim:
        for c in range(inicio, fim, -passo):
            print(c, end=' ')
            sleep(0.2)
        print('FIM!')

        if passo < 0: # AJEITAR
            for c in range(inicio, fim, passo):
                print(c, end=' ')
                sleep(0.2)
            print('FIM!')

#def passonegativo():
    #elif passo < 0:
        #for c in range(inicio, fim, -passo):
            #print(c, end=' ')
            #sleep(0.2)
        #print('FIM!')

#def passozero():
    elif passo == 0:
        for c in range(inicio, fim, passo+1):
            print(c, end=' ')
            sleep(0.2)
        print('FIM!')

#def passozeroeiniciomairquefim():
    elif inicio > fim and passo == 0: # AJEITAR
        for c in range(inicio, fim, -1):
            print(c, end=' ')
            sleep(0.2)
        print('FIM!')

#def normal():
    else:
        for c in range(inicio, fim, passo):
            print(c, end=' ')
            sleep(0.2)
        print('FIM!')


contador()
escolher()