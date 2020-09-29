from datetime import date
an = int(input("Qual seu ano de Nascimento: "))
fc = date.today().year-an 
if fc <= 9 and fc > 3:
    c = "Mirim"
elif fc <= 14 and fc > 9:
    c = "Infantil"
elif fc <=19 and fc > 14:
    c = "Junior"
elif fc <=20 and fc > 19:
    c = "Senior"
elif fc > 20:
    c = "Master"
    msg = f"Você esta na categoria {c}, pois você tem {fc} anos"
    print (msg)
else:
    print ("Infelizmente você não tem idade para começar.")
