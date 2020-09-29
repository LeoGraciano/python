temp = []
lst = []
while True:
    n = str(input("Nome: ")).strip().title()
    temp.append(n)
    for c in range(0, 2):
        nt = float(input(f"{c+1}° Nota: "))
        while nt > 10 or nt < 0:
            nt = float(input("Nota Invalida, digite novamente: "))
        temp.append(nt)
    temp.append((temp[1]+temp[2])/2)
    lst.append(temp[:])
    temp.clear()
    r = str(input("Deseja continua[S/N]: ")).strip().upper()[0]
    while r not in "NS":
        r = str(input("Valor Invalido, continua[S/N]: ")).strip().upper()[0]
    if r == "N":
        break
print("-="*20)
print(f"{'N°':<5}{'NOME':<15}{'MÉDIA':^4}")
for p, d in enumerate(lst):
    print(f"{p+1:<5}{d[0]:<15}{d[3]:^5.1f}", end="")
    print()
print("-"*40)
while True:
    print("Digite 0 para sair.")
    rl = int(input("Quais Notas deseja ver: "))
    if rl == 0:
        break
    while rl > len(lst) or rl < 0:
        rl = int(input("Valor Errado. Quais Notas deseja ver: "))
    print("-"*40)
    print(f"Nome: {lst[rl-1][0]} - Notas:{lst[rl-1][1:3]}")
    print("-="*20)
print("Volte Sempre!!!")
