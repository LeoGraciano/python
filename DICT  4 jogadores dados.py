from random import randint
from time import sleep
from operator import itemgetter
ply = dict()
rank = []
for c in range(1, 5):
    dados = randint(1, 6)
    ply[f"Jogador {c}"] = dados
print(" == Valores jogadores ==")
for k, v in ply.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
# itemgetter(1) Seria VALOR se fosse itemgetter(0) Sera CHAVE
rank = sorted(ply.items(), key=itemgetter(1), reverse=True)
print(" == Ranking dos jogadores ==")
for i, v in enumerate(rank):
    print(f"{i+1}° lugar {v[0]} com {v[1]}")
    sleep(1)
