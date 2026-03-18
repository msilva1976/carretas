# inportando o sqlit
import sqlite3 

# criando a conexão
# CRUD - create, read, update, delete
con = sqlite3.connect('veiculos.bd')




#inserir dados na tabela

def inserir_dados(i):
    #inserino dados na tabela
    with con:
        cur=con.cursor()
        #query = "INSERT INTO carreta( frota, placa, capacidade, eixo, PTB, empresa, codigo, cnpj) VALUES (?,?,?,?,?,?,?,?)"
        query = "INSERT INTO carreta( frota, placa, capacidade, eixo, ptb) VALUES (?,?,?,?,?)"
        cur.execute(query, i)

#update_dados
def update_dados(u):
    with con:
        cur=con.cursor()
        query = "UPDATE carreta SET frota=?, placa=?,capacidade=?, eixo=?, ptb=? WHERE id=?"
        cur.execute(query, u)


#deletar dados
def deletar_dados(d):
    with con:
        cur=con.cursor()
        query = "DELETE FROM carreta WHERE id=?"
        cur.execute(query,d)
        

#ver dados
def ver_dados():
#dados da tabela
    ver_dados=[]
    #ver dados inserido
    with con:
        cur = con.cursor()
        query = "SELECT * FROM carreta"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados        


#ver dados individuais
def ver_dados_individuais(frota):
    ver_dados_individuais=[]

    #ver dados inseridos
    with con:
        cur=con.cursor()
        query = "SELECT * FROM carreta WHERE frota = ?"
        cur.execute(query,frota)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individuais.append(row)


