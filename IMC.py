ps = float(input("Qual seu peso(Kg): "))
at = float(input("Qual sua altura(m): "))
imc = ps / (at**2)
c = ()
if imc < 18.5:
    c = "Abaixo do Peso"
elif imc >= 18.5 and imc<=25:
    c = "Peso ideal"
elif imc > 25 and imc<=30:
    c = "Sobrepeso"
elif imc > 30 and imc<=40:
    c = "Obsidade"
elif imc > 40:
    c = "Obesidade mórbida"
msg = f"Você tem {imc:.1f} de IMC, você esta {c}."
print (msg)