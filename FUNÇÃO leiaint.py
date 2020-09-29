def leiaint(MSG):
    OK = False
    V = 0
    while True:
        n = str(input(MSG))
        if n.isnumeric():
            V = int(n)
            OK = True
        else:
            print("\033[0;31mValor Inválido.\033[m")
        if OK:
            break
    return V


n = leiaint("Digite um Numero: ")
print(f"Numero que você digitou foi {n}")
