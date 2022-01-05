# sequência para custumizar o texto - style, text e back
#STYLE -> 0 none, 1 Bold, 4 Underline e 4 Negative
#As cores principais começam com 30 até 37 (sem biblioteca)
#BACk as cores principais começam com 40 até 47.
'''
\033[0:30:41m
\033[4:33:44m
\033[1:35:43m
\033[30:42m
\033[m
\033[7:30m
'''
print('\033[1:31:43mOlá, Mundo!\033[m')
print('\033[1:30:41mOlá, Mundo!\033[m')
print('\033[7:30mOlá, Mundo!\033[m')
a = 3
b= 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

#Outra opção para formatação.
print('Os valores são {}{}{} e {}{}{} !!!'.format('\033[4;34m',a,'\033[m','\033[4;35m',b,'\033[m'))
