# inportando o sqlit
import sqlite3 

# criando a conexão
# CRUD - create, read, update, delete
con = sqlite3.connect('bob.bd')




#inserir dados na tabela

def inserir_dados_bob(i):
    #inserino dados na tabela
    with con:
        cur=con.cursor()
        #query = "INSERT INTO bob( frota, placa,PTB, empresa, codigo, cnpj) VALUES (?,?,?,?,?,?,?,?)"
        query = "INSERT INTO bob( frota, placa, ptb) VALUES (?,?,?)"
        cur.execute(query, i)

#update_dados
def update_dados_bob(u):
    with con:
        cur=con.cursor()
        query = "UPDATE bob SET frota=?, placa=?, ptb=? WHERE id=?"
        cur.execute(query, u)


#deletar dados
def deletar_dados_bob(d):
    with con:
        cur=con.cursor()
        query = "DELETE FROM bob WHERE id=?"
        cur.execute(query,d)
        

#ver dados
def ver_dado_bobs():
#dados da tabela
    ver_dados=[]
    #ver dados inserido
    with con:
        cur = con.cursor()
        query = "SELECT * FROM bob"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados        


#ver dados individuais
def ver_dados_individuais_bob(frota):
    ver_dados_individuais=[]

    #ver dados inseridos
    with con:
        cur=con.cursor()
        query = "SELECT * FROM carreta WHERE bob = ?"
        cur.execute(query,frota)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individuais.append(row)


