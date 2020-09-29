from random import randint
from time import sleep
print ("-="*19)
print ("QUAL NUMERO O COMPUTADOR ESTA PENSANDO")
print ("PESANDO...")
sleep(2)
print ("-="*19)
print ("DIGITE UM NUMERO DE 0 A 10")
print ("-="*19)
t = 1
play = ""
e = 0
msg = "PARABENS!!! Você acertou de PRIMEIRA"
pc = randint(0,10)
while play != pc:
    play = int(input(f"Digite {t}° tentativa: "))
    t += 1
    if play != pc:
        e += 1
        print ("TENTE NOVAMENTE....")
        msg = f"Você tentou {t}x e errou {e}x"
print (msg)
print (f"PC escolheu {pc} e você {play}")
