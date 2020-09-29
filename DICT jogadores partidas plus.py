dados = {}
gols = []
time = []
while True:
    dados.clear()
    dados["Jogador"] = str(input("Qual nome do Jogador: ")
                           ).strip().capitalize()
    p = int(input("Quants partidas ele jogou: "))
    for c in range(1, p+1):
        gol = int(input(f"  Quantos gols foram marcado na {c}° Partida: "))
        gols.append(gol)
    dados["Gols"] = gols[:]
    dados["Total"] = sum(gols)
    time.append(dados.copy())
    gols.clear()
    r = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
    while r not in "SN":
        r = str(input("Dados Invalido!! continuar[S/N]: ")).strip().upper()[0]
    if r == "N":
        break
print("-="*30)
print(f"{'N°    ':<3}", end="")
for k in dados.keys():
    print(f"{k:<15}", end="    ")
print()
for i, d in enumerate(time):
    print(f"{i+1:<3} - ", end="")
    for v in d.values():
        print(f"{str(v):<15}", end="    ")
    print()
print(f"{'-== DADOS DO JOGADOR ==-':^45}")
while True:
    m = int(input(f"Qual Jogador deseja ver dados de [1/{len(time)}]: "))
    m += -1
    while m <= -1 or m > len(time):  # validando menu do jogador
        m = int(
            input(f"Valor {m+1} Inválido!!! Escolha entre [1/{len(time)}]: "))
        m += -1
    print(f"-- Levantamento do jogador {time[m]['Jogador']}")
    for p, g in enumerate(time[m]['Gols']):
        print(f"    No jogo {p+1} fez {g} Gols.")
    print("-"*50)
    r = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
    print("-"*50)
    while r not in "SN":
        r = str(input("Dados Invalido!! continuar[S/N]: ")).strip().upper()[0]
    if r == "N":
        7
        break
print("PROGRAMA ENCERRADO!!!")
