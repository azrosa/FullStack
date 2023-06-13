class PerfilAcesso:
    def __init__(self, nome=None, codSistema=None, descricao=None):
        self.nome = nome
        self.codSistema = codSistema
        self.descricao = descricao
        self.erroValidacao = ''

    @property
    def codSistema(self):
        return self.__codSistema

    @codSistema.setter
    def codSistema(self, codSistema):
        if codSistema != None and (0 < len(codSistema) <= 15):
            if codSistema.isnumeric() and int(codSistema) > 0:
                self.__codSistema = f'{codSistema:0>15}'
            else:
                self.erroValidacao = f'Insira um código válido!'
        else:
            self.erroValidacao = f'O campo "Código do Sistema" é obrigatório!'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome != None and (0 < len(nome) <= 20):
            self.__nome = nome
        else:
            self.erroValidacao = f'O campo "Nome" é obrigatório!'

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if descricao != None and (0 < len(descricao) <= 200):
            self.__descricao = descricao
        else:
            self.erroValidacao = f'O campo "Descrição" é obrigatório!'
