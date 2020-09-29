idH = 0
nv = ""
qntM = 0
mdi = 0
pm = "mulher está "
for c in range(1,5):
    print ("-"*5,f" {c}° Pessoa ","-"*5) 
    n = str(input(f"NOME: ")).strip().capitalize().split()[0]
    ida = int(input(f"IDADE: "))
    sex = str(input("SEXO[M/F]: ")).strip().upper()
    mdi+= ida
    if  sex == "M" and ida > idH:
         idH = ida
         nv = n
    elif sex == "F":
        if ida <= 20:
            qntM += 1
            if qntM > 1:
                pm = "Mulheres estão"
    else:
        sex != "M" and sex != "F"
        print("Digito Gênero Errado!!!!")
print (f"A media de idade grupo é: {mdi/4}")
print (f"O homem mais velho tem {idH} anos e seu nome é {nv}")
print (f"Existe {qntM} {pm} a baixo dos 20 anos.")