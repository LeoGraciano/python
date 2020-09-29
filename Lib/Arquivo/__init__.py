from Lib.Interface import *


def arqexist(NOME):
    try:
        A = open(NOME, "rt")
        A.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaarq(NOME):
    try:
        A = open(NOME, "wt+")
        A.close()
    except:
        print("Hove um ERRO na criação do arquivo")
    else:
        print(f"Arquivo {NOME} criado com sucesso.")


def lerarq(NOME):
    try:
        A = open(NOME, "rt")
    except:
        print("ERRO AO LER ARQUIVO!!!")
    else:
        tit("PESSOAS CADASTRADAS")
        for L in A:
            DADOS = L.split(";")
            DADOS[1] = DADOS[1].replace("\n", "")
            print(f"{DADOS[0]:.<30} {DADOS[1]:>3} anos")
    finally:
        A.close()


def cadastra(ARQ, NOME="desconhecido", IDADE=0):
    try:
        A = open(ARQ, "at")
    except:
        print("Houve um ERRO na abertura do arquivo")
    else:
        try:
            A.write(f"{NOME};{IDADE}\n")
        except:
            print("Houve um ERRO na hora de escrever os Dados!!")
        else:
            print(f"Novo Registro de {NOME} Adcionado")
            A.close()
