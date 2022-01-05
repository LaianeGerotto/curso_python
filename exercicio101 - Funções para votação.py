# def votação(ano):
#     from datetime import datetime #colocar dentro da função para economizar memoria
#     idade = datetime.now().year - ano
#     if idade < 16:
#         print(f'Com {idade} anos: NÃO VOTA.')
#     if idade >= 18 and idade <= 65:
#         print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
#     if idade >= 16 and idade < 18 or idade > 65:
#         print(f'Com {idade} anos: VOTO OPCIONAL.')
#     return ano
# print('--'*20)
# ano = int(input('Em que ano você nasceu? '))
# votação(ano)

#Correção Guanabara
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16<= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))