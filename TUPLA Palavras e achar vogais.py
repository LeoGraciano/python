p = ("Aprender", "Programa", "Linguagem",
     "Python", "curso", "Grátis", "Estudar", "Praticar",
     "Trabalhar", "Mercado", "Programador", "Futuro")
for v in p:
    print(f"\nNa palavra {v} temos ", end="")
    for letra in v:
        if letra.lower() in "aeiouáâàãéêéíôóõú":
            print(letra.lower(), end=" ")
