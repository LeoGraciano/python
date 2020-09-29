p = m = 0
n = int(input("Tabuada de qual número: "))
print("-="*15)
while True:
    if m < 11:
        p = m * n
        m += 1
        print(f"{n}  x {m-1:2} = {p}")
    else:
        print("-="*15)
        n = int(input("Tabuada de que numero: "))
        m = 0
        print("-="*15)
    if n <= -1:
        break
print("Fim")
