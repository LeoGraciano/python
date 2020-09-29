l = []
for c in range(0, 5):
    n = int(input("Digita um Valor: "))
    while n in l:
        n = int(input("Valor Duplicado Digita um Valor: "))
    if c == 0 or n > max(l):
        l.append(n)
        print("Adicionando no final da fila.")
    else:
        var1 = 0
        while var1 < len(l):
            if n <= l[var1]:
                l.insert(var1, n)
                print(l[var1])
                break
            print(f"Foi adicionando na posição {c}")
            var1 += 1
print(l)
