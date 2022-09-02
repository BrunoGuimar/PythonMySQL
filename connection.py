import mysql.connector
def criar_conexao(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

def fechar_conexao(con):
    return con.close()

def insere_usuario(con, nome, email):
    cursor = con.cursor()
    sql = 'INSERT INTO alunos (nome, email) values (%s, %s)'
    valores = (nome, email)
    cursor.execute(sql, valores)
    con.commit()

def select_usuarios(con):
    cursor = con.cursor()
    sql = "SELECT id, nome, email FROM alunos"
    cursor.execute(sql)

    for (id, nome, email) in cursor: 
        print(id, nome, email)

    cursor.close()

#UPDATE empregados set nome='João da Silva',cidade='São Paulo' where codigo_empregado=2

def update_usuarios(con, nome, email, id):
    cursor = con.cursor()
    sql = "UPDATE alunos set nome='%s',email='%s' where id='%s'"
    valores = (nome, email, id)
    cursor.execute(sql, valores)
    con.commit()

def del_usuarios(con):
    cursor = con.cursor()
    sql = "DELETE FROM alunos WHERE id = 1"
    cursor.execute(sql)
    con.commit()