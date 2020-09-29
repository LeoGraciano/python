from os import replace


def leiaint(MSG):
    while True:
        try:
            V = int(input(MSG))
        except (ValueError, TypeError):
            print("\033[31mERRO!! Digite um valor inteiro valido\033[m")
        except KeyboardInterrupt:
            print("\nUsuário preferiu não digitar o valor")
            return ""
        else:
            return V


def leiafloat(MSG):
    while True:
        try:
            t = str(input(MSG)).replace(",", ".")
            V = float(t)
        except (ValueError, TypeError):
            print("\033[31mERRO!! Esse Dado não é numero Real\033[m")
        except KeyboardInterrupt:
            print("\nUsuário preferiu não digitar o valor")
            return ""
        else:
            return f"{V:.2f}".replace(".", ",")


i = leiaint("Digite um numero Inteiro: ")
f = leiafloat("Digite um número Real: ")
print(f"Você digitou Numeros: \n\tInteiro: {i}\n\tReal: {f}")
