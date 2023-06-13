import xml.etree.ElementTree as ET
import mysql.connector as mycon

database = 'db_banco'
pathXml = 'data/xml/'


def conectarMSQL():
    try:
        conexao = mycon.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="root"
        )
    except mycon.Error as erro:
        print(f"\nERRO: {erro}")
    return conexao


def criarBanco():
    conexao = conectarMSQL()
    cursor = conexao.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    conexao.close()
    print("Banco criado com sucesso.")


def verificarBD():
    conexao = conectarMSQL()
    cursor = conexao.cursor()
    sqlShow = (f"SHOW DATABASES LIKE '{database}'")
    cursor.execute(sqlShow)
    basedados = cursor.fetchall()
    conexao.close()
    if basedados == []:
        criarBanco()
    return True


def conectarBD():
    if verificarBD():
        try:
            banco = mycon.connect(
                host="localhost",
                port=3306,
                user="root",
                passwd="root",
                database=database
            )
        except mycon.Error as erro:
            print(f"\nERRO: {erro}")
        return banco


def criarTabelas():
    banco = conectarBD()
    cursor = banco.cursor()
    comandoCreate = """
CREATE TABLE IF NOT EXISTS sistema (
        id INT NOT NULL AUTO_INCREMENT,
        codigo VARCHAR(15) NOT NULL,
        nome VARCHAR(20) NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS perfil_acesso (
        id INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(20) NOT NULL,
        cod_sistema VARCHAR(15) NOT NULL,
        descricao VARCHAR(200) NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS matriz_sod (
        id INT NOT NULL AUTO_INCREMENT,
        cod_sistema1 VARCHAR(15) NOT NULL,
        nome_perfil1 VARCHAR(20) NOT NULL,
        cod_sistema2 VARCHAR(15) NOT NULL,
        nome_perfil2 VARCHAR(20) NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS usuario (
        id INT NOT NULL AUTO_INCREMENT,
        cpf VARCHAR(11) NOT NULL,
        nome VARCHAR(20) NOT NULL,
        senha VARCHAR(256) NOT NULL,
        nivel_acesso VARCHAR(1) NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS perfil_usuario (
        id INT NOT NULL AUTO_INCREMENT,
        cpf VARCHAR(11) NOT NULL,
        cod_sistema VARCHAR(15) NOT NULL,
        nome_perfil VARCHAR(20) NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS agencia (
        id INT NOT NULL AUTO_INCREMENT,
        numero VARCHAR(4) NOT NULL,
        cidade VARCHAR(20) NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS cliente (
        id INT NOT NULL AUTO_INCREMENT,
        cpf VARCHAR(11) NOT NULL,
        nome VARCHAR(150) NOT NULL,
        endereco VARCHAR(300) NOT NULL,
        contato VARCHAR(15) NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS conta (
        id INT NOT NULL AUTO_INCREMENT,
        numero VARCHAR(11) NOT NULL,
        tipo VARCHAR(20) NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        num_agencia VARCHAR(4) NOT NULL,
        saldo FLOAT NOT NULL,
        limite FLOAT NOT NULL,
        data_abertura DATE NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS tipo_conta (
        id INT NOT NULL AUTO_INCREMENT,
        tipo VARCHAR(20) NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS limite_conta (
        id INT NOT NULL AUTO_INCREMENT,
        categoria VARCHAR(10) NOT NULL,
        valor FLOAT NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS transacao (
        id INT NOT NULL AUTO_INCREMENT,
        num_conta VARCHAR(11) NOT NULL,
        descricao VARCHAR(200) NOT NULL,
        valor FLOAT NOT NULL,
        data DATE NOT NULL,
        PRIMARY KEY (id)
);
    """
    cursor.execute(comandoCreate)
    banco.close()


def verificarTabela(tabela):
    banco = conectarBD()
    cursor = banco.cursor()
    sqlShow = f"SHOW TABLES LIKE '{tabela}'"
    cursor.execute(sqlShow)
    tabelas = cursor.fetchall()
    banco.close()
    if tabelas == []:
        criarTabelas()
        verificarTabela(tabela)
    return True


