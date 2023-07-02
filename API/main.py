from fastapi import FastAPI
import functions as f

app = FastAPI(debug=True)


@app.get("/")
async def root():
    f.criar_bd()
    f.inserir_cidade("São Paulo")
    f.inserir_cidade("Rio de Janeiro")
    f.inserir_cidade("Belo Horizonte")
    f.inserir_cidade("Cidade de Sol")
    f.inserir_predio("Prédio 2", "Residencial", "São Paulo")
    f.inserir_predio("Prédio 1", "ApartLuxo", "Rio de Janeiro")
    f.inserir_predio("Prédio 3", "Comercial", "São Paulo")
    f.inserir_pessoa("João", "Professor", "Prédio 2")
    f.inserir_pessoa("Maria", "Professora", "Prédio 2")
    f.inserir_pessoa("Diogo", "Ladrão", "Prédio 3")
    return {"message": "BD Created"}
"Função para criar o banco de dados e inserir dados iniciais"

@app.get("/cidades")
async def get_cidades(nome: str = None):
    return f.listar_cidades()
"Retorna todas as cidades cadastradas"

@app.get("/cidade/{nome}")
async def get_cidade(nome: str):
    return f.adquirir_cidade(nome)
"Ao passar o nome da cidade, retorna todos os prédios da cidade"

@app.get("/pessoas")
async def listar_pessoas():
    return f.listar_pessoas()
"Lista todas as pessoas cadastradas"

@app.get("/pessoa/{nome}")
async def get_pessoa(nome: str):
    return f.listar_pessoa(nome)
" Lista toda a informação de uma pessoa"
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
