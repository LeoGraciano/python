m = ""
r = ""
while m != 5:
    n1 = int(input("Qual o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    print('''Escolha uma opção:
    [1] - SOMAR
    [2] - MULTIPLICA
    [3] - MAIOR
    [4] - DIGITAR NOVOS NUMEROS
    [5] - SAI DO PROGRAMA''')
    m = int(input("QUAL OPÇÃO DO MENU: "))
    if m == 1:
            r = n1+n2
            print (f"Soma dos números {n1} e {n2} é {r}")
            m = 0
    elif m == 2:
            r = n1 * n2
            print (f"Multiplicação dos números {n1} e {n2} é {r}")
    elif m == 3:
        if n1 > n2:
            print(f"Entre {n1} e {n2} os números {n1} é MAIOR.")
            m = 0
        elif n2 > n1:
            print(f"Entre {n1} e {n2} os números {n2} é MAIOR.")
            m = 0
        else:
            print(f" Dois números são iguais {n1} e {n2}.")
    elif m == 4:
        m = 0
    elif m == 5:
        m = 5
    else:
        print("Escolha novamente.")
