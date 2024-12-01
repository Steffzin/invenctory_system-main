from backend.models import initialize_database
# Importa a função 'initialize_database' do módulo 'models' dentro do diretório 'backend'. Esta função é responsável por inicializar o banco de dados.

from backend.app import app
# Importa o objeto 'app' do módulo 'app' dentro do diretório 'backend'. Este objeto é geralmente uma instância do Flask (ou outra framework web) que será usada para rodar o servidor web.

def main():
    # Define a função principal 'main', que será executada quando o script for rodado diretamente.

    print("Iniciando o sistema...")
    # Exibe a mensagem "Iniciando o sistema..." no console para informar que o sistema está sendo iniciado.

    # Inicializa o banco de dados
    print("Inicializando o banco de dados...")
    # Exibe a mensagem "Inicializando o banco de dados..." no console, indicando que a função para configurar o banco de dados será chamada.

    initialize_database()
    # Chama a função 'initialize_database' para configurar e inicializar o banco de dados, preparando-o para uso.

    # Inicia o backend
    print("Iniciando o backend...")
    # Exibe a mensagem "Iniciando o backend..." no console para indicar que o servidor web será iniciado a seguir.

    app.run(debug=True, port=5000)
    # Inicia o servidor backend, fazendo com que o Flask (ou outro framework web) comece a rodar o aplicativo.
    # O parâmetro 'debug=True' ativa o modo de depuração, permitindo ver mensagens de erro detalhadas e atualizações automáticas quando o código for alterado.
    # O parâmetro 'port=5000' define que o servidor irá rodar na porta 5000.

if __name__ == "__main__":
    main()
    # Verifica se o script está sendo executado diretamente (não importado como módulo em outro script).
    # Se for o caso, chama a função 'main' para iniciar o sistema.
