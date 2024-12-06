extenso = ('Zero', 'Um',
                   'Dois',
                   'Três',
                   'Quatro',
                   'Cinco',
                   'Seis',
                   'Sete',
                   'Oito',
                   'Nove',
                   'Dez',
                   'Onze',
                   'Doze',
                   'Treze',
                   'Catorze',
                   'Quinze',
                   'Desesseis',
                   'Dezessete',
                   'Dezoito',
                   'Dezenove',
                   'Vinte')



numero = int(input('Digite um numero entre 0 e 20: '))

# intervalo = numero => 0 and numero <= 20

while True:

    if numero >= 0 and numero <= 20:
        print(f'Você digitou o número {extenso[numero]}')
        break

    else:
        numero = int(input('Invalido. Digite novamente um numero entre 0 e 20: '))



