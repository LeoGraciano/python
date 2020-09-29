from random import shuffle
n1 = input ('Qual primeiro nome: ')
n2 = input ('Qual segundo nome: ')
n3 = input ('Qual terceiro nome: ')
n4 = input ('Qual quarto nome: ')
l = [n1,n2,n3,n4]
shuffle(l)
print('A ordem ficou:\n1° - {}\n2° - {}\n3° - {}\n4° - {}'.format(l[0],l[1],l[2],l[3]))