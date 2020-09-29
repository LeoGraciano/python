from random import randint
kmh = randint(0,240)
lmt = (kmh - 80) * 7 
print ('O PC foi multado por excesso de Velocidade {:.1f}km/h valor da multa será R${:.2f}.'.format(kmh,lmt) if kmh > 80 else 'Dirija com segurança!!! Sua velocidade é {}km/h'.format(kmh))