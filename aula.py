import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_python'
)
#CRUD

cursor = conexao.cursor()
nome_produto = "Budwiser"
valor = 12

#CREATE
"""
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() #<- edita o bd
"""
#READ
"""
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # <- lê o bd
print(resultado)
"""
#UPDATE
"""
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()
"""
#DELETE
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #<- edita o bd

cursor.close()
conexao.close()
