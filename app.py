from flask import Flask, jsonify
import requests
import pandas as pd


app = Flask(__name__)
# URL base da API de personagens da série Rick and Morty
BASE_URL = "https://rickandmortyapi.com/api/character"

def pegar_personagens(limit=50):
    """
    Buscar os primeiros 'limit' personagens da API.
    Faz uma requisição por personagem.
    Caso ele não ache nenhum personagem, vai retornar no terminal.
    """
    personagens = []
    for i in range(1, limit + 1):
        resposta = requests.get(f"{BASE_URL}/{i}")
        if resposta.status_code == 200:
            personagens.append(resposta.json())
    return personagens

@app.route('/personagens', methods=['GET'])
def listar_personagens():
    """
    Endpoint que retorna uma lista de personagens em JSON
    e salva os dados em um arquivo CSV local.
    """
    personagens = pegar_personagens(limit=50)
    dados = []
    for p in personagens:
        dados.append({
            "id": p["id"],
            "name": p["name"],
            "status": p["status"],
            "species": p["species"],
            "type": p["type"],
            "gender": p["gender"]
        }) 
        """
        Converte a lista criada acima em um DataFrame do Pandas.
        Salva os dados em CSV compartível com Excel.
        """
        tabela = pd.DataFrame(dados)
        tabela.to_csv("50_personagens.csv", index=False, encoding="utf-8-sig")
    # Retorna os dados em formato JSON para quem acessar o endpoint    
    return jsonify(dados)
    


# Inicia a aplicação em Flask para rodar remotamente configurando a porta de acesso.
app.run(port=5000, host='localhost',debug=True)

