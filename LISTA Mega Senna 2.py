from random import randint
print("-="*20)
print(f"======== JOGAR NA MEGA SEMANA ==========")
print("-="*20)
q = int(input("Quantos jogos você quer que eu sorteie? "))
j = []
for c in range(0, q):
    while True:
        n = randint(1, 61)
        if n not in j:
            j.append(n)
        if len(j) == 6:
            j.sort()
            print(f"{c+1}° Jogo: {j}")
            j.clear()
            break
