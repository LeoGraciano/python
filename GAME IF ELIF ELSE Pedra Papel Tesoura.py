from random import randint
from time import sleep
print("-="*11)
i = ("Pedra", "Papel", "Tesoura")
pc = randint(0, 2)
print('''ESCOLHA SUA OPÇÃO:
[1] - Pedra
[2] - Papel
[3] - Tesoura''')
print("-="*11)
h = int(input("O que você escolhe: "))
h = h - 1
print("-="*11)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("POU!!")
sleep(1)
print(f"Computado jogou {i[pc]}")
print(f"Você jogou {i[h]}")
print("-="*11)
if pc == 0:
    if h == 0:
        print("EMPATOU.")
    elif h == 1:
        print("VOCÊ GANHOU!!")
    elif h == 2:
        print("COMPUTADOR GANHOU!!")
    else:
        print("JOGADA INVÁLIDA")
elif pc == 1:
    if h == 0:
        print("VOCÊ GANHOU.")
    elif h == 1:
        print("EMPATE")
    elif h == 2:
        print("COMPUTADOR GANHOU!!")
    else:
        print("JOGADA INVÁLIDA")
elif pc == 2:
    if h == 0:
        print("VOCÊ GANHOU!!!.")
    elif h == 1:
        print("COMPUTADOR GANHOU!!")
    elif h == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")
else:
    h > 4
    print("JOGADA INVÁLIDA")
