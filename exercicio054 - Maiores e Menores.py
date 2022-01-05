from datetime import date
soma = 0
contador2 = 0
contador3 = 0
for contador in range(0,3):
    ano = int(input(f'Digite o ano de nascimento da {contador +1}ª pessoa: '))
    idade = date.today().year - ano
    #print(idade)
    if idade >= 21:
        contador2 = contador2 + 1
        soma += contador2
    elif idade < 21:
        contador3 = contador3 + 1
print(f'Maiores de 21 anos são {contador2} pessoas.')
print(f'Menores de 21 anos são {contador3} pessoas.')
