# Rick and Morty API

Este projeto é uma **API simples** que consome a [Rick and Morty API](https://rickandmortyapi.com/) para obter informações de personagens e disponibilizá-las em formato **JSON**. Além disso, os dados também são exportados para um arquivo CSV chamado `50_personagens.csv`.

---

## **Funcionalidades**

- Buscar informações de **50 personagens** da série Rick and Morty.
- Retornar dados em **JSON** via endpoint `/personagens`.
- Salvar os dados em **CSV local**r.
- Exibir campos relevantes de cada personagem:
  - `id`
  - `name`
  - `status`
  - `species`
  - `type`
  - `gender`

---

## **Tecnologias**

- **Python 3**
- **Flask** - Framework web para criação de APIs.
- **Requests** - Para consumo de APIs externas.
- **Pandas** - Para manipulação e exportação de dados em CSV.

---
