#As listas são modificáveis
#Para declarar uma lista só utilizar []
#para adicionar novos itens a lista usar o comando .APPEND('')
#Para adicionar um item em uma posição já utilizada, usar o comando .INSERT(posição,'')
#Para apagar um item da lista pode utilizar o comando DEL variavel[posição] ou variavel.pop(posição), o POP geralmente
# é utilizado para apagar o último elemento caso a declaração não conste a posição -> variavel.pop()
#Pode utilizar o .remove('nome') para apagar o conteúdo
'''
num =[2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort() #organiza
num.insert(2, 0) #2 é a posição
#num.pop(2) # exclui o item da posição 2
num.sort(reverse=True)
if 5 in num:
    num.remove(5) #remove o número 5 da Lista
else:
    print('Não achei o nº 5')
print(num)
'''

'''
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Fim da lista')

'''

'''
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Fim da lista')
'''

a = [2, 3, 4, 7]
#b = a #Se houver uma alteração em algum item da lista, todas ficarão iguais... para evitar isso usar b = a[:] cria uma cópia
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')