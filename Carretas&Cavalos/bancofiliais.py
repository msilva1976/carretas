#immportando o SQLite
import sqlite3 

#criando a conexao com o banco de dados

con = sqlite3.connect('filial.bd')

# criando a tabela

with con:
    cur = con.cursor()
    cur.execute ("CREATE TABLE filiais( id	INTEGER PRIMARY KEY AUTOINCREMENT, codigo	NUMERIC,	filial	TEXT)")

    
    
#CREATE TABLE "carretas" ("id"	INTEGER,	"frota"	NUMERIC,	"placa"	TEXT,	"capacidade"	NUMERIC,	"eixo"	NUMERIC,	"PTB"	NUMERIC,	"empresa"	TEXT,	"codigo"	NUMERIC,	"cnpj"	NUMERIC,	PRIMARY KEY("id" AUTOINCREMENT))bancofiliais.py