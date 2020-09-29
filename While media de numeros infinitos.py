c = ""
qnt = 0
m = 0
nM= 0
nm = 0
while c != "N":
    n = int(input("Digite um valor: "))
    c = str(input("Deseja Continuar[S/N]: ")).strip().upper()[0]
    qnt += 1
    if c == "S":
        m= n
        m+=m
        if qnt == 1:
            nM = n
            nm = n
        if n > nM:
            nM = n
        if n < nm:
            nm = n
    else:
        print(f"Você digitou {qnt} conjuntos de valores a media é: {m/qnt}") 
        print(f"O mair numero digitado foi {nM} e o menor {nm}")