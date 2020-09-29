n = int(input("Qual valor para calcular o fatorial: "))
c = n
f = 1
print(f"Caculando o {n}! =", end="")
while c > 0:
    print(f" {c}", " x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f"{f}")
