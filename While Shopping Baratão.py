qntV = t = valor = 0
caro = ""
while True:
    n = str(input("NOME DO PRODUTO: ")).upper()
    p = str(input("PREÇO: R$")).strip()
    while p.isnumeric() == False:
        p = str(input("DADO INVÁLIDO!! PREÇO: R$")).strip()
    p = int(p)
    r = str(input("Deseja Continua[S/N]: ")).strip().upper()[0]
    while r not in "SN":  # Continua ou para
        r = str(input("DADO INVALIDO!! Continua[S/N]: ")).strip().upper()[0]
    t += p
    if p > valor:
        valor = p
        caro = n
    if p > 1000:
        qntV += 1
    if r == "N":
        break
print(f"Total da compra ficou em R${t:.2f}.")
if qntV > 0:
    print(f"Teve {qntV} acima de R$1000.00")
print(f"Produto mais de maior valor foi {caro} custando R${valor:.2f}.")
