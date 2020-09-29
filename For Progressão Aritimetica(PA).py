n1 = int(input("Digite um numero: "))
r = int(input("Digite a Razão da PA: "))
for pa in range(n1, n1+(10-1)*r, r):
    print(pa, end=" -> ")
print("ACABOU")
