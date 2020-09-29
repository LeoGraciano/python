s = int(input("Qual sua renda mensal: R$"))
f = float(input("Qual valor do imóvel: R$"))
e = float(input("QUal valor da entrada: R$"))
t = int(input("Quanto meses deseja parcela: "))
p =  (f - e) / t
if p <= (s*0.3):
    if(t%12) > 0:
        print(f"O valor da prestão sera R${p:.2f} como solicidando em {t}x que equivale {(t//12)}ano(s) e {t%12} mes(es)")
    elif (t%12) == 0:
        print(f"O valor da prestão sera R${p:.2f} como solicidando em {t}x que equivale {(t//12)}ano(s)")
else:
    print ("Infelizmente prestação supera 30% da sua renda, tente aumentar o numero de meses ou entrada maior.") 