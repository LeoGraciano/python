n1 = float(input("Qual sua nota: "))
n2 = float(input("Qual sua segunda nota: "))
n3 = float(input("Qual sua terceira nota: "))
n4 = float(input("Qual foi sua Quarta nota: "))
m = (n1+n2+n3+n4) / 4
if (m > 7):
    print(f"Sua nota foi {m:.1f}.Você foi APROVADO!!")
elif (m >= 5):
    print (f"Sua not foi {m:.1f} .Você esta de recuperação.")

else:
    print(f"Sua nota foi {m:.1f} . Infelizmente foi reprovado.")