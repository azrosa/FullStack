class TransacaoControl:
    def __init__(self) -> None:
        self.listaTransacoes = []

    def salvarTransacao(self, transacao):
        self.listaTransacoes.append(transacao)
        return 'Transação salva com sucesso!'

    @property
    def listaTransacoes(self):
        return self.__listaTransacoes

    @listaTransacoes.setter
    def listaTransacoes(self, listaTransacoes):
        self.__listaTransacoes = []

    def verificarTransacao(self, numConta):
        valida = False
        for transacao in self.listaTransacoes:
            if numConta == transacao.numConta:
                valida = True
        return valida

    def salvarTransacao(self, transacao):
        self.listaTransacoes.append(transacao)
        return 'Transação salva com sucesso!'

    def excluirTransacao(self, indice):
        if indice != -1:
            del self.listaTransacoes[indice]
            return 'Transação removida com sucesso!'
        return 'Transação não selecionada.'

    def excluirTransacoes(self, numConta):
        count = 0
        lista = []
        for indice, transacao in enumerate(self.listaTransacoes):
            if transacao.numConta == numConta:
                lista.append(indice)
                count += 1
        for indice in sorted(lista, reverse=True):
            del self.listaTransacoes[indice]
        if count == 0:
            return 'Nenhum transação removida.'
        else:
            return f'{count} transações removidas com sucesso!'
