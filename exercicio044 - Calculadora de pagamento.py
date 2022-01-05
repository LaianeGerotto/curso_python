print('Calculadora de pagamento')
print('')
valor = float(input('Informe o valor da sua Compra: R$'))
print('')
print('Segue abaixo as opções de pagamento:')
print('¨'*40)
print('1- À Vista - Dinheiro (desconto de 10%). \n2- À vista no Cartão (desconto de 5%). \n3- 2x no Cartão (sem desconto). \n4- 3x ou mais no Cartão (20% de juros).')
print('¨'*40)
opcao = int(input('Qual a opção de pagamento você deseja? '))

if opcao == 1:
    pagar = valor - (valor * 0.10)
elif opcao == 2:
    pagar = valor - (valor * 0.05)
elif opcao == 3:
    pagar = valor
    mensal = pagar/2
    print(f'Sua compra será parcelada em 2x de R${mensal:.2f} sem juros')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    pagar = valor + (valor * 0.20)
    mensal = pagar/parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${mensal:.2f} com juros')
else:
    pagar = 0
    print('Opção Inválida!')
print(f'Sua compra de R${valor:.2f} vai custar R${pagar:.2f} no final.')
