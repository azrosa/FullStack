from hashlib import sha256


class Usuario:
    def __init__(self, cpf=None, nome=None, senha=None, nivelAcesso=None):
        self.cpf = cpf
        self.nome = nome
        self.senha = senha
        self.nivelAcesso = nivelAcesso
        self.erroValidacao = ''

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if cpf != None and (0 < len(cpf) <= 11):
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
        if nome != None and (0 < len(nome) <= 20):
            self.__nome = nome
        else:
            self.erroValidacao = f'O campo "Nome" é obrigatório!'

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        if senha != None and len(senha) != 0:
            self.__senha = sha256(senha.encode()).hexdigest()
        else:
            self.erroValidacao = f'O campo "Senha" é obrigatório!'

    @property
    def nivelAcesso(self):
        return self.__nivelAcesso

    @nivelAcesso.setter
    def nivelAcesso(self, nivelAcesso):
        if nivelAcesso != None and len(nivelAcesso) != 0:
            if nivelAcesso.isnumeric() and (0 < int(nivelAcesso) < 5):
                self.__nivelAcesso = str(nivelAcesso)
            else:
                self.erroValidacao = f'Insira um número de 1 a 4!'
        else:
            self.erroValidacao = f'O campo "Nível de acesso" é obrigatório!'

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
