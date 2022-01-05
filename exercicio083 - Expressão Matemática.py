'''
contador = contador2 = 0
expressao = list(input("Digite uma expressão Matemática: "))
if expressao[0] != ')':
    for posicao in expressao:
        if '(' in posicao:
            contador += 1
        elif ')' in posicao:
            contador2 += 1
    if contador == contador2:
        print('Expressão Válida')
    else:
        print('Expressão Inválida')
else:
    print('Expressão Inválida')
'''
#Correção Guanabara
expressao = str(input('Digite a expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')