temp = []
main = []
pmx = pmn = 0
while True:
    temp.append(str(input("Nome: ").strip().title()))
    temp.append(eval(input("Peso[Kg]: ")))
    if len(main) == 0:
        pmx = pmn = temp[1]
    else:
        if pmx < temp[1]:
            pmx = temp[1]
        if pmn > temp[1]:
            pmn = temp[1]
    main.append(temp[:])
    temp.clear()
    r = str(input("Quer Continuar[S/N]: ")).strip().upper()[0]
    while r not in "SN":
        r = str(input("Valor Invalido, Continuar[S/N]: ")).strip().upper()[0]
    if r == "N":
        break
print(f"Foram cadastradas {len(main)} pessoas .")
print(f"O MAIOR peso foi {pmx:.1f}Kg de ", end="")
for p in main:
    if p[1] == pmx:
        print(f"[{p[0]}]", end=" ")
print()
print(f"O MENOR  peso foi de {pmn:.1f}Kg de ", end="")
for p in main:
    if p[1] == pmn:
        print(f"[{p[0]}]")
print()
