from datetime import date
a = int(input("Qual seu ano de nascimento: "))
al = date.today().year - a
if al == 18:
    print ('Esse ano é do seu alistamento.')
elif al > 18:
    print (f"Já passou {al-18} ano(s) do prazo.")
else:
    print(f"Você é muito jovem para se alistar, aguarde {18-al} anos.")