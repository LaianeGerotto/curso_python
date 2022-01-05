print('***'*15)
print('   Podemos ou não formar um Triângulo?!')
print('***'*15)
linha1 = int(input('Digite o tamanho da primeira linha: '))
linha2 = int(input('Digite o tamanho da segunda linha: '))
linha3 = int(input('Digite o tamanho da terceira linha: '))
if ((linha1 < (linha2 + linha3)) and (linha2 < (linha1 + linha3)) and (linha3 < (linha1 + linha2))):
    print('As medidas informadas FORMA um triângulo!')
    if((linha1 == linha2 == linha3)):
        print('Triângulo EQUILÁTERO.')
        print('- Todos os lados são iguais.')
    elif linha1 != linha2 != linha3 != linha1:
        print('Triângulo ESCALENO.')
        print('- Todos os lados diferentes.')
    else:
        print('Triângulo ISÓSCELES.')
        print('- Dois lados iguais.')
else:
    print('As medidas informadas NÃO pode formar um triângulo!')