listabrasileirao = ('Botafogo',
         'Palmeiras',
         'Fortaleza',
         'Flamengo',
         'Internacional',
         'São Paulo',
         'Bahia',
         'Cruzeiro',
         'Vasco da Gama',
         'Atlético-MG',
         'Grêmio',
         'Criciúma',
         'Fluminense',
         'EC Vitória',
         'Corinthians',
         'Athletico-PR',
         'Bragantino',
         'Juventude',
         'Cuiabá',
         'Atlético-GO')

print('=-'*50)
print(f'Lista de times: \033[33m{listabrasileirao[0:]}\033[m')

print('=-'*50)
# 5 primeiros colocados ==
print(f'Lista dos 5 primeiros colocados: \033[34m{listabrasileirao[0:5]}\033[m')
print('=-'*50)

# ultimos 4 colocados ==
print(f'Lista dos últimos 4 colocados: \033[31m{listabrasileirao[-4:20]}\033[m')
print('-='*50)

# ordem alfabética ==
print(f'Lista dos times em ordem alfabética: \033[36m{sorted(listabrasileirao)}\033[m')
print('=-'*50)

# Em que posição está time Flamengo ==
flamengoPosicao = listabrasileirao.index('Flamengo') + 1
print(f'O Flamengo está na \033[33m{flamengoPosicao}ª\033[m posição')
