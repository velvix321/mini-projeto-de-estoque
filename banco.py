import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS estoque(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               codigo INTEGER NOT NULL,
               quantidade INTEGER NOT NULL
               )
               """)
conexao.commit()



class Estoque:
    def __init__(self, nome, codigo, quantidade, id=None):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        self.id = id

    def salvar_produtos(self):
        cursor.execute("INSERT INTO estoque(nome, codigo, quantidade) values(?, ?, ?)",
                        (self.nome, self.codigo, self.quantidade))
        conexao.commit()

    def mostra_produtos(self):
        cursor.execute("SELECT * FROM estoque")
        for linha in cursor.fetchall():
            print(linha)

    def atualizar_produtos(self):
        if self.id is None:
            print("precisa ser um id valido")
            return
        else:
            cursor.execute("""UPDATE estoque
                           set nome = ?, codigo = ?,
                           quantidade = ? where id = ?""",
                           (self.nome, self.codigo, self.quantidade, self.id))
            conexao.commit()
         
    def deletar_produto(self):
        if self.id is None:
            print("precisa ser um id valido")
            return
        else:
            cursor.execute("DELETE FROM estoque WHERE id = ?", (self.id,))
            print(f"produto com o id {self.id} deletado com sucesso")
            conexao.commit()


class Comandos:
    def cadastro(self):
        nome = input("Nome do produto: ")
        codigo = int(input("Código: "))
        quantidade = int(input("Quantidade: "))

        produto = Estoque(nome, codigo, quantidade)
        produto.salvar_produtos()
        print("produto cadastrado com sucesso")

    def atualizar(self):
        id_produto = int(input("ID do produto: "))
        nome = input("Novo nome: ")
        codigo = int(input("Novo código: "))
        quantidade = int(input("Nova quantidade: "))

        produto = Estoque(nome, codigo, quantidade, id_produto)
        produto.atualizar_produtos()
        print("produto atualizado com sucesso")

    def deletar(self):
        id_produto = int(input("ID do produto para deletar: "))
        produto = Estoque(None, None, None, id_produto)
        produto.deletar_produto()
        print("produto deletado com sucesso")

    def mostrar(self):
        produto = Estoque(None, None, None)
        produto.mostra_produtos()

comandos = comandos
valor = int(input("1 cadastrar"))
valor = int(input("2 mostrar"))
valor = int(input("3 atualizar"))
valor = int(input("4 deletar"))
valor = int(input("5 sair"))

if valor == 1:
comandos = Comandos()
comandos.cadastro()
comandos.mostrar()
comandos.atualizar()
comandos.deletar()
comandos.mostrar()

conexao.close()