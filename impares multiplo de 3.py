s = 0
q = 0
for c in range(1,501,2):
    if c % 3 == 0:
        print (c, end = " ")
        q += 1
        s += c
print (f"\nSoma de todos os {q} valores solicitados, múltiplo de 3 é: {s}")