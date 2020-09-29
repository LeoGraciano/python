from datetime import date
a = int(input('Qual ano deseja consultar, 0 = ano atual: '))
if a == 0:
    a = date.today().year
print ('O ano de {} é bissexto'.format(a) if a % 4 and a % 100 != 0 or a %400 == 0 else 'O ano {} não é bissexto'.format(a))