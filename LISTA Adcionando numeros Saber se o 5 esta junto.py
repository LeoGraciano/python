n = list()
while True:
    n.append(int(input("Digite um numero: ")))
    r = str(input("Deseja Continuar[S/N]: ")).strip().upper()
    while r not in "NS":
        r = str(input("Valor invalido, digitou novamente: ")).strip().upper()
    if r == "N":
        break
print(f"Você digitou {len(n)} elementos.")
n.sort(reverse=True)
print(f"Valores digitados foram: {n}")
# Algum motivo isso não funciona
'''if 5 in r:
    print("Existe o numero 5 na lista.")
else:
    print("O valor 5 não esta na lista.")'''
