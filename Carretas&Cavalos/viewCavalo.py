# importando o sqlite
import  sqlite3

#crineo conexão
#CRUD create, read, update, dalete

con = sqlite3.connect('cavalo.db')

#inserino dados na tabela
#inserio dados dos cavalos
def inserirCavalos(i):
    with con:
        cur=con.cursor()
        query = "INSERT INTO cavalo(frota, placa, nome, eixo, ptb) VALUES (?,?,?,?,?)"
        cur.execute(query,i )

def updateCavalos(u):
    with con:
        cur=con.cursor()
        query = "UPDATE cavalo SET frota=?, placa=?, nome=?, eixo=?, ptb=? WHERE id=?"
        cur.execute(query,u)

def deletarCavalos(d):
    with con:
        cur=con.cursor()
        query = "DELETE FROM cavalo WHERE id=?"
        cur.execute(query,d)

def verCavalos():
    verCavalos=[]
    with con:
        cur=con.cursor()
        query = "SELECT * FROM cavalo"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            verCavalos.append(row)
    return verCavalos       

def verCavalosIndividuais(frota):
    verCavalosIndividuais=[]

    with con:
        cur=con.cursor()
        query = "SELECT * FROM cavalo WHERE frota = ?"
        cur.execute(query,frota)

        rows = cur.fetchall()
        for row in rows:
            verCavalosIndividuais.append(row)
    return verCavalosIndividuais    
