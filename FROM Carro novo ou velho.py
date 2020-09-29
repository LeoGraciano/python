from datetime import date
t = int(input('Qual ano de fabricação do seu carro: '))
print ('Carro Novo' if date.today().year-t<=5 else 'Carro Velho')
#if (2020 - t) <=5:
#    print('Seu carro é novo')
#else:
#    print ('Seu carro é velho')
print('--FIM--')