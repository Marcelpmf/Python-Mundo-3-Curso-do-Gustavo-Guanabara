import datetime

ficha = dict()

ficha['Nome'] = str(input('Nome: ').capitalize())

ano_atual = datetime.date.today()
ano = int(input('Ano de nascimento: '))
idade = ano_atual.year - ano
ficha['Idade'] = idade

ficha['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if ficha['ctps'] != 0:
    ficha['Contratação'] = int(input('Ano de contratação: '))
    ficha['Salário'] = float(input('Salário: R$ '))
    ano_aposenta = ficha ['Contratação'] + 35

    # pega o ano_aposenta subtrai pela data atual e depois soma com a idade
    ficha['Aposentadoria'] = ano_aposenta - ano_atual.year + ficha['Idade']

print('-='*50)
print(ficha)

for chaves, valores in ficha.items():
    print(f'{chaves} tem o valor {valores}')
