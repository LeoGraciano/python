num = list()
pares = list()
impares = list()
while True:
    n = int(input("Digite um numero: "))
    if n not in num:
        num.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    else:
        print("Valor duplicado!! Não Adicionado")
    r = str(input("Quer Continuar[S/N]: ")).strip().upper()
    if r not in "NS":
        r = str(input("Dado Invalido, Continuar[S/N]: ")).strip().upper()
    if r == "N":
        break
num.sort()
print(f"Valores digitados foram {num}")
if len(pares) > 0:
    print(f"Os numeros digito {len(pares)} pares e foram {pares.sort()}")
if len(impares) > 0:
    print(f"Os numeros digito {len(impares)} impares e foram {impares.sort()}")
