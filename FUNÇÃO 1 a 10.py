from time import sleep


def lin():
    print("-="*20)


def contage(A, B, C):
    if C == 0:
        C = 1
    if A > B:
        if C > 0:
            C = C-(C*2)
        B += -1
        print(f"O Numero de {A} à {B+1} de {C} em {C}.")
    else:
        print(f"O Numero de {A} à {B} de {C} em {C}.")
    for cont in range(A, B, C):
        print(cont, end=" ")
        sleep(0.5)
    print("FIM")
    lin()


lin()
contage(1, 10, 1)
lin()
contage(10, 1, -1)
while True:
    print(f"{'AGORA SUA VEZ!!':^20}")
    a = int(input("  Inicial: "))
    b = int(input("  Final: "))
    c = int(input("  Passo: "))
    contage(a, b, c)

    r = str(input(" Continuar[S/N]: ")).strip().upper()[0]
    while r not in "NS":
        lin()
        r = str(input(" Dado Invalido!! Continuar[S/N]: ")).strip().upper()[0]
    if r in "N":
        break
print("PROGRAMA ENCERRADO")
