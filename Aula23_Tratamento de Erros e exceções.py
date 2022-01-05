# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a/b
# # except:
# #     print('Infelizmente tivemos um problema :(')
# except Exception as erro:
#     print(f'O problema encontrado foi {erro.__class__}')
# else:
#     print(f'O resultado é {r:.1f}') #opcionais
# finally:
#     print('Volte sempre! Muito Obrigado!')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b

except(ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!')

except ZeroDivisionError:
    print('Não é possível dividir um número por Zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')

else:
    print(f'O resultado é {r:.1f}') #opcionais

finally:
    print('Volte sempre! Muito Obrigado!')
