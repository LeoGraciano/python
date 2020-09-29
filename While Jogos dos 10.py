from random import randint
from time import sleep
pc = randint(0, 10)
print("Sou seu compuntador... Acabei de pensar em um número entre 0 e 10.")
print("Sera que você consegue advinha qual foi?")
acertou = False
qnt = 0
while not acertou:
    play = int(input("Qual seu Palpite: "))
    qnt += 1
    if play == pc:
        acertou = true
    else:
        if play < pc:
            print("Mais... Tente mais uma vez.")
        elif play > pc:
            print("Menos... Tente mais uma vez.")
print(f"Acertou com a {qnt} tentativas. Parabens!!!")
