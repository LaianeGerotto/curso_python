soma = contador = menorvalor = 0
produtomenor = ''
print('-='*20)
print('          Loja MEG Company Ltda')
print('-='*20)
while True:
    produto = str(input('Nome do Produto: ')).upper().strip()
    preco = float(input('Preço: R$'))
    soma += preco
    if preco > 1000:
        contador +=1
    if preco < menorvalor or menorvalor == 0:
        menorvalor = preco
        produtomenor = produto

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    print('=-' * 15)
    if opcao == 'N':
        break
print(f'O Total da compra foi de R${soma:.2f}')
print(f'Temos {contador} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produtomenor} que custou R${menorvalor:.2f}')
'''
#Correção Guanabara
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Programa '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f} ')
'''