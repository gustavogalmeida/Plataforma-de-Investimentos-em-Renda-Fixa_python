import mysql.connector
from mysql.connector import errorcode

print("Conectando ao banco de dados...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("USE `db_plataforma_investimentos`;")

# Limpar a tabela antes de inserir novos dados
cursor.execute("DELETE FROM faixas_lca_pre")

# alimentando tabelas
faixas_lca_pre_sql = 'INSERT INTO faixas_lca_pre (valor_minimo, valor_maximo, taxa, dias_liquidez, dias_vencimento) VALUES (%s, %s, %s, %s, %s)'
faixas_lca_pre = [
      (5000.00, 499999.99, 8.5, 276, 370),
      (500000.00, 99999999.99, 9.35, 276, 370),
      (5000.00, 499999.99, 8.63, 360, 370),
      (500000.00, 99999999.99, 9.54, 360, 370),
]
cursor.executemany(faixas_lca_pre_sql, faixas_lca_pre)

# testando o que foi inserido
cursor.execute('select * from db_plataforma_investimentos.faixas_lca_pre')
print(' -------------  Faixas LCA Prefixada:  -------------')
for faixa in cursor.fetchall():
    print("ID: {}, Valor mínimo: {:.2f}, Valor máximo: {:.2f}, Taxa: {:.2f}, Dias de liquidez: {}, Dias de vencimento: {}".format(faixa[0], faixa[1], faixa[2], faixa[3], faixa[4], faixa[5]))

conn.commit()

cursor.close()
conn.close()