def inserirDadosXmlTabela(tabela, campos):
    banco = conectarBD()
    cursor = banco.cursor()
    treeXml = ET.parse(f'{pathXml}{tabela}s.xml')
    xml = treeXml.findall(f'{tabela}')
    tcampos = '('
    tvalores = '('
    for i, v in enumerate(xml, start=1):
        for campo in campos:
            valor = v.find(f'{campo}').text
            tcampos += f'{campo}, '
            tvalores += f'"{valor}", '
        tcIndice = tcampos.rfind(',')
        tcampos = f'{tcampos[:tcIndice]})'
        tvIndice = tvalores.rfind(',')
        tvalores = f'{tvalores[:tvIndice]})'
        sql = f'INSERT INTO {tabela}{tcampos} VALUES {tvalores}'
        cursor.execute(sql)
        banco.commit()
        tcampos = '('
        tvalores = '('
        print(f"{i}º {tabela} inserido(a) com sucesso.")
    banco.close()


def inserirCampoXmlTabela(tabela, campo):
    banco = conectarBD()
    cursor = banco.cursor()
    treeXml = ET.parse(f'{pathXml}{tabela}s.xml')
    xml = treeXml.findall(f'{tabela}')
    for i, v in enumerate(xml, start=1):
        valor = v.find(f'{campo}').text
        sql = f'INSERT INTO {tabela}({campo}) VALUES ("{valor}")'
        cursor.execute(sql)
        banco.commit()
        print(f"{tabela} inserido(a) com sucesso.")


def verificarDadosTabela(tabela):
    if verificarTabela(tabela):
        banco = conectarBD()
        cursor = banco.cursor()
        sqlSelect = f"SELECT * FROM {tabela}"
        cursor.execute(sqlSelect)
        dados = cursor.fetchall()
        banco.close()
        if dados == []:
            if tabela == 'sistema':
                campos = ['codigo', 'nome']
                inserirDadosXmlTabela(tabela, campos)
            elif tabela == 'perfil_acesso':
                campos = ['nome', 'cod_sistema', 'descricao']
                inserirDadosXmlTabela(tabela, campos)
            elif tabela == 'matriz_sod':
                campos = ['cod_sistema1', 'nome_perfil1',
                          'cod_sistema2', 'nome_perfil2']
                inserirDadosXmlTabela(tabela, campos)
            if tabela == 'usuario':
                campos = ['cpf', 'nome', 'senha', 'nivel_acesso']
                inserirDadosXmlTabela(tabela, campos)
            elif tabela == 'agencia':
                campos = ['numero', 'cidade']
                inserirDadosXmlTabela(tabela, campos)
            elif tabela == 'cliente':
                campos = ['cpf', 'nome', 'endereco', 'contato']
                inserirDadosXmlTabela(tabela, campos)
            elif tabela == 'tipo_conta':
                inserirCampoXmlTabela(tabela, 'tipo')
            elif tabela == 'limite_conta':
                campos = ['categoria', 'valor']
                inserirDadosXmlTabela(tabela, campos)
            else:
                return False
        return True


def verificarId(tabela, id, numero):
    if verificarDadosTabela(tabela):
        banco = conectarBD()
        cursor = banco.cursor()
        cursor.execute(f"SELECT * FROM {tabela} WHERE {id}='{numero}'")
        dados = cursor.fetchall()
        banco.close()
        if dados == []:
            return False
        else:
            return True
    return False


def adicionarDadosTabela(tabela, campos, valores):
    banco = conectarBD()
    cursor = banco.cursor()
    tcampos = '('
    tvalores = '('
    for campo, valor in zip(campos, valores):
        tcampos += f'{campo}, '
        tvalores += f'"{valor}", '
    tcIndice = tcampos.rfind(',')
    tcampos = f'{tcampos[:tcIndice]})'
    tvIndice = tvalores.rfind(',')
    tvalores = f'{tvalores[:tvIndice]})'
    comandoInsert = f'INSERT INTO {tabela}{tcampos} VALUES {tvalores}'
    cursor.execute(comandoInsert)
    banco.commit()
    tcampos = '('
    tvalores = '('
    print(f"{tabela} inserido(a) com sucesso.")


def inserirDadosTabela(tabela, campos, valores, id, numero):
    if not verificarId(tabela, id, numero):
        banco = conectarBD()
        cursor = banco.cursor()
        tcampos = '('
        tvalores = '('
        for campo, valor in zip(campos, valores):
            tcampos += f'{campo}, '
            tvalores += f'"{valor}", '
        tcIndice = tcampos.rfind(',')
        tcampos = f'{tcampos[:tcIndice]})'
        tvIndice = tvalores.rfind(',')
        tvalores = f'{tvalores[:tvIndice]})'
        comandoInsert = f'INSERT INTO {tabela}{tcampos} VALUES {tvalores}'
        cursor.execute(comandoInsert)
        banco.commit()
        tcampos = '('
        tvalores = '('
        print(f"{tabela} inserido(a) com sucesso.")
    else:
        return False


