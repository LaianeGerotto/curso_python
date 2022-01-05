preco = float(input('Digite o preço do Produto: R$'))
desconto = float(input('Digite o desconto em %: '))
print('O produto tem desconto de {}%, sai por R${:.2f}.' .format(desconto, (preco-(preco*desconto/100))))
