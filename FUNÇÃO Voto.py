def IDADAVOTO(a):
    from datetime import date
    ida = date.today().year - a
    if ida < 16:
        msg = "NÃO PODE VOTAR"
    elif 16 <= ida < 18 or ida >= 65:
        msg = "VOTO OPCIONAL"
    else:
        msg = "VOTO OBRIGATÓRIO"
    return f"Com {ida} anos: {msg}"


a = int(input("Qual ano você nasceu: "))
print(IDADAVOTO(a))
