qnt = t = 0
n = int(
    input("Digite um valores para ser tirado a media, para digite [999]: "))
while n != 999:
    t += n
    qnt += 1
    n = int(
        input("Digite um valores para ser tirado a media, para digite [999]: "))
print(f"A soma dos {qnt} números é {t} e a media foi {t/qnt:.1f}")
