class PerfilUsuario:
    def __init__(self, cpf=None, codSistema=None, nomePAcesso=None):
        self.cpf = cpf
        self.codSistema = codSistema
        self.nomePAcesso = nomePAcesso
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
    def nomePAcesso(self):
        return self.__nomePAcesso

    @nomePAcesso.setter
    def nomePAcesso(self, nomePAcesso):
        if nomePAcesso != None and (0 < len(nomePAcesso) <= 20):
            self.__nomePAcesso = nomePAcesso
        else:
            self.erroValidacao = f'O campo "Nome" é obrigatório!'

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
