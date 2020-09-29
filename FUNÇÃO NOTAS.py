def NOTAS(*N, sit=False):
    """
        [Media de Notas]
            Args:
                N (INT): [Adciona valores para calculo da Media]
                sit (optional): [True para mostra situação]. Defaults to False.
            Returns:
                [Dict]: [Retorna o Dicionário que foi adcionado]
    """
    NTS = {}
    NTS['Total'] = len(N)
    NTS['Maior'] = max(N)
    NTS['Menor'] = min(N)
    NTS['Media'] = sum(N)/len(N)
    if sit:
        if NTS['Media'] >= 7:
            NTS['Situação'] = "Boa!!"
        elif NTS['Media'] >= 5:
            NTS['Situação'] = "Razoável"
        else:
            NTS['Situação'] = "Ruim!!"
    return NTS


resp = NOTAS(5.5, 2, 5.4, 3.8)
print(resp)
