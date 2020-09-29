import math
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
l9 = []
par = []
for lin1 in range(0, 3):
    n = int(input(f"Digite o valor [0,{lin1+1}]: "))
    if lin1 == 0:
        l1.append(n)
    elif lin1 == 1:
        l2.append(n)
    elif lin1 == 2:
        l3.append(n)
    if n % 2 == 0:
        par.append(n)
for lin2 in range(0, 3):
    n = int(input(f"Digite o valor [1,{lin2+1}]: "))
    if lin2 == 0:
        l4.append(n)
    elif lin2 == 1:
        l5.append(n)
    elif lin2 == 2:
        l6.append(n)
    if n % 2 == 0:
        par.append(n)
for lin3 in range(0, 3):
    n = int(input(f"Digite o valor [2,{lin3+1}]: "))
    if lin3 == 0:
        l7.append(n)
    elif lin3 == 1:
        l8.append(n)
    elif lin3 == 2:
        l9.append(n)
    if n % 2 == 0:
        par.append(n)
print(f'''-=-=-=-=-=-=-=-=
{l1} {l2} {l3}
{l4} {l5} {l6}
{l7} {l8} {l9}
-=-=-=-=-=-=-=-=''')
#print(f"A soma dos numeros Pares é: {(l1,l2,l3,l4,l5,l6,l7,l8,l9) % 2== 0}")
print(f"A soma das Terceira Coluna é {sum(l3+l6+l9)}")
print(f"O Maior valor da segunda coluna é {max(l4,l5,l6)}")
