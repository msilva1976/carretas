import pandas as pd
import sqlite3

# 1. Ler o arquivo Excel
df = pd.read_excel('C:\\Users\\marco\\OneDrive\\Documentos\\carretas.xlsx', sheet_name='Planilha1')  # Substitua 'Planilha1' pelo nome da sua planilha, se necessário

# 2. Conectar ao banco de dados SQLite (cria o arquivo se não existir)
conn = sqlite3.connect('cavalo.db')

# 3. Carregar dados para o SQLite
# 'if_exists' pode ser 'replace' (substitui) ou 'append' (adiciona)
df.to_sql('cavalo', conn, if_exists='replace', index=False)

# 4. Fechar conexão
conn.close()

#C:\Users\marco\OneDrive\Documentos\CARRETAS_E_CAVALOS V21    MSILVA 3.xlsm
#"C:\Users\marco\OneDrive\Documentos\carretas.xlsx"