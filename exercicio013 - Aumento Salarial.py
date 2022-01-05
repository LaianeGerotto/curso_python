salario = float(input('Digite o salário atual: R$'))
aumento = float(input('Digite a porcentagem(%) do aumento: '))
print('O Novo Salário com o aumento de {}%, corresponde à R${:.2f}.' .format(aumento, (salario+(salario*aumento/100))))
