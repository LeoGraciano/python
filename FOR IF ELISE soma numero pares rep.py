s = 0
q = 0
for c in range(1,7):
    n = int(input(f"Digite o {c}° valor: "))
    if n % 2 == 0:
        s+= n
        q+= 1
if q > 1:
    p = "pares"
else:
    p = "par"
print (f"Você digitou {q} {p} e a soma dos numeros pares é: {s}")
