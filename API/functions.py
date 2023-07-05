import sqlite3
import control_unit as admin

bd = "mundo.db"
conn = sqlite3.connect(bd)
cursor = conn.cursor()


def criar_bd():  # Função para criar o banco de dados e inserir dados iniciais

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
        cidade_nome text not null,
        foreign key (cidade_nome) references cidade(cidade_nome)
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
        predio_nome text not null,
        foreign key (predio_nome) references predio(predio_nome)
        );
    """

    try:
        conn.executescript(sql)
        conn.commit()
    except:
        print("Tabela Pessoa já existe")

    pass


def inserir_cidade(nome):  # Função para inserir uma cidade

    sql = """
    select cidade_id from cidade where cidade_nome = (?);
    """

    cursor.execute(sql, (nome,))
    aux = cursor.fetchone()

    if aux is not None:
        print("Cidade já existe")
        return {"message": "Cidade já existe"}
    else:
        print("A criar cidade com nome: " + nome)

    sql_insert = """
       INSERT INTO cidade (cidade_nome) VALUES (?);
       """

    conn.execute(sql_insert, (nome,))
    conn.commit()

    cidade_dict = {
        "cidade_nome": nome
    }

    return cidade_dict


def inserir_predio(nome, tipo, cidade):  # Função para inserir um prédio

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
    insert into predio (predio_nome, predio_tipo, cidade_nome) values (?, ?, ?);
    """

    try:
        conn.execute(sql, (nome, tipo, cidade))
        conn.commit()
    except:
        print("Algo deu errado, tentou-se criar um predio com estes valores: " + nome + ", " + tipo + ", " + cidade)
        return "Aconteceu um erro, verifique os valores inseridos"

    predio_dict = {
        "predio_nome": nome,
        "predio_tipo": tipo,
        "cidade_nome": cidade
    }

    return predio_dict


def inserir_pessoa(nome, emprego, predio):  # Função para inserir uma pessoa

    sql = """
    select pessoa_id from pessoa where pessoa_nome = (?) and emprego = (?) and predio_nome = (?);
    """

    cursor.execute(sql, (nome, emprego, predio))
    aux = cursor.fetchone()

    if aux is not None:
        print("Pessoa já existe")
        return "Pessoa já existe"
    else:
        print("A criar pessoa com nome: " + nome)

    sql = """
    insert into pessoa (pessoa_nome, emprego, predio_nome) values (?, ?, ?);
    """

    try:
        conn.execute(sql, (nome, emprego, predio))
        conn.commit()
    except:
        print("Algo deu errado, tentou-se criar uma pessoa com estes valores: " + nome + ", " + emprego + ", " + predio)
        return "Aconteceu um erro, verifique os valores inseridos"

    pessoa_dict = {
        "pessoa_nome": nome,
        "emprego": emprego,
        "predio_nome": predio
    }

    return pessoa_dict


def listar_cidades():
    sql = """
    SELECT cidade_id, cidade_nome FROM cidade;
    """
    cursor.execute(sql)
    cidades = cursor.fetchall()

    cidades_list = []
    for cidade in cidades:
        cidade_dict = {
            'cidade_id': cidade[0],
            'cidade_nome': cidade[1]
        }
        cidades_list.append(cidade_dict)

    return cidades_list


def listar_pessoas():  # Função para listar as pessoas

    sql = """
    SELECT pessoa_id, pessoa_nome, emprego, predio_nome FROM pessoa ;
    """
    cursor.execute(sql)
    aux = cursor.fetchall()

    pessoas = []
    for pessoa in aux:
        pessoa_dict = {
            'pessoa_id': pessoa[0],
            'pessoa_nome': pessoa[1],
            'emprego': pessoa[2],
            'predio_nome': pessoa[3]
        }
        pessoas.append(pessoa_dict)

    return pessoas

    pass


def listar_pessoa(nome: str):  # Função para listar dados da pessoa
    sql = """
    SELECT pessoa_id, pessoa_nome, emprego, predio_nome FROM pessoa WHERE pessoa_nome = ?;
    """
    cursor.execute(sql, (nome,))
    pessoa = cursor.fetchone()

    if pessoa:
        pessoa_dict = {
            'pessoa_id': pessoa[0],
            'pessoa_nome': pessoa[1],
            'emprego': pessoa[2],
            'predio_nome': pessoa[3]
        }
        return pessoa_dict
    else:
        return {"error": "Pessoa não encontrada"}


def listar_pessoas_predio(nome: str):  # Função para listar pessoas de um prédio
    sql = """
        SELECT predio_id FROM predio WHERE predio_nome = ?;
        """

    cursor.execute(sql, (nome,))
    predio = cursor.fetchone()
    print(predio[0])
    if predio is None:
        print("Prédio não encontrado")
        return []

    sql = """
            SELECT pessoa_nome, emprego
            FROM pessoa
            WHERE predio_nome = ?;
            """

    cursor.execute(sql, (predio[0],))
    pessoas = cursor.fetchall()

    pessoas_list = []
    for pessoa in pessoas:
        pessoa_dict = {
            'pessoa_nome': pessoa[0],
            'emprego': pessoa[1]
        }
        pessoas_list.append(pessoa_dict)

    return pessoas_list

def listar_predios():  # Função para listar os prédios
    sql = """
    SELECT predio_id, predio_nome, predio_tipo, cidade_nome FROM predio;
    """
    cursor.execute(sql)
    aux = cursor.fetchall()

    predios = []
    for predio in aux:
        predio_dict = {
            'predio_id': predio[0],
            'predio_nome': predio[1],
            'predio_tipo': predio[2],
            'cidade_nome': predio[3]
        }
        predios.append(predio_dict)

    return predios


