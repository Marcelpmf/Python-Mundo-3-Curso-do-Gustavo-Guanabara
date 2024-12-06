# from uteis import fatorial, dobro
#import uteis # maneira mais recomendada
from uteis import numeros

num = int(input('Digite umm número: '))
fat= numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')