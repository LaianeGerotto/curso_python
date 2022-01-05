velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80)* 7
if velocidade > 80:
    print('Você foi multado!!')
    print('- O valor da Multa é R${:.2f}'.format(multa))
else:
    print('Você está dentro do Limite permitido!')
