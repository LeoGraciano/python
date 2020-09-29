f = str(input("Digite uma frase: ")).strip().upper()
ff = f.split()
fj = "".join(ff)
fi = ''
for l in range(len(fj) -1, -1, -1):
    fi +=fj[l] 
if fi == f:
    print (f,fi)
    print("Essa frase é uma Palíndromo.")
else:
    print (f,fi)
    print ("Não é um Palíndromo.")

