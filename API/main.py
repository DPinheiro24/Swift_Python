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
    f.inserir_predio("Prédio1", "ApartLuxo", "Rio de Janeiro")
    f.inserir_predio("Prédio 3", "Comercial", "São Paulo")
    f.inserir_pessoa("João", "Professor", "Prédio1")
    f.inserir_pessoa("Maria", "Professora", "Prédio 2")
    f.inserir_pessoa("Diogo", "Ladrão", "Prédio 2")
    return {"message": "BD Created"}
#Função para criar o banco de dados e inserir dados iniciais

@app.get("/cidades")
async def get_cidades(nome: str = None):
    return f.listar_cidades()
#Retorna todas as cidades cadastradas

@app.get("/cidade/{nome}")
async def get_cidade(nome: str):
    return f.adquirir_cidade(nome)
#Ao passar o nome da cidade, retorna todos os prédios da cidade
@app.get("/predios")
async def get_predios():
    return f.listar_predios()
#Retorna todos os prédios cadastrados

@app.get("/predio/{nome}")
async def get_predio(nome: str):
    return f.listar_pessoas_predio(nome)
#Ao passar o nome do prédio, retorna todas as pessoas que moram no prédio
@app.get("/pessoas")
async def listar_pessoas():
    return f.listar_pessoas()
#Lista todas as pessoas cadastradas

@app.get("/pessoa/{nome}")
async def get_pessoa(nome: str):
    return f.listar_pessoa(nome)
#Lista toda a informação de uma pessoa"

@app.get("/criar_cidade/{nome}")
async def criar_cidade(nome: str):
    return f.inserir_cidade(nome)
#Cria uma cidade

@app.get("/criar_predio/{nome}/{tipo}/{cidade}")
async def criar_predio(nome: str, tipo: str, cidade: str):
    return f.inserir_predio(nome, tipo, cidade)
#Cria um prédio

@app.get("/criar_pessoa/{nome}/{emprego}/{predio}")
async def criar_pessoa(nome: str, emprego: str, predio: str):
    return f.inserir_pessoa(nome, emprego, predio)
#Cria uma pessoa

@app.get("/deletar_cidade/{nome}")
async def deletar_cidade(nome: str):
    return f.deletar_cidade(nome)
#Deleta uma cidade

@app.get("/deletar_predio/{nome}")
async def deletar_predio(nome: str):
    return f.deletar_predio(nome)
#Deleta um prédio

@app.get("/deletar_pessoa/{nome}")
async def deletar_pessoa(nome: str):
    return f.deletar_pessoa(nome)
#Deleta uma pessoa

@app.get("/atualizar_cidade/{nome}/{novo_nome}")
async def atualizar_cidade(nome: str, novo_nome: str):
    return f.atualizar_cidade(nome, novo_nome)
#Atualiza o nome de uma cidade

@app.get("/atualizar_predio/{nome}/{novo_nome}/{novo_tipo}/{nova_cidade}")
async def atualizar_predio(nome: str, novo_nome: str, novo_tipo: str, nova_cidade: str):
    return f.atualizar_predio(nome, novo_nome, novo_tipo, nova_cidade)
#Atualiza o nome, tipo e cidade de um prédio

@app.get("/atualizar_pessoa/{nome}/{novo_nome}/{novo_emprego}/{novo_predio}")
async def atualizar_pessoa(nome: str, novo_nome: str, novo_emprego: str, novo_predio: str
                           ):
    return f.atualizar_pessoa(nome, novo_nome, novo_emprego, novo_predio)
#Atualiza o nome, emprego e prédio de uma pessoa

@app.get("/code/{code}")
async def atualizar_code(code: int):
    return f.atualizar_code(code)

