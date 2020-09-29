n = s = c = 0
while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    s += n
    c += 1
if c == 1:
    msg = f"Foi digitados apenas {c} numero e valor é: {s}"
else:
    msg = (f"A soma dos {c} conjuntos de numero foi {s}")
print(msg)
