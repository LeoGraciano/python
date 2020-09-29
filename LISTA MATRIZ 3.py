mtz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = nmx = sl = 0
for l in range(0, 3):
    for c in range(0, 3):
        mtz[l][c] = int(input(f"Digite o valor [{l},{c}]: "))
        if mtz[l][c] % 2 == 0:
            spar += mtz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{mtz[l][c]:^5}]", end="")
    print()
print(f"A soma dos números pares é: {spar}")
print(f"A sola terceira coluna é: {mtz[0][2]+mtz[1][2]+mtz[2][2]}")
print(f"O maior numero da segunda linha é: {max(mtz[1])}")
