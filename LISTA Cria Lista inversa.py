l = []
while True:
    n = int(input("Digite um valor: "))
    r = str(input("Deseja Continua[S/N]: ")).strip().upper()
    while r in "SN":
        r = str(input("Deseja Continua[S/N]: ")).strip().upper()
    if r == "N":
        break
