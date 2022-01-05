n = 0
opcao = "SN"

escrita = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
                'Cinco','Seis', 'Sete','Oito', 'Nove',
                'Dez', 'Onze', 'Doze','Treze','Quatorze',
                'Quinze','Dezesseis','Dezessete', 'Dezoito',
                'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número 0 e 20: '))
    if n >= 0 and n <= 20:
        break
    print('Tente novamente.', end=" ")

print(f'Você digitou o número {escrita[n]}.')















'''
#Correção Guanabara

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco','Seis', 'Sete','Oito', 'Nove', 
        'Dez', 'Onze', 'Doze','Treze','Quatorze',
        'Quinze','Dezesseis','Dezessete', 'Dezoito', 
        'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o numero {cont[num]}')
'''