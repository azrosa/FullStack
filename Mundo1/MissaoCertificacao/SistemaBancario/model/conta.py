class Conta:
    def __init__(self, numero=None, tipoConta=None, cpf=None, numAgencia=None, saldo=None, limite=None, dataAbertura=None):
        self.numero = numero
        self.tipoConta = tipoConta
        self.cpf = cpf
        self.numAgencia = numAgencia
        self.saldo = saldo
        self.limite = limite
        self.dataAbertura = dataAbertura
        self.erroValidacao = ''

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        if numero != None and len(numero) != 0:
            self.__numero = f'{numero:0>11}'
        else:
            self.erroValidacao = f'O campo "Número da Conta" é obrigatório!'

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if cpf != None and (9 < len(cpf) <= 11):
            if cpf.isnumeric():
                self.__cpf = f'{cpf:0>11}'
            else:
                self.erroValidacao = f'Insira um CPF válido!'
        else:
            self.erroValidacao = f'O campo "CPF" é obrigatório!'

    @property
    def numAgencia(self):
        return self.__numAgencia

    @numAgencia.setter
    def numAgencia(self, numAgencia):
        if numAgencia != None and len(numAgencia) != 0:
            if numAgencia.isnumeric() and (0 < int(numAgencia) < 10**4):
                self.__numAgencia = numAgencia
            else:
                self.erroValidacao = f'Selecione uma agência!'
        else:
            self.erroValidacao = f'O campo "Agência" é obrigatório!'

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo != 0:
            self.__saldo = saldo
        else:
            self.erroValidacao = f'O campo "Saldo" é obrigatório!'

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        if limite != 0:
            self.__limite = limite
        else:
            self.erroValidacao = f'O campo "Limite" é obrigatório!'

    @property
    def dataAbertura(self):
        return self.__dataAbertura

    @dataAbertura.setter
    def dataAbertura(self, dataAbertura):
        if dataAbertura != None:
            self.__dataAbertura = dataAbertura
        else:
            self.erroValidacao = f'O campo "Data de Abertura" é obrigatório!'

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:,.2f} realizado com sucesso."

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return f"Saque de R${valor:,.2f} realizado com sucesso."
