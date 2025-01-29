import psycopg2

def conectardb():

    con = psycopg2.connect(

        host='localhost',
        database = 'biblioteca',
        user = 'postgres',
        password = '12345'
    )
    return con

def login(login, senha):
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT * from usuarios where email='{login}' and senha='{senha}'  "
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida

def inserir_user(nome, contato, contatofamiliar, endereco, bairro, cep, sexo, email, senha):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO usuarios (nome, contato, contatofamiliar, endereco, bairro, cep, sexo, email, senha) VALUES ('{nome}','{contato}','{contatofamiliar}', '{endereco}', '{bairro}', '{cep}', '{sexo}', '{email}', '{senha}' )"
        cur.execute(sql)

    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False

    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito

def inserir_livros(titulo, autor, editora, login):
    conn = conectardb()
    cur = conn.cursor()

    try:
        sql = f"INSERT INTO livros (titulo, autor, editora, login) VALUES ('{titulo}', '{autor}', '{editora}', '{login}')"
        cur.execute(sql)

    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False

    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito

def listar_livros(login):
    con = conectardb()
    cur = con.cursor()
    sql = f"SELECT  titulo, autor, editora from livros WHERE login='{login}'"
    cur.execute(sql)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida
