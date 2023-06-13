class Cliente:
    def __init__(self, cpf=None, nome=None, endereco=None, contato=None):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.erroValidacao = ''

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if cpf != None and len(cpf) != 0:
            if self.is_cpf_valido(cpf):
                self.__cpf = cpf
            else:
                self.erroValidacao = f'Insira um CPF válido!'
        else:
            self.erroValidacao = f'O campo "CPF" é obrigatório!'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome != None and len(nome) != 0:
            self.__nome = nome
        else:
            self.erroValidacao = f'O campo "Nome" é obrigatório!'

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        if endereco != None and len(endereco) != 0:
            self.__endereco = endereco
        else:
            self.erroValidacao = f'O campo "Endereço" é obrigatório!'

    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self, contato):
        if contato != None and len(contato) != 0:
            if contato.isnumeric() and (10**8 < int(contato) < 10**9):
                self.__contato = f'{contato:09s}'
            else:
                self.erroValidacao = f'Insira um contato válido!'
        else:
            self.erroValidacao = f'O campo "Contato" é obrigatório!'

    def is_cpf_valido(self, cpf: str) -> bool:
        if len(cpf) != 11:
            return False
        if cpf in (c * 11 for c in "1234567890"):
            return False
        cpf_reverso = cpf[::-1]
        for i in range(2, 0, -1):
            cpf_enumerado = enumerate(cpf_reverso[i:], start=2)
            dv_calculado = sum(
                map(lambda x: int(x[1]) * x[0], cpf_enumerado)) * 10 % 11
            if cpf_reverso[i - 1:i] != str(dv_calculado % 10):
                return False
        return True
