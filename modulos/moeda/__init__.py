def dobro(N=0, fmt=False):
    """
        [Dobra Valor]
            Args:
                N (Float): [Valor]
            Returns:
                [Float]: [Valor Final]
    """
    r = N * 2
    return r if fmt is False else dinBR(r)


def metade(N=0, fmt=False):
    """
        [Reduz Pela Metade]
            Args:
                N (Float): [Valor]
            Returns:
                [Float]: [Valor Final]
    """
    r = N / 2
    return r if fmt is False else dinBR(r)


def aumentar(N=0, P=0, fmt=False):
    """
        [Aumentar Porcentagem]
            Args:
                N (Float): [Valor]
                P (Float): [Porcentagem]
            Returns:
                [Float]: [Valor Final]
    """
    r = N + N*(P/100)
    return r if fmt is False else dinBR(r)


def diminuir(N=0, P=0, fmt=False):
    """
        [Diminui Porcentagem]
            Args:
                N (INT): [Valor]
                P (INT): [Porcentagem]
            Returns:
                [INT]: [Valor Final]
    """
    r = N - N*(P/100)
    return r if fmt is False else dinBR(r)


def dinBR(N=0, din="R$"):
    return f"{din}{N:.2f}".replace(".", ",")


def leiaint(MSG):
    while True:
        V = str(input(MSG)).replace(",", ".").strip()
        if V.isnumeric() or V == "":
            N = int(V)
            break
        else:
            print(f"{V} é um valor invalido!!")
    return N


def leiadin(MSG):
    while True:
        V = str(input(MSG)).replace(",", ".").strip()
        if V.isalpha() or V == "":
            print(f"ERRO: {V} é Valor inválido!!!")
        else:
            return float(V)
            break


def tit(MSG):
    print("~"*(len(MSG)*2+6))
    print(f"  {MSG.center(len(MSG)*2)}")
    print("~"*(len(MSG)*2+6))


def resumido(N=1, A=0, D=0):
    tit("TABELA DE VALORES")
    print(
        f"{f'  Dobro {dinBR(N)} ':.<30} {dinBR(N+N*(A/100))}")
    if A > 0:
        print(
            f"{f'  Acrescimo {A}% ':.<30} {dinBR(N+N*(A/100))}")
    if D > 0:
        print(
            f"{f'  Desconto {D}% ':.<30} {dinBR(N-N*(D/100))}")
