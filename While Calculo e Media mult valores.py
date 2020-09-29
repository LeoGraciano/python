r = ""
t = qnt = Mn = mn = 0
while r in "S":
    n = int(input("Digite um numero: "))
    t += n
    qnt += 1
    r = str(input("Quer continuar[S/N]")).strip().upper()[0]
    while r not in "SN":
        r = str(
            input("Dados Inválidos tente novamente[S/N]: ")).strip().upper()[0]
    if qnt == 1:
        mn = Mn = n
        msgn = "Número"
    else:
        msgn = "Números"
        if n < mn:
            nm = n
        if n > Mn:
            Mn = n
print(f"A soma foi {t} em {qnt} {msgn} digitados media foi {t/qnt:.1f}")
print(f"maior numéro é {Mn} e o menor foi {mn}.")
