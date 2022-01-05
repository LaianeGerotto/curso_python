from datetime import date
ano = int(input('Digite um ano ou 0 (zero) para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO Bissexto!')