from random import randint
print("-="*20)
print(f"======== JOGAR NA MEGA SEMANA ==========")
print("-="*20)
q = int(input("Quantos jogos você quer que eu sorteie? "))

for c in range(0, q):
    while True:
        l = [randint(0, 61), randint(0, 61), randint(0, 61),
             randint(0, 61), randint(0, 61), randint(0, 61)]
        if l[0] != l[1] and l[0] != l[2] and l[0] != l[3] and l[0] != l[4] and l[0] != l[5] and l[1] != l[2] and l[1] != l[3] and l[1] != l[4] and l[1] != l[5] and l[2] != l[3] and l[2] != l[4] and l[2] != l[5] and l[3] != l[4] and l[3] != l[5] and l[4] != l[5]:
            l.sort()
            print(f"Jogo {c+1}: {l}")
            break
