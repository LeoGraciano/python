from random import randint
from time import sleep


def somaPAR():
    spr = 0
    for i, v in enumerate(números):
        if v % 2 == 0:
            spr += v
    if spr == 0:
        spr = "Não temos Numeros Pares"
    print(f"A soma dos números pares de: {números}, temos: {spr}")


def sorteia():
    print("Sorteamos 5 numeros da lista: ", end="")
    for c in range(0, 5):
        n = randint(0, 999)
        números.append(n)
        print(n, end=" ")
        sleep(.5)
    print("PRONTO")


números = []