def inserirCampoTabela(tabela, campo, valor):
    if not verificarId(tabela, campo, valor):
        banco = conectarBD()
        cursor = banco.cursor()
        comandoInsert = f"INSERT INTO {tabela}({campo}) VALUES ('{valor}')"
        cursor.execute(comandoInsert)
        banco.commit()
        banco.close()
        print(f"{campo} inserido(a) com sucesso.")
    else:
        return False


def selecionarDadosTabela(tabela, id=None, numero=None, exceto=None, campo=None, valor=None):
    if verificarDadosTabela(tabela):
        lista = []
        banco = conectarBD()
        cursor = banco.cursor()
        if numero != None:
            sqlSelect = (f"SELECT * FROM {tabela} WHERE {id} = '{numero}'")
        elif exceto != None:
            sqlSelect = (f"SELECT * FROM {tabela} WHERE {id} != '{exceto}'")
        elif valor != None:
            sqlSelect = (
                f"SELECT * FROM {tabela} WHERE {id} = '{numero}' AND {campo}='{valor}'")
        else:
            sqlSelect = (f"SELECT * FROM {tabela}")
        cursor.execute(sqlSelect)
        dados = cursor.fetchall()
        for dado in dados:
            lista.append(dado)
        return lista
        banco.close()
    else:
        print(f"\033[91mTabela {tabela} está vazia.\033[m")
        return False


def selecionarCampoTabela(tabela, campo=None, id=None, numero=None, exceto=None):
    if verificarDadosTabela(tabela):
        lista = []
        banco = conectarBD()
        cursor = banco.cursor()
        if numero != None:
            sqlSelect = (
                f"SELECT {campo} FROM {tabela} WHERE {id} = '{numero}'")
        elif exceto != None:
            sqlSelect = (
                f"SELECT {campo} FROM {tabela} WHERE {id} != '{exceto}'")
        else:
            sqlSelect = (f"SELECT {campo} FROM {tabela}")
        cursor.execute(sqlSelect)
        dados = cursor.fetchall()
        banco.close()
        for dado in dados:
            lista.append(dado)
        return lista
    else:
        print(f"\033[91mTabela {tabela} está vazia.\033[m")
        return False


def atualizarDadosTabela(tabela, id, numero, campos, valores):
    valida = False
    dados = selecionarDadosTabela(tabela, id, numero)
    for campo, valor in zip(campos, valores):
        if dados:
            op = atualizarCampoTabela(tabela, campo, valor, id, numero)
            if op:
                valida = True
            else:
                valida = False
        else:
            print(f"\033[91mTabela {tabela} não possui {id} {numero}.\033[m")
            return False
    return valida


def atualizarCampoTabela(tabela, campo, valor, id, numero):
    dados = selecionarCampoTabela(tabela, campo, id, numero)
    if dados:
        banco = conectarBD()
        cursor = banco.cursor()
        comandoUpdate = f"UPDATE {tabela} SET {campo}='{valor}' WHERE {id}='{numero}'"
        cursor.execute(comandoUpdate)
        banco.commit()
        banco.close()
        return True
    else:
        print(f"\033[91mTabela {tabela} não possui {id} {numero}.\033[m")
        return False


def excluirDadosTabela(tabela, id=None, numero=None, exceto=None, campo=None, valor=None):
    dados = selecionarDadosTabela(tabela, id, numero)
    if dados != []:
        banco = conectarBD()
        cursor = banco.cursor()
        if numero != None:
            sqlDelete = (f"DELETE FROM {tabela} WHERE {id}='{numero}'")
        elif exceto != None:
            sqlSelect = (f"DELETE FROM {tabela} WHERE {id} != '{exceto}'")
        elif valor != None:
            sqlDelete = (
                f"DELETE FROM {tabela} WHERE {id}='{numero}' AND {campo}='{valor}'")
        else:
            sqlDelete = (f"DELETE FROM {tabela}")
        cursor.execute(sqlDelete)
        banco.commit()
        print(f"\033[93mDados apagados com sucesso.\033[m")
        banco.close()
        return True
    else:
        print(f"\033[91mTabela {tabela} não possui {id} {numero}.\033[m")
        return False
