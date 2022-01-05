from exercicio108_Formatando_moedas import funções

preço = float(input('Digite o preço: R$ '))
print(f'A METADE de {funções.moeda(preço)} é {funções.moeda(funções.metade(preço))}')
print(f'A DOBRO de {funções.moeda(preço)} é {funções.moeda(funções.dobro(preço))}')
print(f'Aumentando 10%, temos {funções.moeda(funções.aumentar(preço, 10))}')
print(f'Reduzindo 13%, temos {funções.moeda(funções.diminuir(preço, 13))}')