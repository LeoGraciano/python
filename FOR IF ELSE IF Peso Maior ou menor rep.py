M = 0
m = 0
for r in range(1, 6):
    p = float(input(f"Qual da {r}° peso(kg) deseja inserir: "))
    if r == 1:
        M = p
        m = p
    else:
        if p > M:
            M = p
        if p < m:
            m = p
print(f"O maior peso é {M}kg e menor peso é {m}kg.")
