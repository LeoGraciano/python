aluno = dict()
aluno["Nome"] = str(input("Nome: ")).strip().title()
aluno["Média"] = eval(input(f"Média do {aluno['Nome']}: "))
if aluno['Média'] >= 7:
    aluno['Situação'] = "APROVADO"
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = "RECUPERAÇÃO"
else:
    aluno['Situação'] = "REPROVADO"
print("-="*20)
for v, k in aluno.items():
    print(f"   - {v} é igual {k}")
