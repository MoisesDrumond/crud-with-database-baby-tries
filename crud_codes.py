import sqlite3 as lite

con = lite.connect('dados.db')

lista = []

perguntaMAIN = int(input('[1] Create, [2] Read, [3] Update, [4] Delete: '))

pergunta1 = input('Qual e o seu nome?')
pergunta2 = input('Qual e o seu email?')
pergunta3 = int(input('Qual e o seu telefone?'))
pergunta4 = input('Qual e o dia da sua consulta?')
pergunta5 = input('Qual e o seu estado?')
pergunta6 = input('Qual e o seu assunto?')
# CREATE
if perguntaMAIN == 1:
    with con:
        cur = con.cursor()
        query = f"INSERT INTO formulario(nome, email, telefone, dia_em, estado, assunto) VALUES(?, ?, ?, ?, ?, ?)"
        lista.append(pergunta1)
        lista.append(pergunta2)
        lista.append(pergunta3)
        lista.append(pergunta4)
        lista.append(pergunta5)
        lista.append(pergunta6)
        cur.execute(query, lista)

# READ
with con:
    cur = con.cursor()
    query = "SELECT * FROM formulario"
    cur.execute(query)
    informacao = cur.fetchall()
    for dado in informacao:
        print(dado)

lista2 = []
# UPDATE
with con:
    pergunta = input('Digite o id do usuario a ser atualizado: ')
    pergunta2 = input('Digite o novo nome do usuario: ')
    cur = con.cursor()
    query = f"UPDATE formulario SET nome = '{pergunta2}' WHERE id = {pergunta}"
    lista2.append(pergunta)
    lista.append(pergunta2)
    # o jeito abaixo tambem funciona, so n sei se e vulnerável, mas parece até melhor e mais simples a primeira vista
    # query = "UPDATE formulario SET nome = 'Moshua' WHERE id = 1"
    cur.execute(query)

# DELETE
with con:
    ask = input('Digite o ID do usuário a ser deletado:')
    cur = con.cursor()
    query = f"DELETE FROM formulario WHERE id = {ask}"
    # query = "DELETE FROM formulario WHERE id = 1
    # mesma coisa do update
    cur.execute(query)
