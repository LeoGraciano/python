from modulos import moeda

p = float(input("Qual preço do Produto: R$ "))
print(f"O preço em dobro é {moeda.dobro(p,True)}")
print(f"Dividindo pela metade ficara {moeda.metade(p,True)}")
print(f"Aumentando o preço em 13% ficara {moeda.aumentar(p,13,True)}")
print(f"Diminuindo o preço de 13% ficara {moeda.diminuir(p, 13,True)}")
