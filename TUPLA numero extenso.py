ne = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze",
      "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    n = int(input("Digite um número de 0 a 20: "))
    while n not in range(0, 21):
        n = int(input("Valor Incorreto: Digite um número de 0 a 20: "))
#    if n >= 0 and n <= 20:
#        break
    print(f"Você digitou o número: {ne[n]}")
