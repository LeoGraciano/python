p = c = m = 0
n = int(input("Tabuada de qual numero: "))
print("~"*20)
while True:
    if n < 0:
        break
    for m in range(1, 10):
        p = n * m
        print(f" {n}  x {m} = {p} ")
    else:
        print("~"*20)
        n = int(input("Nova tabuada? "))
        print("~"*20)
