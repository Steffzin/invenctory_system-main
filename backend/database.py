import sqlite3  # Importa o módulo sqlite3 para interagir com bancos de dados SQLite

class Database:  # Define a classe Database para gerenciar a interação com o banco de dados
    def __init__(self, db_name="inventory.db"):  # Inicializa a classe com o nome do banco de dados, padrão é "inventory.db"
        self.db_name = db_name  # Atribui o nome do banco de dados à variável de instância

    def connect(self):  # Método que conecta ao banco de dados SQLite e retorna a conexão
        return sqlite3.connect(self.db_name)  # Retorna uma conexão com o banco de dados especificado

    def get_items(self):  # Método para obter todos os itens da tabela "items"
        try:
            with self.connect() as conn:  # Estabelece a conexão com o banco de dados dentro de um contexto (automaticamente fecha ao sair)
                cursor = conn.cursor()  # Cria um objeto cursor para executar comandos SQL
                cursor.execute("SELECT * FROM items")  # Executa a consulta SQL para selecionar todos os itens da tabela "items"
                rows = cursor.fetchall()  # Obtém todas as linhas retornadas pela consulta

                # Nome das colunas do banco de dados para mapear os dados corretamente
                columns = ["id", "item_name", "description", "quantity", "price"]

                # Cria uma lista de dicionários, onde cada dicionário representa um item
                items = []
                for row in rows:
                    item = {columns[i]: row[i] for i in range(len(columns))}  # Mapeia cada linha para um dicionário usando os nomes das colunas
                    items.append(item)  # Adiciona o dicionário de item à lista de itens

                return items  # Retorna a lista de dicionários representando os itens

        except Exception as e:  # Captura qualquer exceção que ocorra durante o processo
            return str(e)  # Retorna a mensagem de erro como string

    def add_items(self, name, desc, amount, price):  # Método para adicionar um novo item à tabela "items"
        try:
            with self.connect() as conn:  # Estabelece a conexão com o banco de dados dentro de um contexto
                conn.cursor().execute("""
                INSERT INTO items (item_name, description, quantity, price)
                VALUES (?, ?, ?, ?)""", (name, desc, amount, price))  # Executa a consulta SQL para inserir um novo item na tabela
                conn.commit()  # Confirma a transação para garantir que os dados sejam salvos no banco
        except Exception as e:  # Captura qualquer exceção que ocorra durante o processo
            return str(e)  # Retorna a mensagem de erro como string

    def update_element(self, item_id, amount):  # Método para atualizar a quantidade de um item na tabela "items"
        try:
            with self.connect() as conn:  # Estabelece a conexão com o banco de dados dentro de um contexto
                conn.cursor().execute("""
                    UPDATE items SET quantity = ?  # Comando SQL para atualizar a quantidade de um item
                    WHERE id = ?""", (amount, item_id))  # O valor da quantidade e o id do item são passados como parâmetros
                conn.commit()  # Confirma a transação para garantir que a atualização seja salva no banco
        except Exception as e:  # Captura qualquer exceção que ocorra durante o processo
            return str(e)  # Retorna a mensagem de erro como string

    def delete_element(self, item_id):  # Método para excluir um item da tabela "items"
        try:
            with self.connect() as conn:  # Estabelece a conexão com o banco de dados dentro de um contexto
                conn.cursor().execute("DELETE FROM items WHERE id = ?", (item_id,))  # Executa a consulta SQL para excluir um item com o id fornecido
                conn.commit()  # Confirma a transação para garantir que a exclusão seja realizada no banco
        except Exception as e:  # Captura qualquer exceção que ocorra durante o processo
            return str(e)  # Retorna a mensagem de erro como string
