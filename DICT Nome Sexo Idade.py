dados = dict()
grupo = []
ida = 0
while True:
    dados["Nome"] = str(input("Nome: ")).strip().title()
    dados["Idade"] = int(input("Idade: "))
    ida += dados["Idade"]
    dados["Sexo"] = str(input("Sexo[M/F]: ")).strip().upper()[0]
    while dados["Sexo"] not in "MF":  # validação Sexo
        dados["Sexo"] = str(
            input("Dado Invalido!!! Sexo[M/F]: ")).strip().upper()[0]
    r = str(input("Deseja Continuar[S/N]: ")).strip().upper()[0]
    while r not in "SN":  # validação de Continuação
        r = str(input("Dado Inválido!!! Continuar[S/N]: ")).strip().upper()[0]
    grupo.append(dados.copy())
    dados.clear()
    if r == "N":
        break
print(grupo)
print("-="*20)
print(f"    Foram cadastradas {len(grupo)} pessoas.")
m = ida/len(grupo)
print(f"    A media de idade do grupo é {m} anos.")
print(f"    As mulheres Cadastradas foram: ", end="")
for p in grupo:
    if p['Sexo'] == "F":
        print(p['Nome'], end=" ")
print()
print(f"A lista de pessoas acima da media são : ", end="")
for p in grupo:
    if p['Idade'] > m:
        print(f"{p['Nome']} com {p['Idade']}", end=" ")
print()
