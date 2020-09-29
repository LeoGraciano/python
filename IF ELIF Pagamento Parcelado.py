print("-="*20)
p = float(input("Qual valor do produto: R$"))
print("-="*20)
print ('''[1] - Àvista em Dinheiro com (10% Desconto).
[2] - Àvista em Cartão com (5% Desconto).")
[3] - Parcelado em 2x vezes")
[4] - 3x vezes ou mais no Cartão com (20% de juros)''')
print ("-="*20)
f = int(input("Qual a forma de pagamento: "))
print("-="*20)
if f == 1:
    vf = p*0.90
    d = "10%"
    print (f"Valor do produto é de {p} com {d} desconto.")
elif f == 2:
    vf = p*0.95
    d = "5%"
    print (f"Valor do produto é de {p} com {d} desconto.")
elif f == 3:
    vf = p
    vp = p/2
    np = 2
    print (f"Valor do produto fica em R${vf} em {np}x com parcela no valor de R${vp:.2f}")
elif f == 4:
    np = int(input('Qual numero de parcela: '))
    vf = p*1.20 
    vp = vf/np
    print (f"Valor do produto fica em R${vf} em {np}x com parcela no valor de R${vp:.2f}")
else: 
    f > 3 or p == 0
    print("Valor não é valido")