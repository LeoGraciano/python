from datetime import datetime


def cadastro_clientes():
    print(' =-=-=-Cadastro do Cliente-=-=-=')
    cpf = int(input(' Informe CPF:'))
    nome = str(input(' Informe o nome:'))
    rg = int(input(' Informe RG:'))
    # criando o dicionario
    dados_clientes = {}
    # organizando o dicionario
    dados_clientes[cpf] = [nome, rg]
    # salvando no arquivo csv.
    salvar_csv = open('clientes.csv', 'a')
    salvar_csv.write(f'{nome};{rg};{cpf}\n')
    salvar_csv.close()
    """
    Um print na tela, no final de todo processo, para ter certeza 
    que a função por completo foi concluida.
    """
    print(' =-=-=-Cadastro Realizado!-=-=-=')


def cadastro_filmes():
    print(' =-=-=-Cadastro de Filmes-=-=-=')
    codigo = str(input(' Informe codigo do Filme:'))
    tipo = str(input(' DVD ou FITA ?'))
    titulo = str(input(' Informe nome do Filme:'))
    ano = int(input(' Informe ano de lançamento:'))
    # criando o dicionario
    dados_filmes = {}
    # organizando o dicionario
    dados_filmes[codigo] = [tipo, titulo, ano]
    # salvando no arquivo csv.
    salvar_csv = open('filmes.csv', 'a')
    salvar_csv.write(f'{codigo};{tipo};{titulo};{ano}\n')
    salvar_csv.close()
    """
    Um print na tela, no final de todo processo, para ter certeza 
    que a função por completo foi concluida.
    """
    print(' =-=-=-Cadastro Realizado!-=-=-=\n')


def alocacao_filmes():
    print(' =-=-=-Registrando Alocação-=-=-=')
    nome = str(input(' Informe nome do locatario:'))
    codproduto = int(input(' Indorme Codigo do filme alugado:'))
    data = datetime.now()
    data_alugado_str = data.strftime(' %d/%m/%Y')
    print('Dia da locação:', data_alugado_str)

    dados_alocacao = {}
    dados_alocacao[codproduto] = [nome, data_alugado_str]

    salvar_csv = open('emprestimos.csv', 'a')
    salvar_csv.write(f'{codproduto};{nome};{data_alugado_str}\n')
    salvar_csv.close

    print('Locação concluida com sucesso!')


def atrasadinhos():
    clientes = open('clientes.csv', 'r')
    filmes = open('filmes.csv', 'r')
    emprestimos = open('emprestimos.csv', 'r')

    clientes = clientes.readlines()
    filmes = filmes.readlines()
    emprestimos = emprestimos.readlines()

    quantidade_dias = 0
    # pegar data de hoje
    data_hoje = datetime.now()
    data_hoje = str(data_hoje)
    data_hoje = data_hoje[:10]
    ano_hoje, mes_hoje, dia_hoje = data_hoje.split('-')

    # verificar emprestimos
    cpf_atual = 0
    nome_filme_atual = ''
    print('CPF Nome Título Empréstimo Situação Dias')
    for item in emprestimos:
        id_filme, nome_atual, data_atual = item.split(';')
        dia, mes, ano = data_atual.split('-')

        # 2020               2019
        if int(ano_hoje) > int(ano):
            quantidade_dias += (int(ano_hoje) - int(ano)) * 365
            # maio 05     julho 07
            if (int(mes_hoje) - int(mes)) > 0:
                quantidade_dias += int(mes_hoje) - int(mes) * 30
                if int(dia_hoje) < int(dia):  # mesmo ano meses diferentes dia de hoje menor
                    quantidade_dias += int(dia) - int(dia_hoje)
                elif int(dia_hoje) > int(dia):  # mesmo ano meses diferentes dia de hoje maior
                    quantidade_dias -= int(dia_hoje) - int(dia)

            elif (int(mes_hoje) - int(mes)) < 0:
                quantidade_dias -= abs(int(mes_hoje) - int(mes)) * 30
                if int(dia_hoje) < int(dia):  # mesmo ano meses diferentes dia de hoje menor
                    quantidade_dias += int(dia) - int(dia_hoje)
                elif int(dia_hoje) > int(dia):  # mesmo ano meses diferentes dia de hoje maior
                    quantidade_dias -= int(dia_hoje) - int(dia)

            elif int(mes_hoje) == int(mes):
                if int(dia_hoje) > int(dia):  # MESMO ANO E MES MAS DIAS DIFERENTES
                    quantidade_dias = int(dia_hoje) - int(dia)

        elif int(ano_hoje) == int(ano):
            # 08-13               #06-06
            if int(mes_hoje) > int(mes):  # mesmo ano meses diferentes
                quantidade_dias += (int(mes_hoje) - int(mes)) * 30

                if int(dia_hoje) < int(dia):  # mesmo ano meses diferentes dia de hoje menor
                    quantidade_dias += int(dia) - int(dia_hoje)
                elif int(dia_hoje) > int(dia):  # mesmo ano meses diferentes dia de hoje maior
                    quantidade_dias -= int(dia_hoje) - int(dia)

            elif int(mes_hoje) == int(mes):
                if int(dia_hoje) > int(dia):  # MESMO ANO E MES MAS DIAS DIFERENTES
                    quantidade_dias = int(dia_hoje) - int(dia)


####### PARTE IMPORTANTE #######
        # quantidade_dias = 6
        if quantidade_dias > 7:
            for cliente in clientes:
                nome, rg, cpf = cliente.split(';')
                if nome_atual == nome:
                    cpf_atual = cpf
                    break
            for filme in filmes:
                id_agora, _, nome, _ = filme.split(';')

                if id_agora == id_filme:
                    nome_filme_atual = nome
                    break
            print(
                f'{cpf_atual}|{nome_atual}|{nome_filme_atual}|{data_atual}|atrasado|{quantidade_dias}')


atrasadinhos()
