class ClienteControl:
    def __init__(self) -> None:
        self.listaClientes = []

    @property
    def listaClientes(self):
        return self.__listaClientes

    @listaClientes.setter
    def listaClientes(self, listaClientes):
        self.__listaClientes = []

    def verificarCliente(self, cpf):
        valida = False
        for cliente in self.listaClientes:
            if cpf == cliente.cpf:
                valida = True
        return valida

    def retornarCliente(self, cpf):
        for cliente in self.listaClientes:
            if cpf == cliente.cpf:
                return cliente
        return False

    def salvarCliente(self, cliente):
        self.listaClientes.append(cliente)
        return 'Cliente salvo com sucesso!'

    def atualizarCliente(self, cpf, nome, endereco, contato):
        for cliente in self.listaClientes:
            if cliente.cpf == cpf:
                cliente.nome = nome
                cliente.endereco = endereco
                cliente.contato = contato
                return 'Cliente atualizado com sucesso!'
        return 'Cliente não selecionado'

    def excluirCliente(self, indice):
        if indice != -1:
            del self.listaClientes[indice]
            return 'Cliente removido com sucesso!'
        return 'Cliente não selecionado.'
