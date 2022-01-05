from datetime import date
print('-'*49)
print(" Verificação para Alistamento do Serviço Militar ")
print('-'*49)
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
print(f'Quem nasceu em {ano} tem {idade} anos atualmente.\n Observações:')
if idade < 18:
    print('- Você não tem idade alistar!')
    print(f'- Faltam {18 - idade} ano(s).')
elif idade == 18:
    print('- Você tem que se alistar IMEDIATAMENTE!.')
elif idade > 18:
    print('- Você já passou da idade de se Alistar')
    print(f'- Já se passaram {idade - 18} ano(s) para o Alistamento.')