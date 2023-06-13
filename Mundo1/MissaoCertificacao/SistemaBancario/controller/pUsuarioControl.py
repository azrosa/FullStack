class PUsuarioControl:
    def __init__(self) -> None:
        self.listaPUsuarios = []

    @property
    def listaPUsuarios(self):
        return self.__listaPUsuarios

    @listaPUsuarios.setter
    def listaPUsuarios(self, listaPUsuarios):
        self.__listaPUsuarios = []

    def verificarPUsuario(self, cpf):
        valida = False
        for pUsuario in self.listaPUsuarios:
            if cpf == pUsuario.cpf:
                valida = True
        return valida

    def retornarPUsuario(self, cpf, codSistema, nomePAcesso):
        for pUsuario in self.listaPUsuarios:
            if pUsuario.cpf == cpf and pUsuario.codSistema == codSistema and pUsuario.nomePAcesso == nomePAcesso:
                return pUsuario
        return False

    def retornarPUsuarios(self, cpf):
        lista = []
        for pUsuario in self.listaPUsuarios:
            if cpf == pUsuario.cpf:
                lista.append(pUsuario)
        return lista

    def salvarPUsuario(self, pUsuario):
        self.listaPUsuarios.append(pUsuario)
        return 'Perfil de usuário salvo com sucesso!'

    def excluirPUsuario(self, indice):
        if indice != -1:
            del self.listaPUsuarios[indice]
            return 'Perfil de usuário removido com sucesso!'
        return 'Perfil de usuário não selecionado.'
