#immportando o SQLite
import sqlite3 

#criando a conexao com o banco de dados

con = sqlite3.connect('carretas.db')

# criando a tabela

with con:
    cur = con.cursor()
    cur.execute ("CREATE TABLE carreta( id	INTEGER PRIMARY KEY AUTOINCREMENT, frota	NUMERIC,	placa	TEXT,	capacidade	NUMERIC,	eixo	NUMERIC,	PTB	NUMERIC,	empresa	TEXT,	codigo	NUMERIC,	cnpj	NUMERIC)")

    
    
#CREATE TABLE "carretas" ("id"	INTEGER,	"frota"	NUMERIC,	"placa"	TEXT,	"capacidade"	NUMERIC,	"eixo"	NUMERIC,	"PTB"	NUMERIC,	"empresa"	TEXT,	"codigo"	NUMERIC,	"cnpj"	NUMERIC,	PRIMARY KEY("id" AUTOINCREMENT))