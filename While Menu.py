n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
m = 0
while m != 5 or m > 5:
    print("-="*20)
    print('''Menu do Sistema:
[1] - Somar
[2] - Multiplia
[3] - Maior Numéro
[4] - NOVO NUMEROS
[5] - Sair do Programa''')
    m = int(input("Qual opção Deseja: "))
    print("-="*20)
    if m == 1:
        s = n1 + n2
        print(f"A soma dos números {n1} + {n2} = {s}")
    elif m == 2:
        p = n1 * n2
        print(f"A produto dos numero {n1} x {n2} = {p}")
    elif m == 3:
        if n1 > n2:
            print(f"o {n1} é Maior.")
        else:
            n2 > n1
        print(f"O {n2} é Maior")
    elif m == 4:
        n1 = int(input("Digite novamente o valor: "))
        n2 = int(input("Digite outro valor:"))
    else:
        m == 5
        print("Fim do Programa")
