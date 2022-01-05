'''
n = 0
soma = 0
contador = 0
while n != 999:
    n = int(input('Digite um número: '))
    soma += n
    contador +=1
print(f'A soma entre eles é {soma-999}.')
print(f'Foram digitados {contador-1} números.')
'''

#Correção Guanabara
n = 0
contador = 0
soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um número [999 para parar]: ')) #para não precisar alterar o valor das variaveis soma - 999 e contador - 1
print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')