class Agencia:
    def __init__(self, numero=None, cidade=None):
        self.numero = numero
        self.cidade = cidade
        self.erroValidacao = ''

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        if numero != None and (0 < len(numero) <= 4):
            if numero.isnumeric() and int(numero) > 0:
                self.__numero = f'{numero:0>4}'
            else:
                self.erroValidacao = f'Insira um número válido!'
        else:
            self.erroValidacao = f'O campo "Número da Agência" é obrigatório!'

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        if cidade != None and (0 < len(cidade) <= 20):
            self.__cidade = cidade
        else:
            self.erroValidacao = f'O campo "Cidade" é obrigatório!'
