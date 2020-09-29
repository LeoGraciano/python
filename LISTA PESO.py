grupo = list()
dados = list()
dmx = list()
dmn = list()
pmx = pmn = 0
while True:
    dados.append(str(input("Nome: ").strip().title()))
    dados.append(eval(input("Peso[Kg]: ")))
    grupo.append(dados[:])
    dados.clear()
    r = str(input("Quer continuar[S/N]: ")).strip().upper()[0]
    if r not in "NS":
        r = str(input("Dados inválido, continuar[S/N]: ")).strip().upper()[0]
    if r == "N":
        break
for p, d in enumerate(grupo):
    if p == 0:
        pmx = d[1]
        pmn = d[1]
        dmx.append(d[0])
    elif d[1] >= pmx:
        if d[1] == pmx:
            dmx.append(d[0])
        elif d[1] > pmx:
            dmx.clear()
            pmx = d[1]
            dmx.append(d[0])
    elif d[1] <= pmn:
        if d[1] == pmn:
            dmn.append(d[0])
        elif d[1] < pmn:
            dmn.clear()
            pmn = d[1]
            dmn.append(d[0])
print(f"Você Cadastro {len(grupo)} pessoas.")
print(f"O maior peso de {pmx:.1f}Kg e foi {dmx}")
print(f"O menor peso {pmn:.1f}Kg e foi {dmn}")
