#importando o sqlit

import sqlite3

#criando a conexão

#CRUD - create, read, update, delete

con = sqlite3.connect('cavalo.bd')

#criando a tabela

with con:
    cur = con.cursor()  
    cur.execute("CREATE TABLE cavalo(id INTEGER PRIMARY KEY AUTOINCREMENT, frota NUMERIC, placa TEXT, nome TEXT, eixo NUMERIC, ptb NUMERIC)")
    