num = []
pares = []
impares = []
while True:
    n = (int(input(" Digite um valor")))
    if n not in num:
        num.append(n)
    else:
        print("Valor Duplicado!!! Não Adicionado.")
    r = str(input("Deseja Continuar[S/N]: ")).strip().upper()[0]
    if r not in "NS":
        r = str(input("Dado Invalido, Continuar[S/N]: ")).strip().upper()[0]
    if r in "N":
        break
for p, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
num.sort()
print(f"Valores digitados forama a lista: {num}")
if len(pares) > 0:
    print(f"Valores pares digitados: {pares}")
if len(impares) > 0:
    print(f"Os valores impares são: {impares}")
