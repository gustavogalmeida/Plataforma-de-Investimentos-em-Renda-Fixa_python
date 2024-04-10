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

cursor.execute("DROP DATABASE IF EXISTS `db_investimentos`;")

cursor.execute("CREATE DATABASE `db_investimentos`;")

cursor.execute("USE `db_investimentos`;")

# criando tabelas
TABLES = {}
TABLES['modalidades'] = ('''
      CREATE TABLE `modalidades` (
      `id` int NOT NULL AUTO_INCREMENT,
      `nome` varchar(30) NOT NULL,
      `tipo` varchar(30) NOT NULL,
      `resgate_automatico` varchar(40) NOT NULL,
      `prazo_minimo` int NOT NULL,
      `prazo_maximo` int NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo modalidades
modalidades_sql = 'INSERT INTO modalidades (nome, tipo, resgate_automatico, prazo_minimo, prazo_maximo) VALUES (%s, %s, %s, %s, %s)'
modalidades = [
      ("LCA DI", "LCA", "Não permitido", 276, 730),
      ("RDC Flexível", "RDC", "Permitido", 0, 5000)
]
cursor.executemany(modalidades_sql, modalidades)

cursor.execute('select * from db_investimentos.modalidades')
print(' -------------  Modalidades:  -------------')
for modalidade in cursor.fetchall():
    print(modalidade[1])


# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()