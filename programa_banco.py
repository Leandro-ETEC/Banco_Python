import mysql.connector #pip install mysql-connector
try:
    dados_banco = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345678",
        database = "banco_corredor"
    )
except:
    print("Não conectou ao banco!")
minha_conexao = dados_banco.cursor()
x = str(1) #Variável texto = 1, str é casting para string
while x != '0': #
    while True:
        dados_corredor = [] #vetor ou array (2 dimensões!)
        while True:
            nome_corredor = str(input("informe o nome do atleta: ")) #input = system.out Java
            if not nome_corredor:
                print("Inserir um nome válido!")
                continue   
            else:
                dados_corredor.append(str(nome_corredor).upper()) #append envia pro vetor
                break                                             #.upper() força palavra maiúscula
        sobrenome_corredor = str(input("informe o sobrenome do atleta: "))
        dados_corredor.append(str(sobrenome_corredor).upper())
        print("Nome %s armazenado com sucesso", nome_corredor)
        print("Nome %s armazenado com sucesso", sobrenome_corredor)
        confirmacao = str(input("(1) confirma (0) corrige"))
        while confirmacao != 0:
            confirmacao = str(input("(1) continuar (0) sair"))
            break
        if dados_corredor[1]:
            try:
                comando_insert = "INSERT INTO tabela_corredor VALUES(default, %s, %s)"
                variaveis = (dados_corredor[0], dados_corredor[1])
                minha_conexao.execute(comando_insert, variaveis)
            except:
                print("Não fez o insert!")
            finally:
                dados_banco.commit()
        else:
            print("Nada inserido no vetor!")
        x = str(input("Digite 1 para continuar ou 0 para sair"))

        while x !=0 and x != 1:
            x = str(input("Digite 1 para continuar ou 0 para sair"))
minha_conexao.close()