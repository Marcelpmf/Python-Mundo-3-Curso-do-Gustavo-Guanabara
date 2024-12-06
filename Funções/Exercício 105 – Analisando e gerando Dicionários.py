def notas(* num, sit=False):

    dados = dict()
    dados['Total'] = len(num)
    dados['Maior'] = max(num)
    dados['Menor'] = min(num)
    dados['Média'] = sum(num)/len(num)

    if sit:
        if dados['Média'] >= 7:
            dados['Situação'] = str('BOA')

        if 6 >= dados['Média'] or dados['Média'] < 7:
            dados['Situação'] = str('RAZOÁVEL')

        if dados['Média'] < 6:
            dados['Situação'] = str('RUIM')

    print(dados)

resposta = notas(6.5, 3.5, 10, 4.5, sit=True)