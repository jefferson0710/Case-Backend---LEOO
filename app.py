from flask import Flask, jsonify
import requests
import pandas as pd


app = Flask(__name__)
BASE_URL = "https://rickandmortyapi.com/api/character"

def pegar_personagens(limit=50):
    personagens = []
    for i in range(1, limit + 1):
        resposta = requests.get(f"{BASE_URL}/{i}")
        if resposta.status_code == 200:
            personagens.append(resposta.json())
    return personagens

@app.route('/personagens', methods=['GET'])
def listar_personagens():
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
       
        tabela = pd.DataFrame(dados)
        tabela.to_csv("50_personagens.csv", index=False, encoding="utf-8-sig")
    return jsonify(dados)
    



app.run(port=5000, host='localhost',debug=True)

