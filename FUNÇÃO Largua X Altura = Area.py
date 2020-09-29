def area(A, B):
    p = A*B
    print(f"A área de um terreno de {A}x{B} é de {p}m².")


print(f"{'CONTROLE DE TERRENO':^5}")
print("-"*30)
a = eval(input("    Qual Altura (m): "))
l = eval(input("    Qual Largura (m): "))
area(a, l)
