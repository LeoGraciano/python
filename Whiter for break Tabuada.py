c = 0
while True:
    n = str(input("Tabuada de que numero? ")).strip()
    while n.isnumeric() == False:
        n = str(input("DADO INVALIDO!!! Qual numero? ")).strip()
    n = int(n)
    print("~"*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n}  x {c:2} = {n*c}")
    print("~"*30)
print("PROGRAMA TABUADA ENCERRO. VOLTE SEMPRE")
