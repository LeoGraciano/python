print("Geradora de PA")
n = int(input("Qual valor termo: "))
r = int(input("Qual a razão: "))
t = n
c = 1
ttl = 0
mais = int(input("Quantos termos: "))
while mais != 0:
    ttl += mais
    while c <= ttl:
        print(f"{t} -> ", end="")
        t += r
        c += 1
    print(" FIM")
    mais = int(input("Quantos termos você quer mostra a mais? "))
print("Fim")
print("A progressão foi finalizada me")
