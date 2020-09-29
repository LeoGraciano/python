from modulos import moeda
p = moeda.leiadin("Preço do Produto: R$")
a = moeda.leiadin("Acrescimo (%): ")
d = moeda.leiadin("Desconto (%): ")

moeda.resumido(p, a, d)
