import json

def abrir_json() -> dict:
    try:
        with open('produtos.json', 'r') as arquivo_json:
            produtos_json = json.load(arquivo_json)
            if produtos_json == {}:
                return {'produtos': [], 'pedidos': []}
            return produtos_json
    except (FileNotFoundError, json.JSONDecodeError):  # Ajuste aqui
        return {'produtos': [], 'pedidos': []}


def salvar_produtos(produtos: dict):
    with open('produtos.json', 'w') as arquivo_json:
        json.dump(produtos, arquivo_json, indent=4)