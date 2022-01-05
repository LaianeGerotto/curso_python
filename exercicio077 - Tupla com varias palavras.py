'''
vogais = 'aeiou'
conjunto = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for lista in range(0,len(conjunto)):
    print(f'Na palavra {conjunto[lista].upper()} temos', end=' ')
    for letra in conjunto[lista]:
        if letra in vogais:
            print(letra, end=' ')
    print()
'''
#Correção Guanabara
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou': #para acertar palavras com acento só escrever 'aáàâãeéèêiíìî...'
            print(letra, end=' ')

