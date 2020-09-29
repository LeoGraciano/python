l = list()
qnt = mx = mn = 0
for c in range(0, 5):
    l.append(int(input(f"Digite valor na posição {qnt}: ")))
    qnt += 1
print(f"O valores digitados foram: {l}")
print(
    f"O Maior valor dos numeros digitado foram {max(l)} e o minimo foi {min(l)}.")
print(f"O maior valor é {max(l)} ele esta na posição: ", end="")
for p, v in enumerate(l):
    if v == max(l):
        print(f"{p}", end=" ")
print(f"\nO menor valor é {min(l)} ele esta na posição: ", end="")
for p, v in enumerate(l):
    if v == min(l):
        print(f"{p}", end=" ")
