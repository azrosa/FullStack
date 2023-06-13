class SistemaControl:
    def __init__(self) -> None:
        self.listaSistemas = []

    @property
    def listaSistemas(self):
        return self.__listaSistemas

    @listaSistemas.setter
    def listaSistemas(self, listaSistemas):
        self.__listaSistemas = []

    def verificarSistema(self, codigo):
        valida = False
        for sistema in self.listaSistemas:
            if codigo == sistema.codigo:
                valida = True
        return valida

    def retornarSistema(self, codigo):
        for sistema in self.listaSistemas:
            if sistema.codigo == codigo:
                return sistema
        return False

    def salvarSistema(self, sistema):
        self.listaSistemas.append(sistema)
        return 'Sistema salvo com sucesso!'

    def excluirSistema(self, indice):
        if indice != -1:
            del self.listaSistemas[indice]
            return 'Sistema removido com sucesso!'
        return 'Sistema não selecionado.'
