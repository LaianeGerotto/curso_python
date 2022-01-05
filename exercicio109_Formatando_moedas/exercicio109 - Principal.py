from exercicio109_Formatando_moedas import funções

preço = float(input('Digite o preço: R$ '))
print(f'A METADE de {funções.moeda(preço)} é {funções.metade(preço, True)}')
print(f'A DOBRO de {funções.moeda(preço)} é {funções.dobro(preço, True)}')
print(f'Aumentando 10%, temos {funções.aumentar(preço, 10, True)}')
print(f'Reduzindo 13%, temos {funções.diminuir(preço, 13, True)}')