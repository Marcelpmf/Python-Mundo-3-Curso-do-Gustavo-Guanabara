def area():
    largura = float(input('COMPRIMENTO (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    a = largura * comprimento
    print(f'A área de seu terreno {largura}x{comprimento} é de {a}m².')

def cabecalho():
    print()
    print('CALCULO DA AREA DE TERRENOS')
    print('-'*30)
    

cabecalho()
area()




