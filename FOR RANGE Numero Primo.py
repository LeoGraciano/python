qp = 0
n = int(input("Digite um numero: "))
for p in range(1,n+1): 
    if n % p == 0:
        qp += 1
if qp == 2:
    print ("Esse numero é primo")
else:
    print ("Esse numero não é primo.")