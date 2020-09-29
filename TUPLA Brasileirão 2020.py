br2020 = ("Atlético - MG", "Vasco da Gama", "Internacional", "Bahia",
          "Atlético - PR",  "Grêmio", "Atlético - GO", "Santos", "Fluminense",
          "Sport Recife", "São Paulo", "Flamengo", "Palmeiras", "Botafogo",
          "Bragantino - SP", "Corinthians", "Goiás", "Ceará - SC", "Fortaleza",
          "Curitiba")
print(f"Os 5 primeiros colocados:\n {br2020[:5]}")
print("-="*20)
print(f"Os 4 últimos Colocados:\n {br2020[-4:]}")
print("-="*20)
print(f"Os time em ordem Alfabética:\n {sorted(br2020)}")
print("-="*20)
# print("O Flamento esta na {}ª Posição".format(br2020.index("Flamengo")))
# print("-="*20) #f"{}" Não funciona com index dentro de um contexto necessita
# usar aspas simples.
print(f"O Flamento esta na {br2020.index('Flamengo')+1}° Posição")
