from random import randint


class ContaControl:
    def __init__(self) -> None:
        self.listaContas = []

    @property
    def listaContas(self):
        return self.__listaContas

    @listaContas.setter
    def listaContas(self, listaContas):
        self.__listaContas = []

    def verificarConta(self, numero):
        valida = False
        for conta in self.listaContas:
            if numero == conta.numero:
                valida = True
        return valida

    def retornarConta(self, numero):
        for conta in self.listaContas:
            if conta.numero == numero:
                return conta
        return False

    def gerarNUmConta(self):
        for i in range(10**4, 10**5):
            if len(str(i)) == 10:
                conta = f'{i:0>11}'
                if not self.verificarConta(conta):
                    break
        return conta

    def gerarNumConta(self):
        count = 0
        for i in range(10**4, 10**5):
            numero = randint(10**4, 10**5)
            if not self.verificarConta(numero):
                break
            count += 1
        return f'{numero:0>9}{count:0>2}'

    def salvarConta(self, conta):
        self.listaContas.append(conta)
        return 'Conta salva com sucesso!'

    def atualizarConta(self, numero, tipoConta, cpf, numAgencia, saldo, limite, dataAbertura):
        for conta in self.listaContas:
            if conta.numero == numero:
                conta.tipoConta = tipoConta
                conta.cpf = cpf
                conta.numAgencia = numAgencia
                conta.saldo = saldo
                conta.limite = limite
                conta.dataAbertura = dataAbertura
                return 'Conta atualizada com sucesso!'
        return 'Conta não selecionada'

    def excluirConta(self, indice):
        if indice != -1:
            del self.listaContas[indice]
            return 'Conta removida com sucesso!'
        return 'Conta não selecionada.'
