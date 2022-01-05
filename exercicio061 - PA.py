'''
print('=='*15)
print('  Progressão Aritmética - PA')
print('=='*15)
termo1 = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))
print('')
print('Os 10º primeiros termos da PA:')
pa = termo1 + (10 - 1) * razao
contador = termo1
while contador < (pa+razao):
    print(contador, end=' -> ')
    contador += razao
print('Acabou')
'''
#Correção Guanabara
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1
print('FIM')
