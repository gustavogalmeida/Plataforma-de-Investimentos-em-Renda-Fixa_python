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

# criando dicionario que armazena as tabelas
TABLES = {}
TABLES['simulacao'] = ('''
        CREATE TABLE `simulacao`(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `descricao` varchar(30) not null,
            `valor_aplicado` decimal (10, 2) not null,
            `cdi` decimal (10, 2) not null,
            `cdi_sobras` decimal (10, 2) not null,
            `dias` int not null,
            `rentabilidade_bruta` decimal (10, 2) not null,
            `saldo_total` decimal (10, 2) not null,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['politica_lca_pre_276'] = ('''
        CREATE TABLE `politica_lca_pre_276`(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `valor_minimo` decimal (10, 2) not null,
            `valor_maximo` decimal (10, 2) not null,
            `taxa` decimal (10, 2) not null,
            `dias_liquidez` int not null,
            `dias_vencimento` int not null,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['politica_lca_pre_360'] = ('''
        CREATE TABLE `politica_lca_pre_360`(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `valor_minimo` decimal (10, 2) not null,
            `valor_maximo` decimal (10, 2) not null,
            `taxa` decimal (10, 2) not null,
            `dias_liquidez` int not null,
            `dias_vencimento` int not null,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['politica_rdc_pre_181'] = ('''
        CREATE TABLE `politica_rdc_pre_181`(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `valor_minimo` decimal (10, 2) not null,
            `valor_maximo` decimal (10, 2) not null,
            `taxa` decimal (10, 2) not null,
            `dias_liquidez` int not null,
            `dias_vencimento` int not null,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['politica_rdc_pre_361'] = ('''
        CREATE TABLE `politica_rdc_pre_361`(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `valor_minimo` decimal (10, 2) not null,
            `valor_maximo` decimal (10, 2) not null,
            `taxa` decimal (10, 2) not null,
            `dias_liquidez` int not null,
            `dias_vencimento` int not null,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['politica_rdc_flexivel'] = ('''
        CREATE TABLE `politica_rdc_flexivel`(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `valor_minimo` decimal (10, 2) not null,
            `valor_maximo` decimal (10, 2) not null,
            `taxa` decimal (10, 2) not null,
            `dias_liquidez` int not null,
            `dias_vencimento` int not null,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['politica_lca_pos_276'] = ('''
        CREATE TABLE `politica_lca_pos_276`(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `valor_minimo` decimal (10, 2) not null,
            `valor_maximo` decimal (10, 2) not null,
            `taxa` decimal (10, 2) not null,
            `dias_liquidez` int not null,
            `dias_vencimento` int not null,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['politica_lca_pos_360'] = ('''
        CREATE TABLE `politica_lca_pos_360`(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `valor_minimo` decimal (10, 2) not null,
            `valor_maximo` decimal (10, 2) not null,
            `taxa` decimal (10, 2) not null,
            `dias_liquidez` int not null,
            `dias_vencimento` int not null,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['politica_lca_pos_730'] = ('''
        CREATE TABLE `politica_lca_pos_730`(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `valor_minimo` decimal (10, 2) not null,
            `valor_maximo` decimal (10, 2) not null,
            `taxa` decimal (10, 2) not null,
            `dias_liquidez` int not null,
            `dias_vencimento` int not null,
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