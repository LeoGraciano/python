r = s = ""
qntM = qntw = qntH = 0

while True:
    i = str(input("Qual idade: "))
    while i.isnumeric() != True:  # Validação Idade
        i = str(input("DADO INVÁLIDO, qual idade: "))
    i = (int(i))
    s = str(input("Qual Sexo[M/F]: ")).strip().upper()[0]
    while s not in "MF":  # validação Sexo
        s = str(input("DADO INVÁLIDO, qual Sexo[M/F]: ")).strip().upper()[0]
    r = str(input("Que continua[S/N]: ")).strip().upper()[0]
    if s == "F" and i < 20:
        qntw += 1
    elif s == "M":
        qntH += 1
    if i >= 18:
        qntM += 1
    while r not in "SN":  # Validação de Parada
        r = str(
            input("DADO INVÁLIDO, Seja Continuar[S/N]: ")).strip().upper()[0]
    if r == "N":  # Condição de parada
        break
if qntM > 0:
    print(f"Existe {qntM} Pessoas maiores de 18 anos.")
if qntH > 0:
    print(f"Existe {qntH} Homens cadastrados.")
if qntw > 0:
    print(f"Existe {qntw} mulheres a baixo de 20 anos.")
