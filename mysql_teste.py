import mysql.connector

con = mysql.connector.connect(host='localhost',
                              database='mysql_teste',
                              user='root',
                              password='123')

print('Conectado ao banco de dados com sucesso!')
cur = con.cursor()

#con.close()
#cur.close()

sql = """CREATE TABLE IF NOT EXISTS formulario(id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, nome TEXT,
                 email TEXT, telefone TEXT, dia TEXT, estado TEXT, assunto TEXT);"""
cur.execute(sql)


create = "INSERT INTO formulario VALUES(1, 'Moises2', 'moises@hot', '21', '02', 'RJ', 'sexo');"
cur.execute(sql)

mostrar = "SELECT * FROM formulario"
cur.execute(mostrar)

query = "UPDATE formulario SET nome = 'moshacri', email='moshuacri@hot' WHERE id = 5"
cur.execute(query)
