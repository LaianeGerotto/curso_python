print('Vamos calcular sua Média?!')
n1 = float(input('Digite a 1ª Nota: '))
n2 = float(input('Digite a 2ª Nota: '))
media = (n1 + n2)/ 2
print('--'*12)
if media < 5.0:
    print('O Aluno está Reprovado!')
elif media > 5.0 and media < 6.9:
    print('O Aluno está em Recuperação!')
elif media > 7:
    print('Aluno está Aprovado. Parabéns!')
print(f'Sua Média foi {media}!')