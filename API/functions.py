import sqlite3
import control_unit as admin

bd = "mundo.db"
conn = sqlite3.connect(bd)
cursor = conn.cursor()

def criar_bd(): # Função para criar o banco de dados e inserir dados iniciais

    sql = """
    CREATE TABLE cidade (
        cidade_id integer primary key autoincrement not null,
        cidade_nome text not null
        );
    """

    try:
        conn.executescript(sql)
        conn.commit()
    except:
        print("Tabela Cidade já existe")

    sql = """
    CREATE TABLE predio (
        predio_id integer primary key autoincrement not null ,
        predio_nome text not null,
        predio_tipo text,
        cidade_id integer not null,
        foreign key (cidade_id) references cidade(cidade_id)
        );
    """

    try:
        conn.executescript(sql)
        conn.commit()
    except:
        print("Tabela Predio já existe")

    sql = """
    CREATE TABLE pessoa (
        pessoa_id integer primary key autoincrement not null,
        pessoa_nome text not null,
        emprego text,
        predio_id integer not null,
        foreign key (predio_id) references predio(predio_nome)
        );
    """

    try:
        conn.executescript(sql)
        conn.commit()
    except:
        print("Tabela Pessoa já existe")

    pass

def inserir_cidade(nome): # Função para inserir uma cidade

    sql = """
    select cidade_id from cidade where cidade_nome = (?);
    """

    cursor.execute(sql, (nome,))
    aux = cursor.fetchone()

    if aux is not None:
        print("Cidade já existe")
        return "Cidade já existe"
    else:
        print("A criar cidade com nome: " + nome)

    sql = """
    insert into cidade (cidade_nome) values (?);
    """

    conn.execute(sql, (nome,))

    conn.commit()

    pass

def inserir_predio(nome, tipo, cidade): # Função para inserir um prédio
    
    sql = """
    select predio_id from predio where predio_nome = (?);
    """

    cursor.execute(sql, (nome,))
    aux = cursor.fetchone()

    if aux is not None:
        print("Predio já existe")
        return "Predio já existe"
    else:
        print("A criar predio com nome: " + nome)

    sql = """
    insert into predio (predio_nome, predio_tipo, cidade_id) values (?, ?, ?);
    """

    try:
        conn.execute(sql, (nome, tipo, cidade))
        conn.commit()
    except:
        print("Algo deu errado, tentou-se criar um predio com estes valores: " + nome + ", " + tipo + ", " + cidade)
        return "Aconteceu um erro, verifique os valores inseridos"

    pass

def inserir_pessoa(nome, emprego, predio): # Função para inserir uma pessoa

    sql = """
    select pessoa_id from pessoa where pessoa_nome = (?) and emprego = (?) and predio_id = (?);
    """

    cursor.execute(sql, (nome, emprego, predio))
    aux = cursor.fetchone()

    if aux is not None:
        print("Pessoa já existe")
        return "Pessoa já existe"
    else:
        print("A criar pessoa com nome: " + nome)

    sql = """
    insert into pessoa (pessoa_nome, emprego, predio_id) values (?, ?, ?);
    """

    try:
        conn.execute(sql, (nome, emprego, predio))
        conn.commit()
    except:
        print("Algo deu errado, tentou-se criar uma pessoa com estes valores: " + nome + ", " + emprego + ", " + predio)
        return "Aconteceu um erro, verifique os valores inseridos"

    pass

def listar_cidades(): # Função para listar as cidades

    sql = """
    select cidade_id, cidade_nome from cidade;
    """
    
    cursor.execute(sql)
    aux = cursor.fetchall()

    for i in aux:
        print(i);

    return aux

    pass

def listar_pessoas(): # Função para listar as pessoas

    sql = """
    SELECT pessoa_id, pessoa_nome, emprego, predio_id FROM pessoa ;
    """
    cursor.execute(sql)
    aux = cursor.fetchall()

    pessoas = []
    for pessoa in aux:
        pessoa_dict = {
            'pessoa_id': pessoa[0],
            'pessoa_nome': pessoa[1],
            'emprego': pessoa[2],
            'predio_id': pessoa[3]
        }
        pessoas.append(pessoa_dict)

    return pessoas

    pass

def listar_pessoa(nome: str): # Função para listar dados da pessoa
    sql = """
    SELECT pessoa_id, pessoa_nome, emprego, predio_id FROM pessoa WHERE pessoa_nome = ?;
    """
    cursor.execute(sql, (nome,))
    pessoa = cursor.fetchone()

    if pessoa:
        pessoa_dict = {
            'pessoa_id': pessoa[0],
            'pessoa_nome': pessoa[1],
            'emprego': pessoa[2],
            'predio_id': pessoa[3]
        }
        return pessoa_dict
    else:
        return {"error": "Pessoa não encontrada"}


def listar_pessoas_predio(nome: str): # Função para listar pessoas de um prédio
    sql = """
    SELECT pessoa_id, pessoa_nome, emprego FROM pessoa WHERE pessoa_nome = ?;
    """
    cursor.execute(sql, (nome,))
    pessoas = cursor.fetchall()

    pessoas_list = []
    for pessoa in pessoas:
        pessoa_dict = {
            'pessoa_id': pessoa[0],
            'pessoa_nome': pessoa[1],
            'emprego': pessoa[2]
        }
        pessoas_list.append(pessoa_dict)

    return pessoas_list

def adquirir_cidade(nome: str): # Função para mostrar todos os predios da cidade

    sql = """
    SELECT cidade_nome from cidade where cidade_nome = (?); 
    """

    cursor.execute(sql, (nome,))

    aux = cursor.fetchone()

    if aux is None:
        print("Cidade não existe")
        return "Cidade não existe"
    else:
        print("Cidade existe " + aux[0])
        sql = """
        SELECT p.predio_nome, p.predio_tipo
        FROM predio p
        JOIN cidade c ON p.cidade_id = c.cidade_nome
        WHERE c.cidade_nome = ?;
        """

        cursor.execute(sql, (nome,))

        aux = cursor.fetchall()

        predios = [list(aux) for aux in aux]

        print(predios)

        return predios