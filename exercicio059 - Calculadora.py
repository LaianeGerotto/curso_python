
print('CALCULADORA')
opcao = 0
while opcao != 5:
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    print('OPÇÕES: ')
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa')
    opcao = int(input('Qual a opção desejada? '))
    if opcao == 1:
        resultado = n1 + n2
        print(f'Resultado = {resultado}')
    if opcao == 2:
        resultado = n1 * n2
        print(f'Resultado = {resultado}')
    if opcao == 3:
        if n1 > n2:
            print(f'Resultado: {n1}')
        else:
            print(f'Resultado: {n2}')
'''
#Correção Guabanara
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa')
    opcao = int(input('----> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando.....')
    else:
        print('Opção Inválida. Tente novamente')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')
'''