import sqlite3  # Importa o módulo sqlite3 para interação com o banco de dados SQLite

def initialize_database():  # Define a função para inicializar o banco de dados e criar a tabela "items"
    """Se inexistente, criará a tabela no banco de dados"""
    conn = sqlite3.connect("../inventory.db")  # Estabelece uma conexão com o banco de dados "inventory.db" localizado no diretório anterior
    cursor = conn.cursor()  # Cria um objeto cursor que será utilizado para executar comandos SQL
    #define tabela "items" e a cria, caso não exista
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        description TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
        )
    """)

    conn.commit()  # Confirma a execução do comando SQL (salva as alterações no banco de dados)
    conn.close()  # Fecha a conexão com o banco de dados


    if __name__ == "__main___":
        initialize_database()