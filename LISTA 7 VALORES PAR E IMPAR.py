grupo = [[], []]
n = 0
for c in range(0, 7):
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        grupo[1].append(n)
    else:
        grupo[0].append(n)
if len(grupo[1]) > 0:
    grupo[1].sort()
    print(f"Foram digitando {len(grupo[1])} números pares: {grupo[1]}")
if len(grupo[0]) > 0:
    grupo[0].sort()
    print(f"Foram digitado {len(grupo[0])} números impares: {grupo[0]}")
