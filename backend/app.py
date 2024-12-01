from flask import Flask, jsonify, request  # Importa as classes e funções necessárias do Flask
from .database import Database  # Importa a classe Database de um módulo local chamado 'database'

app = Flask(__name__)  # Cria uma instância da aplicação Flask
db = Database()  # Cria uma instância da classe Database para interagir com o banco de dados

@app.after_request  # Define uma função para ser executada após cada resposta, adicionando cabeçalhos CORS
def add_cors_headers(response):
    """Adicionar cabeçalhos CORS manualmente"""
    response.headers['Access-Control-Allow-Origin'] = '*'  # Permite qualquer origem acessar o recurso
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'  # Define os métodos HTTP permitidos
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'  # Define os cabeçalhos permitidos
    return response  # Retorna a resposta com os cabeçalhos modificados

@app.route("/items", methods=["GET"])  # Define uma rota para a URL '/items' com o método GET
def get_items():
    """Recupera todos os dados do banco"""
    try:
        items = db.get_items()  # Chama o método get_items da classe Database para obter todos os itens
        if items:
            return jsonify(items), 200  # Se itens foram encontrados, retorna os itens com o código de status 200
        else:
            return jsonify({"message": "Não há itens"}), 404  # Se não houver itens, retorna uma mensagem com status 404
        
    except Exception as e:
        return jsonify({"error": f"Erro ao recuperar itens: {str(e)}"}), 500  # Retorna um erro genérico em caso de exceção

@app.route("/items", methods=["POST"])  # Define uma rota para a URL '/items' com o método POST
def add_items():
    """Adiciona itens novos ao inventário"""
    try:
        req = request.json  # Obtém os dados enviados na requisição no formato JSON

        # Valida os dados obrigatórios
        if not all(key in req for key in ["item_name", "description", "quantity", "price"]):
            return jsonify({"error": "Dados incoerentes"}), 400  # Retorna erro 400 se algum dado necessário não foi fornecido
        
        # Adiciona item ao banco
        db.add_items(req["item_name"], req["description"], req["quantity"], req["price"])
        return jsonify({"message": "Item adicionado com sucesso!"}), 201  # Retorna sucesso com código 201 (item criado)
    
    except Exception as e:
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500  # Retorna erro 500 em caso de exceção

@app.route("/items/<int:item_id>", methods=["PUT"])  # Define uma rota para a URL '/items/<item_id>' com o método PUT
def update(item_id):
    """Atualiza a quantidade de um item"""
    try:
        req = request.json  # Obtém os dados enviados na requisição no formato JSON

        # Valida a quantidade
        if "quantity" not in req:
            return jsonify({"error": "Falta o campo da quantidade"}), 400  # Retorna erro 400 se a quantidade não foi informada
        
        # Atualiza o item
        db.update_element(item_id, req["quantity"])
        return jsonify({"message": "Atualização realizada!"}), 200  # Retorna sucesso com código 200
    
    except KeyError as ke:
        return jsonify({"error": f"Sem chave: {str(ke)}"}), 400  # Retorna erro 400 caso falte alguma chave esperada na requisição
    
    except Exception as e:
        return jsonify({"error": f"Erro ao atualizar item: {str(e)}"}), 500  # Retorna erro 500 em caso de exceção

@app.route("/items/<int:item_id>", methods=["DELETE"])  # Define uma rota para a URL '/items/<item_id>' com o método DELETE
def delete(item_id):
    """Remove um item do inventário"""
    try:
        db.delete_element(item_id)  # Chama o método para deletar um item com o id fornecido
        return jsonify({"message": "Item removido com sucesso!"}), 200  # Retorna sucesso com código 200

    except Exception as e:
        return jsonify({"error": f"Erro na remoção: {str(e)}"}), 500  # Retorna erro 500 em caso de exceção

    if __name__ == "__main___":
        initialize_database()
        