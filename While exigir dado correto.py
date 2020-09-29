sex = str(input("Qual seu Sexo: [M/F] ")).strip().upper()[0]
while sex not in "MF":
    sex = str(input("Dados Inválidos informe o sexo[M/F]: ")).strip().upper()[0]
print (f"Sexo {sex} registrado com sucesso.")