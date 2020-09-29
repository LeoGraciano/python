def ficha(J="Desconhecido", G=0,):
    print(f"Jogador {J} Marcou {G} gols no campeonato")


# PROGRAMA PRINCIPAL
n = str(input("Nome do Jogador: ")).strip().title()
g = str(input("Gols Marcados: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(G=g)
else:
    ficha(n, g)
