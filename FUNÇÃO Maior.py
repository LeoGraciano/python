from time import sleep


def maior(* n):
    c = m = 0
    print("Analisando os numeros...")
    sleep(3)
    for v in n:
        print(f"{v} ", end="")
        sleep(.5)
        if c == 0:
            m = v
        elif v > m:
            m = v
        c += 1
    print()
    print(f"O Maior Valor é {m} e foram digitando {c} números")
    print("-="*30)
    sleep(1)


maior(1, 2, 3, 4, 9)
maior(1, 2, 3)
maior(2)
maior()
