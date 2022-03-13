import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_python'
)
#CRUD

cursor = conexao.cursor()
nome_produto = "Redbull"
valor = 16

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

cursor.close()
conexao.close()