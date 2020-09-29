a = int(input('Qual primeiro número: '))
b = int(input('Qual segundo número: '))
c = int(input('Qual terceiro numero: '))
if a < b and  a < c:
    m = a
if b < a and b < c:
    m = b
if c < a and c < b:
    m = c
if a > b and a > c:
    M = a
if b > a and b > c:
    M = b
if c > a and c > b:
    M = c
print ('O menor valor foi {} e o maior foi {}.'.format(m,M))