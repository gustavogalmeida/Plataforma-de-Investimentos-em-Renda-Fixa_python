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



################ Alimentando tabelas ##############
#### LCA PRE 276 ####
cursor.execute("DELETE FROM politica_lca_pre_276")
politica_lca_pre_276_sql = 'INSERT INTO politica_lca_pre_276 (valor_minimo, valor_maximo, taxa, dias_liquidez, dias_vencimento) VALUES (%s, %s, %s, %s, %s)'
politica_lca_pre_276 = [
      (5000.00, 499999.99, 8.5, 276, 370),
      (500000.00, 99999999.99, 9.35, 276, 370),
]
cursor.executemany(politica_lca_pre_276_sql, politica_lca_pre_276)

#### LCA PRE 360 ####
cursor.execute("DELETE FROM politica_lca_pre_360")
politica_lca_pre_360_sql = 'INSERT INTO politica_lca_pre_360 (valor_minimo, valor_maximo, taxa, dias_liquidez, dias_vencimento) VALUES (%s, %s, %s, %s, %s)'
politica_lca_pre_360 = [
      (5000.00, 499999.99, 8.63, 360, 370),
      (500000.00, 99999999.99, 9.54, 360, 370),
]
cursor.executemany(politica_lca_pre_360_sql, politica_lca_pre_360)

#### RDC PRE 181 ####
cursor.execute("DELETE FROM politica_rdc_pre_181")
politica_rdc_pre_181_sql = 'INSERT INTO politica_rdc_pre_181 (valor_minimo, valor_maximo, taxa, dias_liquidez, dias_vencimento) VALUES (%s, %s, %s, %s, %s)'
politica_rdc_pre_181 = [
      (1.00, 499999.99, 9.2, 181, 370),
      (500000.00, 99999999.99, 10.05, 181, 370),
]
cursor.executemany(politica_rdc_pre_181_sql, politica_rdc_pre_181)

#### RDC PRE 361 ####
cursor.execute("DELETE FROM politica_rdc_pre_361")
politica_rdc_pre_361_sql = 'INSERT INTO politica_rdc_pre_361 (valor_minimo, valor_maximo, taxa, dias_liquidez, dias_vencimento) VALUES (%s, %s, %s, %s, %s)'
politica_rdc_pre_361 = [
      (1.00, 499999.99, 9.33, 361, 370),
      (500000.00, 99999999.99, 10.24, 361, 370),
]
cursor.executemany(politica_rdc_pre_361_sql, politica_rdc_pre_361)

#### RDC Flexível ####
cursor.execute("DELETE FROM politica_rdc_flexivel")
politica_rdc_flexivel_sql = 'INSERT INTO politica_rdc_flexivel (valor_minimo, valor_maximo, taxa, dias_liquidez, dias_vencimento) VALUES (%s, %s, %s, %s, %s)'
politica_rdc_flexivel = [
      (1.00, 49999.99, 95.00, 0, 5000),
      (50000.00, 149999.99, 96.00, 0, 5000),
      (150000.00, 299999.99, 97.00, 0, 5000),
      (300000.00, 499999.99, 98.00, 0, 5000),
      (500000.00, 99999999.99, 100.00, 0, 5000),
]
cursor.executemany(politica_rdc_flexivel_sql, politica_rdc_flexivel)


#### LCA Pós 276 ####
cursor.execute("DELETE FROM politica_lca_pos_276")
politica_lca_pos_276_sql = 'INSERT INTO politica_lca_pos_276 (valor_minimo, valor_maximo, taxa, dias_liquidez, dias_vencimento) VALUES (%s, %s, %s, %s, %s)'
politica_lca_pos_276 = [
      (5000.00, 49999.99, 87.00, 276, 730),
      (50000.00, 149999.99, 90.00, 276, 730),
      (150000.00, 299999.99, 92.00, 276, 730),
      (300000.00, 499999.99, 94.00, 276, 730),
      (500000.00, 999999.99, 96.00, 276, 730),
      (1000000.00, 99999999.99, 97.00, 276, 730),
]
cursor.executemany(politica_lca_pos_276_sql, politica_lca_pos_276)

#### LCA Pós 360 ####
cursor.execute("DELETE FROM politica_lca_pos_360")
politica_lca_pos_360_sql = 'INSERT INTO politica_lca_pos_360 (valor_minimo, valor_maximo, taxa, dias_liquidez, dias_vencimento) VALUES (%s, %s, %s, %s, %s)'
politica_lca_pos_360 = [
      (5000.00, 49999.99, 89.00, 360, 730),
      (50000.00, 149999.99, 91.00, 360, 730),
      (150000.00, 299999.99, 93.00, 360, 730),
      (300000.00, 499999.99, 95.00, 360, 730),
      (500000.00, 999999.99, 97.00, 360, 730),
      (1000000.00, 99999999.99, 98.00, 360, 730),
]
cursor.executemany(politica_lca_pos_360_sql, politica_lca_pos_360)

#### LCA Pós 730 ####
cursor.execute("DELETE FROM politica_lca_pos_730")
politica_lca_pos_730_sql = 'INSERT INTO politica_lca_pos_730 (valor_minimo, valor_maximo, taxa, dias_liquidez, dias_vencimento) VALUES (%s, %s, %s, %s, %s)'
politica_lca_pos_730 = [
      (5000.00, 49999.99, 91.00, 730, 730),
      (50000.00, 149999.99, 93.00, 730, 730),
      (150000.00, 299999.99, 95.00, 730, 730),
      (300000.00, 499999.99, 97.00, 730, 730),
      (500000.00, 999999.99, 98.00, 730, 730),
      (1000000.00, 99999999.99, 99.00, 730, 730),
]
cursor.executemany(politica_lca_pos_730_sql, politica_lca_pos_730)

"""
# testando o que foi inserido
cursor.execute('select * from db_plataforma_investimentos.politica_lca_pre_276')
print(' -------------  politica LCA Pre 276:  -------------')
for faixa in cursor.fetchall():
    print("ID: {}, Valor mínimo: {:.2f}, Valor máximo: {:.2f}, Taxa: {:.2f}, Dias de liquidez: {}, Dias de vencimento: {}".format(faixa[0], faixa[1], faixa[2], faixa[3], faixa[4], faixa[5]))
"""

conn.commit()

cursor.close()
conn.close()