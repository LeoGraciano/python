def lin(T=42):
    return "-" * T


def tit(TXT):
    print(lin())
    print(TXT.center(42))
    print(lin())


def leiaint(MSG):
    while True:
        try:
            V = int(input(MSG))
        except (ValueError, TypeError):
            print("ERRO!!! Valor informatdo Inválido.")
        except KeyboardInterrupt:
            print("Usuário Desistiu de Digitar")
            return ""
        else:
            return V


def menu(LISTA):
    tit("MENU PRINCIPAL")
    for i, D in enumerate(LISTA):
        print(f"\033[33m{i+1}\033[m - \033[34m{D}\033[m")
    print(lin())
    OPÇ = leiaint("Sua Opção: ")
    return OPÇ
