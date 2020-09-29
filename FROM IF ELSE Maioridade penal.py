from datetime import date
qM = 0
qm = 0
n = 0
for i in range (0,6):
    n += 1 
    an = int(input(f"Qual {n}° ano de Nascimento: "))
    id = date.today().year - an
    if id >= 21:
      qM += 1
    else:        
        qm += 1
if qM > 1:
  pM = "pessoas"
else:
  pM = "pessoa"
if qm > 1:
  pm = "pessoas"
else:
  pm = "pessoa"
print (f"Tem {qM} {pM} de maior") 
print (f"Tem {qm} {pm} de menor")