class UsuarioControl:
    def __init__(self) -> None:
        self.listaUsuarios = []

    @property
    def listaUsuarios(self):
        return self.__listaUsuarios

    @listaUsuarios.setter
    def listaUsuarios(self, listaUsuarios):
        self.__listaUsuarios = []

    def verificarUsuario(self, cpf):
        valida = False
        for usuario in self.listaUsuarios:
            if usuario.cpf == cpf:
                valida = True
        return valida

    def retornarUsuario(self, cpf=None, nome=None):
        if cpf != None:
            for usuario in self.listaUsuarios:
                if usuario.cpf == cpf:
                    return usuario
        elif nome != None:
            for usuario in self.listaUsuarios:
                if usuario.nome == nome:
                    return usuario
        else:
            return False

    def salvarUsuario(self, usuario):
        self.listaUsuarios.append(usuario)
        return 'Usuário salvo com sucesso!'

    def excluirUsuario(self, indice):
        if indice != -1:
            del self.listaUsuarios[indice]
            return 'Usuário removido com sucesso!'
        return 'Usuário não selecionado.'
