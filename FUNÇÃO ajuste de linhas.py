def lin(msg):
    print("~"*(len(msg)+2))
    print(f" {msg:^5}")
    print("~"*(len(msg)+2))


n = str(input("Digite uma Mensagem: "))
lin(n)
