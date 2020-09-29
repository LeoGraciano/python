n = str (input('Qual seu nome completo: ')).strip()
#ns = n.split()
print('Seu primeiro nome é: {}.'.format(n.split()[0].title()))
print('Seu ultimo nome é: {}.'.format(n.split()[-1].title()))