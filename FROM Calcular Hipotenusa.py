from math import hypot
co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual valor do cateto adjacente: '))
#hi = (ca**2 + co**2)**(1/2)
#print ('A hipotenusa do é {:.2f}.'.format(hi))
hi = hypot(co,ca)
print('A hipotenusa é {:.2f}.'.format(hi))