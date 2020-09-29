n = list()
while True:
    nv = int(input("Digite um valor: "))
    if nv not in n:
        n.append(nv)
        print("Valor adicionado com sucesso.")
    else:
        print("Valor Duplicado!!! Não pode ser adicionando.")
    r = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
    while r not in "SN":
        r = str(
            input("Valor Inválido, deseja continuar[S/N]: ")).strip().upper()[0]
    if r in "N":
        break
print(sorted(n))
