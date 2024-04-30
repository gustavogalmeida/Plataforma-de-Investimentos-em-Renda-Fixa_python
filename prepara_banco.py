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

cursor.execute("DROP DATABASE IF EXISTS `db_plataforma_investimentos`;")

cursor.execute("CREATE DATABASE `db_plataforma_investimentos`;")

cursor.execute("USE `db_plataforma_investimentos`;")

# criando dicionario que armazena as tabelas
TABLES = {}
TABLES['simulacao'] = ('''
        CREATE TABLE `simulacao`(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `descricao` varchar(30) not null,
            `valor_aplicado` float not null,
            `cdi` float not null,
            `cdi_sobras` float not null,
            `dias` int not null,
            `rentabilidade_bruta` float not null,
            `saldo_total` float not null,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tablea {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


conn.commit()

cursor.close()
conn.close()