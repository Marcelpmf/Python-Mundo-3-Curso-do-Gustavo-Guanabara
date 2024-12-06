def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano

    if idade < 16:
        return f'Com idade {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com idade {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com idade {idade} anos: VOTO OBRIGATÓRIO.'


ano_nascimento = int(input("Em que ano você nasceu? "))
print(voto(ano_nascimento))

