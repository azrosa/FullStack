class MatrizControl:
    def __init__(self) -> None:
        self.listaMatriz = []

    @property
    def listaMatriz(self):
        # return self.__listaMatriz.sort(key=lambda m: m.codSistema1)
        return self.__listaMatriz

    @listaMatriz.setter
    def listaMatriz(self, listaMatriz):
        self.__listaMatriz = []

    def verificarMatriz(self, cS1, nP1, cS2, nP2):
        valida = False
        for m in self.listaMatriz:
            if m.codSistema1 == cS1 and m.nomePerfil1 == nP1 and m.codSistema2 == cS2 and m.nomePerfil2 == nP2:
                valida = True
        return valida

    def retornarMatriz(self, cS1, nP1, cS2, nP2):
        for m in self.listaMatriz:
            if (m.codSistema1 == cS1 and m.nomePerfil1 == nP1) and (m.codSistema2 == cS2 and m.nomePerfil2 == nP2):
                return m
        return False

    def salvarMatriz(self, matriz):
        self.listaMatriz.append(matriz)
        return 'Matriz salva com sucesso!'

    def excluirMatriz(self, indice):
        if indice != -1:
            del self.listaMatriz[indice]
            return 'Matriz removida com sucesso!'
        return 'Matriz não selecionada.'
