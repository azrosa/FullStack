class PAcessoControl:
    def __init__(self) -> None:
        self.listaPAcessos = []

    @property
    def listaPAcessos(self):
        return self.__listaPAcessos

    @listaPAcessos.setter
    def listaPAcessos(self, listaPAcessos):
        self.__listaPAcessos = []

    def verificarPAcesso(self, nome):
        valida = False
        for pAcesso in self.listaPAcessos:
            if nome == pAcesso.nome:
                valida = True
        return valida

    def retornarPAcesso(self, nome):
        for pAcesso in self.listaPAcessos:
            if pAcesso.nome == nome:
                return pAcesso
        return False

    def salvarPAcesso(self, pAcesso):
        self.listaPAcessos.append(pAcesso)
        return 'Perfil de acesso salvo com sucesso!'

    def excluirPAcesso(self, indice):
        if indice != -1:
            del self.listaPAcessos[indice]
            return 'Perfil de acesso removido com sucesso!'
        return 'Perfil de acesso não selecionado.'
