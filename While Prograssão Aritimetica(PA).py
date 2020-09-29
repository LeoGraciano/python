print("Geador de PA")
print("-="*10)
n = int(input("Digite o valor da PA: "))
r = int(input("Qual a razão da PA: "))
t = n
c = 1
while c <= 10:
    print(f"{t} -> ", end="")
    t += r
    c += 1
print("FIM")
