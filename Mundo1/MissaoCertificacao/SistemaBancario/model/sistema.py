class Sistema:
    def __init__(self, codigo=None, nome=None):
        self.codigo = codigo
        self.nome = nome
        self.erroValidacao = ''

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if codigo != None and (0 < len(codigo) <= 15):
            if codigo.isnumeric() and (0 < int(codigo) < 10**15):
                self.__codigo = f'{codigo:0>15}'
            else:
                self.erroValidacao = f'Insira um código válido!'
        else:
            self.erroValidacao = f'O campo "Código" é obrigatório!'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome != None and (0 < len(nome) <= 20):
            self.__nome = nome
        else:
            self.erroValidacao = f'O campo "Nome" é obrigatório!'
