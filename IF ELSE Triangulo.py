print('-=-'*20)
print('Analisado de Triangulo')
print('-=-'*20)
r1 = float(input('Qual tamanho da primeira reta: '))
r2 = float(input('Qual tamanho da segunda reta: '))
r3 = float(input('Qual tamanho da terceira reta: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Pode formar triangulo!!!')

else:
    print ('Não Pode formar triangulo')