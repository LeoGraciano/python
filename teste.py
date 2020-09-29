def contador(i=0, f=0, p=0):
    """[Contador]
    Args:
        i (int): [Inicio da contagem]. Defaults to 0.
        f (int): [Fim da contagem]. Defaults to 0.
        p (int): [Passo da contagem]. Defaults to 0.
    """
    c = i
    while c <= f:
        print(f"{c} ", end="")
        c += p
    print("Fim")
