from random import randint
from time import sleep
game = ("Par", "Impar")
pcn = randint(1, 5)
pcg = randint(0, 1)
qnt = 0
while True:
    print("~"*30)
    print("COMPUTADOR PENSANDO..")
    print("~"*30)
    n = int(input("Digite um valor 1 à 5: "))
    while n > 5:
        n = int(input("Dado invalido,Digite um valor 1 à 5: "))
    vg = str(input("Par ou Impar[P/I]: ")).strip().upper()[0]
    print("~"*30)
    while vg not in "PI":  # VALIDAR PAR E IMPAR
        vg = str(
            input("Dado Inválido!! Digite Par ou Impar[P/I]: ")).strip().upper()[0]
    print("~"*30)
    pcn = randint(1, 5)
    if vg in "P":
        pcg = game[1]
    elif vg in "I":
        pcg = game[0]
    s = pcn + n
    if s % 2 == 0:
        c = "P"
        if c == vg:
            print(f"total de {n} + {pcn} = {s} a soma é Par. ", end="")
            print("Você ganhou!!!!")
            qnt += 1
        else:
            break
    elif s % 2 != 0:
        c = "I"
        if c == vg:
            print(f"total de {n} + {pcn} = {s} a soma é Impar. ", end="")
            print("Você ganhou!!!!")
            qnt += 1
        else:
            break
print(f"total de {n} + {pcn} = {s} a soma é {pcg} ")
print(f"Você perdeu!!! ")
if qnt > 0:
    print(f"Conseguiu ganhar {qnt} vitorias")
print("~"*30)
