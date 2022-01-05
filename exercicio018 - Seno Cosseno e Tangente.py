import math
ang = int(input('Digite o ângulo: '))
rad = math.radians(ang)
print('Baseado no {}º o é SENO {:.3f}, o COSSENO é {:.3f} e TANGENTE é {:.3f}'.format(ang,math.sin(rad), math.cos(rad), math.tan(rad)))

