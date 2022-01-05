print('-'*19)
print(' Base de conversão')
print('-'*19)
n = int(input('Digite um número inteiro: '))
print('Base de Conversão: \n  [1] para Binário \n  [2] para Octal \n  [3] para Hexadecimal')
tipo = int(input('Qual opção deseja 1, 2 ou 3? '))
if tipo == 1:
   conversao = bin(n)[2:]
   print(f'O numero {n} corresponde ao \033[34m{conversao}\033[m em BINÁRIO.')
elif tipo == 2:
    conversao = oct(n)[2:]
    print(f'O numero {n} corresponde ao \033[34m{conversao}\033[m em OCTAL.')
elif tipo == 3:
    conversao = hex(n)[2:]
    print(f'O numero {n} corresponde ao \033[34m{conversao}\033[m em HEXADECIMAl.')
else:
    print('Opção inválida. Tente Novamente!')