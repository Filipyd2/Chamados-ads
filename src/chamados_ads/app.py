from flask import Flask, jsonify, request

app = Flask(__name__)

chamados: list[dict] = [
    {
        "id": 1,
        "titulo": "Erro de acesso ao sistema acadêmico",
        "descricao": "Usuário não consegue autenticar no portal.",
        "prioridade": "Alta",
        "status": "Aberto",
    }
]
proximo_id = 2


@app.get("/")
def inicio():
    return {
        "mensagem": "API funcionando"
    }


@app.get("/chamados")
def listar_chamados():
    return jsonify(chamados), 200


@app.get("/chamados/<int:chamado_id>")
def obter_chamado(chamado_id: int):
    chamado = next((c for c in chamados if c["id"] == chamado_id), None)
    if not chamado:
        return jsonify({"erro": "Chamado não encontrado"}), 404
    return jsonify(chamado), 200


@app.post("/chamados")
def criar_chamado():
    global proximo_id
    dados = request.get_json(silent=True) or {}

    titulo = str(dados.get("titulo", "")).strip()
    descricao = str(dados.get("descricao", "")).strip()
    prioridade = str(dados.get("prioridade", "Média")).strip()

    if not titulo or not descricao:
        return jsonify({"erro": "Os campos 'titulo' e 'descricao' são obrigatórios"}), 400

    novo_chamado = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "Aberto",
    }
    chamados.append(novo_chamado)
    proximo_id += 1

    return jsonify(novo_chamado), 201


@app.patch("/chamados/<int:chamado_id>")
def atualizar_chamado(chamado_id: int):
    chamado = next((c for c in chamados if c["id"] == chamado_id), None)
    if not chamado:
        return jsonify({"erro": "Chamado não encontrado"}), 404

    dados = request.get_json(silent=True) or {}
    if "titulo" in dados:
        chamado["titulo"] = str(dados["titulo"]).strip()
    if "descricao" in dados:
        chamado["descricao"] = str(dados["descricao"]).strip()
    if "prioridade" in dados:
        chamado["prioridade"] = str(dados["prioridade"]).strip()
    if "status" in dados:
        chamado["status"] = str(dados["status"]).strip()

    return jsonify(chamado), 200


@app.delete("/chamados/<int:chamado_id>")
def excluir_chamado(chamado_id: int):
    global chamados
    chamado = next((c for c in chamados if c["id"] == chamado_id), None)
    if not chamado:
        return jsonify({"erro": "Chamado não encontrado"}), 404

    chamados = [c for c in chamados if c["id"] != chamado_id]
    return "", 204
