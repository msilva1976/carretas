# inportando o sqlit
import sqlite3 

# criando a conexão
# CRUD - create, read, update, delete
con = sqlite3.connect('industrial.bd')




#inserir dados na tabela

def inserir_dados_industrial(i):
    #inserino dados na tabela
    with con:
        cur=con.cursor()
        #query = "INSERT INTO carreta( frota, placa, capacidade, eixo, PTB, empresa, codigo, cnpj) VALUES (?,?,?,?,?,?,?,?)"
        query = "INSERT INTO industria( codigo, filial) VALUES (?,?)"
        cur.execute(query, i)

#update_dados
def update_dados_industrial(u):
    with con:
        cur=con.cursor()
        query = "UPDATE industria SET codigo=?, filial=? WHERE id=?"
        cur.execute(query, u)


#deletar dados
def deletar_dados_industrial(d):
    with con:
        cur=con.cursor()
        query = "DELETE FROM industria WHERE id=?"
        cur.execute(query,d)
        

#ver dados
def ver_dados_industrial():
#dados da tabela
    ver_dados=[]
    #ver dados inserido
    with con:
        cur = con.cursor()
        query = "SELECT * FROM industria"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados        


#ver dados individuais
def ver_dados_individuais_industrial(frota):
    ver_dados_individuais=[]

    #ver dados inseridos
    with con:
        cur=con.cursor()
        query = "SELECT * FROM industria WHERE codigo = ?"
        cur.execute(query,frota)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individuais.append(row)


