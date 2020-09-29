n = (int(input("Digite um Número: ")),
     int(input("Digite outro Número: ")),
     int(input("Digite mais um Número: ")),
     int(input("Digite o ultimo Número: ")))
print(f"Você digitou o valor {n}")
if 9 in n:
    print(f"O valor 9 aparece {n.count(9)} vezes.")
if 3 in n:
    print(f"O numero 3 aparece na {n.index(3)+1}ª posição ")
print("Você valores pares digitados foram: ", end="")
for p in n:
    if p % 2 == 0:
        print(p, end=" ")
