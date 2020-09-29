po = int(input('Qual Km você vai rodar: '))
print('você esta presta a começa uma viagem de {}km.'.format(po))
pç = po * 0.50 if po <= 200 else po * 0.45
print ('Sua passagem vai custar R${:.2f}. Boa viagem!!!'.format(pç))

#FUNCIONA MAS FAZER DE UMA MAIS SIMPLES
#n200 = po * 0.50
#n201 = po * 0.45
#print ('Você pagar o valor de R$ {:.2f} para rodar {:.0f}km.'.format(n200,po) if po <= 200 else 'Você pagara R${:.2f} para rodar {:.0f}km.'.format(n201,po))
