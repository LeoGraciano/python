from Lib.Interface import *
from time import sleep
from Lib.Arquivo import *

arq = "DadosPessoas.txt"

if not arqexist(arq):
    criaarq(arq)


while True:
    m = menu(["Lista Pessoas", "Cadastra Pessoas", "Sair"])
    if m == 1:
        tit("LISTA PESSOAS")
        lerarq(arq)
    elif m == 2:
        tit("CADASTRA PESSOAS")
        n = str(input("Nome: ")).strip().title()
        i = leiaint("Idade: ")
        cadastra(arq, n, i)
    elif m == 3:
        tit("SAIR DO SISTEMA ATÉ LOGO!!!")
        break
    else:
        tit("\t\033[31mDIGITE UMA OPÇÃO VALIDA\033[m")
        sleep(2)
