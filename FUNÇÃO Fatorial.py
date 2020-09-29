def fatorial(n=1, show=False):
    """
        [Calculo de Fatorial]
            Args:
                n (INT): [Numero a ser Calculado]. Defaults to 1.
                show (OPCIONAL: TRUE, FALSE): [Para mostra a operação]. Defaults to False.
            Returns:
                [INT]: [Retorna o valor do Fatorial]
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f"{c}", end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return print(f)


fatorial(5, True)
