print('***'*15)
print('   Podemos ou não formar um Triângulo?!')
print('***'*15)
linha1 = int(input('Digite o tamanho da primeira linha: '))
linha2 = int(input('Digite o tamanho da segunda linha: '))
linha3 = int(input('Digite o tamanho da terceira linha: '))
if ((linha1 < (linha2 + linha3)) and (linha2 < (linha1 + linha3)) and (linha3 < (linha1 + linha2))):
    print('As medidas informadas FORMA um triângulo!')
else:
    print('As medidas informadas NÃO forma um triângulo!')
