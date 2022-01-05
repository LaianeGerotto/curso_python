from datetime import date
ano = int(input('Digite o ano de Nascimento do atleta: '))
idade = date.today().year - ano
print(f'Idade {idade} anos.')
if idade <= 9:
    print('Até 9 anos classificação: MIRIM')
elif idade <= 14:
    print('Até 14 anos classificação: INFANTIL')
elif idade <=19:
    print('Até 19 anos classificação: JUNIOR')
elif idade <= 25:
    print('Até 20 anos classificação: SÊNIOR' )
else:
      print('Acima de 20 anos classificação: MASTER')
