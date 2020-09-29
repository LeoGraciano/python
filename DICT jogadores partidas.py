dados = {}
gols = []
dados["Jogador"] = str(input("Qual nome do Jogador: ")
                       ).strip().title().split()[0]
p = int(input("Quants partidas ele jogou: "))
for c in range(1, p+1):
    gol = int(input(f"  Quantos gols foram marcado na {c}° Partida: "))
    gols.append(gol)
dados["Gols"] = gols[:]
dados["Total"] = sum(gols)
print("-="*20)
for k, v in dados.items():
    print(f"O Campo {k} tem valor {v}")
print("-="*20)
print(f"O jogador {dados['Jogador']} jogou {p} partidas.")
for c in range(1, p+1):
    if gols[c-1] > 0:
        print(f"  => Na {c}° partida , ele fez {gols[c-1]} Gols")
print(f"Foi um total de {sum(gols)} gols")
