import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXIST produtos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               codigo INTEGER NO NULL
               quantidade INTEGER NO NULL )""")

conexao.commit

def salvar_produto(nome, codigo, quantidade):
    cursor.execute("INSERT INTO estoque(nome, codigo, quantidade) values(?, ?)", (nome, codigo, quantidade))
    conexao.commit

def deletar_produto(nome, codigo, quantidade):
    cursor.execute(" ")