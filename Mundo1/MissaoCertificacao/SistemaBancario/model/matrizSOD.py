class MatrizSOD:
    def __init__(self, codSistema1=None, nomePerfil1=None, codSistema2=None, nomePerfil2=None):
        self.codSistema1 = codSistema1
        self.nomePerfil1 = nomePerfil1
        self.codSistema2 = codSistema2
        self.nomePerfil2 = nomePerfil2
        self.erroValidacao = ''

    @property
    def codSistema1(self):
        return self.__codSistema1

    @codSistema1.setter
    def codSistema1(self, codSistema1):
        if codSistema1 != None and (0 < len(codSistema1) <= 15):
            if codSistema1.isnumeric() and int(codSistema1) > 0:
                self.__codSistema1 = f'{codSistema1:0>15}'
            else:
                self.erroValidacao = f'Insira um código válido!'
        else:
            self.erroValidacao = f'O campo "Código do Sistema 1" é obrigatório!'

    @property
    def nomePerfil1(self):
        return self.__nomePerfil1

    @nomePerfil1.setter
    def nomePerfil1(self, nomePerfil1):
        if nomePerfil1 != None and (0 < len(nomePerfil1) <= 20):
            self.__nomePerfil1 = nomePerfil1
        else:
            self.erroValidacao = f'O campo "Nome do Perfil 1" é obrigatório!'

    @property
    def codSistema2(self):
        return self.__codSistema2

    @codSistema2.setter
    def codSistema2(self, codSistema2):
        if codSistema2 != None and (0 < len(codSistema2) <= 15):
            if codSistema2.isnumeric() and int(codSistema2) > 0:
                self.__codSistema2 = f'{codSistema2:0>15}'
            else:
                self.erroValidacao = f'Insira um código válido!'
        else:
            self.erroValidacao = f'O campo "Código do Sistema 2" é obrigatório!'

    @property
    def nomePerfil2(self):
        return self.__nomePerfil2

    @nomePerfil2.setter
    def nomePerfil2(self, nomePerfil2):
        if nomePerfil2 != None and (0 < len(nomePerfil2) <= 20):
            self.__nomePerfil2 = nomePerfil2
        else:
            self.erroValidacao = f'O campo "Nome do Perfil 2" é obrigatório!'
