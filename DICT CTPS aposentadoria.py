from datetime import datetime
dados = dict()
dados["Nome"] = str(input("Nome: ")).strip().title()
a = int(input("Ano de nascimento: "))
dados["Idade"] = datetime.now().year - a
dados["CTPS"] = int(input("Numero da carteira de Trabalho (0 não tem): "))
if dados["CTPS"] != 0:
    dados["Contração"] = int(input("Ano de contração: "))
    dados["Salário"] = float(input("Salário Atual: R$"))
    dados["Aposentadoria"] = (
        35-(datetime.now().year - dados["Contração"]))+dados['Idade']
for k, v in dados.items():
    print(f"  -{k} tem valor {v}")
