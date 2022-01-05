'''
n = 0
contador = 0
opcao = 'Ss'
soma = 0
maior = False
menor = False
while opcao != 'N':
    n = int(input('Digite um número: '))
    opcao = str(input('Deseja continuar [S] sim e [N] não: ')).upper()
    contador += 1
    soma += n
    media = soma / contador
    if n > maior or maior is False:
        maior = n
    if n < menor or menor is False:
        menor = n
print(f'Você digitou {contador} números.')
print(f'Soma de todos os números são {soma}')
print(f'Média foi {media}')
print(f'O Maior nº é {maior}')
print(f'O Menor nº é {menor}')
'''
#Correção Guanabara
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
