n = eval(input("Digite um numero: "))
print('''Escolha uma base da conversão:
[1] converter para BINÁRIO
[2] converte para OCTAL
[3] converte para HEXADECIMAL''')
o = int (input("Sua opção: "))
if o == 1:
    nc=bin(n)
    nu="BINÁRIO"
elif o == 2:
    nc=oct(n)
    nu="OCTAL"
elif o == 3:
    nc=hex(n)
    nu="HEXADECIMAL"
print (f"{n} convertido em {nu} é igual a {nc}")
if o > 3:
    print("Numero inválido")
