const apiUrl = "http://127.0.0.1:5000/items"; // Define a URL da API do backend para interagir com os itens do inventário
let currentItemId = null; // Variável para armazenar o ID do item que está sendo editado, usada para identificar qual item será atualizado

// Função para listar os itens do inventário
async function fetchItems() {
    try {
        const response = await fetch(apiUrl); // Faz uma requisição GET para a URL da API e aguarda a resposta
        const items = await response.json(); // Converte a resposta para JSON (um array de itens)
        renderItems(items); // Chama a função renderItems para exibir os itens na página
    } catch (error) {
        console.error("Erro ao buscar itens:", error); // Exibe um erro caso a requisição falhe
    }
}

// Função para renderizar os itens na página
function renderItems(items) {
    const itemList = document.getElementById("inventory"); // Obtém o elemento com id "inventory" onde os itens serão listados
    itemList.innerHTML = ""; // Limpa a lista de itens antes de renderizar novos
    items.forEach(item => { // Itera sobre cada item recebido
        const listItem = document.createElement("div"); // Cria um novo elemento div para cada item
        listItem.classList.add("item"); // Adiciona a classe "item" para estilização do item
        listItem.innerHTML = `
            <span>${item.item_name} - ${item.description} (Qtd: ${item.quantity}, Preço: ${item.price} moedas)</span>
            <button class="update-btn" onclick="openUpdatePopup(${item.id}, ${item.quantity})">Atualizar</button>
            <button class="delete-btn" onclick="deleteItem(${item.id})">Excluir</button>
        `; // Cria o conteúdo HTML para exibir as informações do item, incluindo botões para atualizar e excluir
        itemList.appendChild(listItem); // Adiciona o novo item à lista no DOM
    });
}

// Função para adicionar um novo item
async function addItem(event) {
    event.preventDefault(); // Evita o recarregamento da página ao submeter o formulário

    const nome = document.getElementById("item-nome").value; // Obtém o nome do item inserido
    const descricao = document.getElementById("item-descricao").value; // Obtém a descrição do item inserido
    const quantidade = document.getElementById("item-quantidade").value; // Obtém a quantidade do item inserido
    const preco = document.getElementById("item-preco").value; // Obtém o preço do item inserido

    const newItem = { // Cria um objeto com os dados do novo item
        item_name: nome,
        description: descricao,
        quantity: parseInt(quantidade),
        price: parseFloat(preco)
    };

    try {
        const response = await fetch(apiUrl, { // Faz uma requisição POST para adicionar o item
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(newItem) // Envia os dados do novo item no corpo da requisição
        });

        if (response.ok) { // Verifica se a resposta foi bem-sucedida
            fetchItems(); // Atualiza a lista de itens
            closeAddPopup(); // Fecha o popup de adicionar item
            
            // Limpa os campos do formulário
            document.getElementById("item-nome").value = "";
            document.getElementById("item-descricao").value = "";
            document.getElementById("item-quantidade").value = "";
            document.getElementById("item-preco").value = "";
        } else {
            console.error("Erro ao adicionar item:", response.statusText); // Exibe um erro se a resposta não for bem-sucedida
        }
    } catch (error) {
        console.error("Erro ao adicionar item:", error); // Exibe um erro se a requisição falhar
    }
}


// Conectar a função de adicionar item ao formulário
document.getElementById("add-item-form").onsubmit = addItem; // Define a função addItem como o manipulador de evento para o envio do formulário de adicionar item

// Função para excluir um item
async function deleteItem(itemId) {
    try {
        const response = await fetch(`${apiUrl}/${itemId}`, { method: "DELETE" }); // Faz uma requisição DELETE para excluir o item com o id fornecido

        if (response.ok) { // Verifica se a resposta foi bem-sucedida
            fetchItems(); // Atualiza a lista de itens
        } else {
            console.error("Erro ao excluir item:", response.statusText); // Exibe um erro se a resposta não for bem-sucedida
        }
    } catch (error) {
        console.error("Erro ao excluir item:", error); // Exibe um erro se a requisição falhar
    }
}

// Função para abrir o popup de adicionar
document.getElementById("add-item-button").onclick = function() { 
    document.getElementById("add-popup").style.display = "flex"; // Exibe o popup de adicionar item
};

// Função para fechar o popup de adicionar
document.getElementById("cancel-add").onclick = function() {
    closeAddPopup(); // Chama a função para fechar o popup de adicionar item
};

// Função para fechar o popup de adicionar
function closeAddPopup() {
    document.getElementById("add-popup").style.display = "none"; // Esconde o popup de adicionar item
}

// Função para abrir o popup de atualizar
function openUpdatePopup(itemId, currentQuantity) {
    currentItemId = itemId; // Armazena o ID do item que será atualizado
    document.getElementById("update-popup").style.display = "flex"; // Exibe o popup de atualizar item
    document.getElementById("update-quantidade").value = currentQuantity; // Define o valor do campo de quantidade para a quantidade atual do item
}

// Função para fechar o popup de atualizar
document.getElementById("cancel-update").onclick = function() {
    closeUpdatePopup(); // Chama a função para fechar o popup de atualizar item
};

// Função para fechar o popup de atualizar
function closeUpdatePopup() {
    document.getElementById("update-popup").style.display = "none"; // Esconde o popup de atualizar item
}

// Função para atualizar a quantidade
async function updateItem(event) {
    event.preventDefault(); // Evita o recarregamento da página ao submeter o formulário

    const newQuantity = document.getElementById("update-quantidade").value; // Obtém o novo valor da quantidade inserida

    try {
        const response = await fetch(`${apiUrl}/${currentItemId}`, { // Faz uma requisição PUT para atualizar o item com o id armazenado
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ quantity: parseInt(newQuantity) }) // Envia a nova quantidade no corpo da requisição
        });

        if (response.ok) { // Verifica se a resposta foi bem-sucedida
            fetchItems(); // Atualiza a lista de itens
            closeUpdatePopup(); // Fecha o popup de atualizar item
        } else {
            console.error("Erro ao atualizar item:", response.statusText); // Exibe um erro se a resposta não for bem-sucedida
        }
    } catch (error) {
        console.error("Erro ao atualizar item:", error); // Exibe um erro se a requisição falhar
    }
}

// Função para lidar com o envio do formulário de atualização
document.getElementById("update-item-form").onsubmit = updateItem; // Define a função updateItem como o manipulador de evento para o envio do formulário de atualização de item

// Inicializa a lista de itens
fetchItems(); // Chama a função fetchItems para carregar os itens quando a página é carregada
