c = str(input('Qual nome da sua cidade: ')).strip()
#print('Sua cidade começa com Santo: {}.'.format('Santo' in c[:5]))
print ('Sua cidade começa com Santo: {}'.format(c[:5].upper() == 'SANTO'))