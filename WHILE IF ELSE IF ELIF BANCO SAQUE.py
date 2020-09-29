v = str(input("VALOR DO SAQUE: R$")).strip()
while v.isnumeric() == False:
    v = str(input("VALOR INVÁLIDO, DIGITE NOVAMENTE: R$")).strip()
v = (int(v))
nts = 50
qntn = 0
ttl = v
while True:
    if ttl >= nts:
        ttl -= nts
        qntn += 1
    else:
        if qntn > 0:
            print(f"Total de {qntn} cédulas de R$ {nts}")
        if nts == 50:
            nts = 20
        elif nts == 20:
            nts = 10
        elif nts == 10:
            nts = 5
        elif nts == 2:
            nts = 1
        qntn = 0
        if ttl == 0:
            break
print("VOLTE SEMPRE!!")