def adquirir_cidade(nome: str):  # Função para mostrar todos os predios da cidade

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
        JOIN cidade c ON p.cidade_nome = c.cidade_nome
        WHERE c.cidade_nome = ?;
        """

        cursor.execute(sql, (nome,))

        aux = cursor.fetchall()

        predios = [list(aux) for aux in aux]

        print(predios)

        return predios

def deletar_cidade(nome: str):  # Função para deletar uma cidade
    sql_select_cidade = """
       SELECT cidade_id FROM cidade WHERE cidade_nome = ?; 
       """

    cursor.execute(sql_select_cidade, (nome,))
    cidade = cursor.fetchone()

    if cidade is None:
        print("Cidade não existe")
        return "Cidade não existe"
    else:
        print("Cidade existe: " + str(cidade[0]))

        cidade_id = cidade[0]

        # Deletar todos os prédios da cidade e suas pessoas associadas
        sql_select_predios = """
           SELECT predio_nome FROM predio WHERE cidade_id = ?;
           """
        cursor.execute(sql_select_predios, (cidade_id,))
        predios = cursor.fetchall()

        for predio in predios:
            predio_id = predio[0]

            # Deletar todas as pessoas do prédio
            sql_delete_pessoas = """
               DELETE FROM pessoa WHERE predio_nome = ?;
               """
            cursor.execute(sql_delete_pessoas, (predio_id,))

            # Deletar o prédio
            sql_delete_predio = """
               DELETE FROM predio WHERE predio_nome = ?;
               """
            cursor.execute(sql_delete_predio, (predio_id,))

        # Deletar a cidade
        sql_delete_cidade = """
           DELETE FROM cidade WHERE cidade_nome = ?;
           """
        cursor.execute(sql_delete_cidade, (nome,))

        conn.commit()

        return "Cidade, prédios e pessoas foram deletados com sucesso"

def deletar_predio(nome: str):  # Função para deletar um predio
    sql_select_predio = """
        SELECT predio_id FROM predio WHERE predio_nome = ?; 
        """

    cursor.execute(sql_select_predio, (nome,))
    predio = cursor.fetchone()

    if predio is None:
        print("Prédio não existe")
        return "Prédio não existe"
    else:
        print("Prédio existe: " + str(predio[0]))

        predio_id = predio[0]

        # Deletar todas as pessoas do prédio
        sql_delete_pessoas = """
            DELETE FROM pessoa WHERE predio_nome = ?;
            """
        cursor.execute(sql_delete_pessoas, (predio_id,))

        # Deletar o prédio
        sql_delete_predio = """
            DELETE FROM predio WHERE predio_nome  = ?;
            """
        cursor.execute(sql_delete_predio, (predio_id,))

        conn.commit()

        return "Prédio e suas pessoas foram deletados com sucesso"

def deletar_pessoa(nome: str):  # Função para deletar uma pessoa

    sql = """
    SELECT pessoa_id from pessoa where pessoa_nome = (?); 
    """

    cursor.execute(sql, (nome,))

    aux = cursor.fetchone()

    if aux is None:
        print("Pessoa não existe")
        return "Pessoa não existe"
    else:
        print("Pessoa existe " + str (aux[0]))
        sql = """
        DELETE FROM pessoa WHERE pessoa_nome = ?;
        """

        cursor.execute(sql, (nome,))

        conn.commit()

        return "Pessoa deletada com sucesso"
def atualizar_cidade(nome: str, novo_nome: str):  # Função para atualizar uma cidade

    sql = """
    SELECT cidade_id from cidade where cidade_nome = (?); 
    """

    cursor.execute(sql, (nome,))

    aux = cursor.fetchone()

    if aux is None:
        print("Cidade não existe")
        return "Cidade não existe"
    else:
        print("Cidade existe " + str( aux[0]))
        sql = """
        UPDATE cidade SET cidade_nome = ? WHERE cidade_nome = ?;
        """

        cursor.execute(sql, (novo_nome, nome))

        conn.commit()

        return "Cidade atualizada com sucesso"
def atualizar_predio(nome: str, novo_nome: str, novo_tipo: str, nova_cidade: str):  # Função para atualizar um predio

    sql_check = """
        SELECT predio_id FROM predio WHERE predio_nome = ?;
        """

    cursor.execute(sql_check, (nome,))
    predio = cursor.fetchone()

    if predio is None:
        print("Predio não existe")
        return "Predio não existe"
    else:
        print("Predio existe " + str(predio[0]))
        sql_update = """
            UPDATE predio SET predio_nome = ?, predio_tipo = ?, cidade_nome = (
                SELECT cidade_id FROM cidade WHERE cidade_nome = ?
            ) WHERE predio_id = ?;
            """

        cursor.execute(sql_update, (novo_nome, novo_tipo, nova_cidade, predio[0]))

        conn.commit()

        return "Predio atualizado com sucesso"

def atualizar_pessoa(nome: str, novo_nome: str, novo_emprego: str, novo_predio: int):  # Função para atualizar uma pessoa

    sql_check = """
        SELECT pessoa_id FROM pessoa WHERE pessoa_nome = ?;
        """

    cursor.execute(sql_check, (nome,))
    pessoa = cursor.fetchone()

    if pessoa is None:
        print("Pessoa não existe")
        return "Pessoa não existe"
    else:
        print("Pessoa existe " + str(pessoa[0]))
        sql_update = """
            UPDATE pessoa SET pessoa_nome = ?, emprego = ?, predio_nome = ? WHERE pessoa_id = ?;
            """

        cursor.execute(sql_update, (novo_nome, novo_emprego, novo_predio, pessoa[0]))

        conn.commit()

        return "Pessoa atualizada com sucesso"
