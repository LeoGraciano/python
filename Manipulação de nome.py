n = str(input('Qual seu nome: ')).strip()
print('Seu nome é: {}.'.format(n))
print('Maiusculo: {}'.format(n.upper()))
print('Minusculo: {}'.format(n.lower()))
#nse = n.split()
#nsec = len(nse[0])
#print ('Quantas letras tem o primeiro nome: {}'.format(nsec))
#nse = ''.join(nse)
#nsc = len(nse)
#print('Quantas letras: {}.'.format(nsc))
print ('Seu nome tem {} letras.'.format(len(n) - n.count(' ')))
print ('Seu primeiro nome tem {} letras.'.format(n.find(' ')))