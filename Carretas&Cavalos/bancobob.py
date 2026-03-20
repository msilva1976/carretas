#immportando o SQLite
import sqlite3 

#criando a conexao com o banco de dados

con = sqlite3.connect('bob.bd')

# criando a tabela

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE bob(id INTEGER PRIMARY KEY AUTOINCREMENT, frota	NUMERIC,	placa	TEXT,PTB	NUMERIC)")

    
    
#CREATE TABLE "carretas" ("id"	INTEGER,	"frota"	NUMERIC,	"placa"	TEXT,	"capacidade"	NUMERIC,	"eixo"	NUMERIC,	"PTB"	NUMERIC,	"empresa"	TEXT,	"codigo"	NUMERIC,	"cnpj"	NUMERIC,	PRIMARY KEY("id" AUTOINCREMENT))