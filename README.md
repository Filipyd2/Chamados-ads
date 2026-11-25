# chamados-ads

API REST desenvolvida em Python com Flask para gerenciamento de chamados de suporte técnico, utilizando `uv` para gerenciamento de dependências e build.

## Identificação

* **Aluno:** Luiz Filipy Soares da Silva
* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
* **Professor4:** [JayrAlencar]
* **Licença:** MIT

## Pré-requisitos

* Python 3.14 ou superior
* [uv](https://docs.astral.sh/uv/) instalado

## Instalação e Execução

1. **Clone o repositório e entre no diretório:**
   ```bash
   git clone https://github.com/<seu-usuario>/chamados-ads.git
   cd chamados-ads
   ```

2. **Instale as dependências e crie o ambiente virtual com `uv`:**
   ```bash
   uv sync
   ```

3. **Execute a aplicação:**

   * **Via script do projeto (`pyproject.toml`):**
     ```bash
     uv run chamados-ads
     ```
   * **Ou diretamente via CLI do Flask:**
     ```bash
     uv run flask --app chamados_ads.app run --debug
     ```

4. **Verifique o funcionamento:**
   Acesse `http://127.0.0.1:5000/` no navegador ou via `curl`:
   ```bash
   curl http://127.0.0.1:5000/
   ```
   Resposta esperada:
   ```json
   {
     "mensagem": "API funcionando"
   }
   ```

## Endpoints Disponíveis

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/` | Verifica o status da API |
| `GET` | `/chamados` | Lista todos os chamados |
| `GET` | `/chamados/<id>` | Busca um chamado pelo ID |
| `POST` | `/chamados` | Cria um novo chamado (`titulo`, `descricao`, `prioridade`) |
| `PATCH` | `/chamados/<id>` | Atualiza campos ou `status` de um chamado |
| `DELETE` | `/chamados/<id>` | Remove um chamado |

## Exemplo de Uso (`POST /chamados`)

```bash
curl -X POST http://127.0.0.1:5000/chamados \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Projetor sem imagem", "descricao": "Sala 04 sem sinal HDMI", "prioridade": "Alta"}'
```
