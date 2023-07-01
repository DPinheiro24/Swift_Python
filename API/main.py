from fastapi import FastAPI
import functions as f

app = FastAPI(debug=True)


@app.get("/")
async def root():
    f.criar_bd()
    f.inserir_cidade("São Paulo")
    f.inserir_cidade("Rio de Janeiro")
    f.inserir_cidade("Belo Horizonte")
    f.inserir_predio("Prédio 2", "Residencial", "São Paulo")

    f.inserir_predio("Prédio 3", "Comercial", "São Paulo")
    f.inserir_pessoa("João", "Professor", "Prédio 2")
    f.inserir_pessoa("Maria", "Professora", "Prédio 2")
    f.inserir_pessoa("Diogo", "Ladrão", "Prédio 3")
    return {"message": "BD Created"}

@app.get("/cidades")
async def get_cidades(nome: str = None):
    return f.listar_cidades()

@app.get("/cidade/{nome}")
async def get_cidade(nome: str):
    #nome_cidade = nome.replace(" ", "")
    """cidade = f.listar_cidade(nome)
    if cidade and 'cidade_id' in cidade:
        predios = f.listar_predios(cidade['cidade_id'])
        cidade['predios'] = predios
        return cidade
    else:
        return {"error": "Cidade não encontrada"}
    """
    return f.adquirir_cidade(nome)

@app.get("/pessoas")
async def listar_pessoas():
    return f.listar_pessoas()

@app.get("/pessoa/{nome}")
async def get_pessoa(nome: str):
    return f.listar_pessoa(nome)

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
