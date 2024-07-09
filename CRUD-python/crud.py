import mysql.connector 


conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'sua senha',
    database = 'nome do seu BD',
)
cursor = conexao.cursor()



#CRUD
nome_produto = "plano internet basico"
valor = 210
comando = f'DELETE FROM vendas WHERE  nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o BD  



cursor.close()
conexao.close()


#CREATE 

#nome_produto = "plano internet intermediario"
#valor = 250
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)

#READ 

#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall() # ler o banco de dados 
#print(resultado)

#UPDATE 

#nome_produto = "plano internet basico"
#valor = 210
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() # edita o BD  

#DELETE 

#nome_produto = "plano internet basico"
#valor = 210
#comando = f'DELETE FROM vendas WHERE  nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() # edita o BD  