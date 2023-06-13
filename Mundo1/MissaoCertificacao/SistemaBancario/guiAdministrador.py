import data.conexao as con
from datetime import datetime as dt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from model.sistema import Sistema
from model.perfilAcesso import PerfilAcesso
from model.matrizSOD import MatrizSOD
from model.usuario import Usuario
from model.perfilUsuario import PerfilUsuario
from view.telaAdministrador import Ui_MainWindow
from controller.sistemaControl import SistemaControl
from controller.pAcessoControl import PAcessoControl
from controller.matrizControl import MatrizControl
from controller.usuarioControl import UsuarioControl
from controller.pUsuarioControl import PUsuarioControl


class GUIAdministrador(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.numeroId = ''
        self.controleSistema = SistemaControl()
        self.controlePAcesso = PAcessoControl()
        self.controleMatriz = MatrizControl()
        self.controleUsuario = UsuarioControl()
        self.controlePUsuario = PUsuarioControl()
        self.init_components()
        self.corSucesso = "background-color: rgb(209, 255, 209);"
        self.corErro = "background-color: rgb(250, 185, 185);"

    def init_components(self):
        self.label_logo.setPixmap(QPixmap('img\logoV.png'))
        self.pushButton_sistema.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_sistemas))
        self.pushButton_pAcesso.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_pAcessos))
        self.pushButton_matriz.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_matriz))
        self.pushButton_usuario.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_usuarios))
        self.pushButton_pUsuario.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_pUsuarios))

        self.pushButton_salvarSistema.clicked.connect(self.salvarSistema)
        self.pushButton_limparSistema.clicked.connect(self.limparSistema)
        self.pushButton_editarSistema.clicked.connect(self.editarSistema)
        self.pushButton_consultarSistema.clicked.connect(self.consultarSistema)
        self.pushButton_excluirSistema.clicked.connect(self.excluirSistema)
        self.pushButton_voltarListaSistemas.clicked.connect(
            self.voltarListaSistemas)
        self.pushButton_atualizarSistema.clicked.connect(self.atualizarSistema)

        self.pushButton_salvarPAcesso.clicked.connect(self.salvarPAcesso)
        self.pushButton_limparPAcesso.clicked.connect(self.limparPAcesso)
        self.pushButton_editarPAcesso.clicked.connect(self.editarPAcesso)
        self.pushButton_consultarPAcesso.clicked.connect(self.consultarPAcesso)
        self.pushButton_excluirPAcesso.clicked.connect(self.excluirPAcesso)
        self.pushButton_voltarListaPAcessos.clicked.connect(
            self.voltarListaPAcessos)
        self.pushButton_atualizarPAcesso.clicked.connect(self.atualizarPAcesso)

        self.pushButton_salvarMatriz.clicked.connect(self.salvarMatriz)
        self.pushButton_limparMatriz.clicked.connect(self.limparMatriz)
        self.pushButton_consultarMatriz.clicked.connect(self.consultarMatriz)
        self.pushButton_excluirMatriz.clicked.connect(self.excluirMatriz)
        self.pushButton_voltarListaMatriz.clicked.connect(
            self.voltarListaMatriz)
        self.comboBox_sistemas1Matriz.currentIndexChanged.connect(
            self.filtrarPAcessos1Matriz)
        self.comboBox_sistemas2Matriz.currentIndexChanged.connect(
            self.filtrarPAcessos2Matriz)

        self.pushButton_salvarUsuario.clicked.connect(self.salvarUsuario)
        self.pushButton_limparUsuario.clicked.connect(self.limparUsuario)
        self.pushButton_editarUsuario.clicked.connect(self.editarUsuario)
        self.pushButton_consultarUsuario.clicked.connect(self.consultarUsuario)
        self.pushButton_excluirUsuario.clicked.connect(self.excluirUsuario)
        self.pushButton_voltarListaUsuarios.clicked.connect(
            self.voltarListaUsuarios)
        self.pushButton_atualizarUsuario.clicked.connect(self.atualizarUsuario)

        self.pushButton_salvarPUsuario.clicked.connect(self.salvarPUsuario)
        self.pushButton_limparPUsuario.clicked.connect(self.limparPUsuario)
        self.pushButton_consultarPUsuario.clicked.connect(
            self.consultarPUsuario)
        self.pushButton_excluirPUsuario.clicked.connect(self.excluirPUsuario)
        self.pushButton_voltarListaPUsuarios.clicked.connect(
            self.voltarListaPUsuarios)
        self.comboBox_sistemasPUsuario.currentIndexChanged.connect(
            self.filtrarPAcessosPUsuario)

        self.frame_msgBar.hide()
        self.pushButton_fecharMsg.clicked.connect(
            lambda: self.frame_msgBar.hide())
        self.initBD()

    def initBD(self):
        sistemas = con.selecionarDadosTabela('sistema')
        lsSistemas = ['--- Selecione ---']
        if sistemas:
            for s in sistemas:
                sistema = Sistema(s[1], s[2])
                self.controleSistema.salvarSistema(sistema)
            for sis in self.controleSistema.listaSistemas:
                lsSistemas.append(sis.nome)
            self.listarSistemas()
        self.comboBox_sistemasPAcesso.addItems(lsSistemas)
        self.comboBox_sistemas1Matriz.addItems(lsSistemas)
        self.comboBox_sistemas2Matriz.addItems(lsSistemas)
        self.comboBox_sistemasPUsuario.addItems(lsSistemas)
        pAcessos = con.selecionarDadosTabela('perfil_acesso')
        lsPAcessos = ['--- Selecione ---']
        if pAcessos:
            for pa in pAcessos:
                pAcesso = PerfilAcesso(pa[1], pa[2], pa[3])
                self.controlePAcesso.salvarPAcesso(pAcesso)
            for pas in self.controlePAcesso.listaPAcessos:
                lsPAcessos.append(pas.nome)
            self.listarPAcessos()
        self.comboBox_pAcessos1Matriz.addItems(lsPAcessos)
        self.comboBox_pAcessos2Matriz.addItems(lsPAcessos)
        self.comboBox_pAcessosPUsuario.addItems(lsPAcessos)
        matriz = con.selecionarDadosTabela('matriz_sod')
        if matriz:
            for ma in matriz:
                mat = MatrizSOD(ma[1], ma[2], ma[3], ma[4])
                self.controleMatriz.salvarMatriz(mat)
            self.listarMatriz()
        usuarios = con.selecionarDadosTabela('usuario')
        if usuarios:
            for u in usuarios:
                usuario = Usuario(u[1], u[2], u[3], u[4])
                self.controleUsuario.salvarUsuario(usuario)
            self.listarUsuarios()
        pUsuarios = con.selecionarDadosTabela('perfil_usuario')
        if pUsuarios:
            for pu in pUsuarios:
                pUsuario = PerfilUsuario(pu[1], pu[2], pu[3])
                self.controlePUsuario.salvarPUsuario(pUsuario)
            self.listarPUsuarios()

    def listarSistemas(self):
        contLinhas = 0
        self.tableWidget_sistemas.clearContents()
        self.tableWidget_sistemas.setRowCount(
            len(self.controleSistema.listaSistemas))
        for sistema in self.controleSistema.listaSistemas:
            self.tableWidget_sistemas.setItem(
                contLinhas, 0, QTableWidgetItem(sistema.codigo))
            self.tableWidget_sistemas.setItem(
                contLinhas, 1, QTableWidgetItem(sistema.nome))
            contLinhas += 1

    def salvarSistema(self):
        sistema = Sistema()
        sistema.codigo = self.lineEdit_codSistema.text()
        sistema.nome = self.lineEdit_nomeSistema.text()
        if len(sistema.erroValidacao) != 0:
            self.label_msg.setText(sistema.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            if self.controleSistema.verificarSistema(sistema.codigo):
                sistema.erroValidacao = f'Sistema {sistema.codigo} já está cadastrado.'
                self.label_msg.setText(sistema.erroValidacao)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                campos = ['codigo', 'nome']
                valores = [sistema.codigo, sistema.nome]
                con.inserirDadosTabela(
                    'sistema', campos, valores, 'codigo', sistema.codigo)
                msg = self.controleSistema.salvarSistema(sistema)
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.comboBox_sistemasPAcesso.addItem(sistema.nome)
                self.comboBox_sistemas1Matriz.addItem(sistema.nome)
                self.comboBox_sistemas2Matriz.addItem(sistema.nome)
                self.comboBox_sistemasPUsuario.addItem(sistema.nome)
                self.listarSistemas()

    def limparSistema(self):
        self.lineEdit_codSistema.clear()
        self.lineEdit_nomeSistema.clear()

    def consultarSistema(self):
        indice = self.tableWidget_sistemas.currentRow()
        if indice != -1:
            sistemas = con.selecionarCampoTabela('sistema', 'codigo')
            codigo = sistemas[indice][0]
            self.numeroId = codigo
            sistema = con.selecionarDadosTabela('sistema', 'codigo', codigo)
            self.label_consultarCodSistema.setText(sistema[0][1])
            self.label_consultarNomeSistema.setText(sistema[0][2])
            self.tabWidget_sistemas.setCurrentIndex(2)
        else:
            self.label_msg.setText('Sistema não selecionado.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def voltarListaSistemas(self):
        self.label_consultarCodSistema.clear()
        self.label_consultarNomeSistema.clear()
        self.numeroId = ''
        self.tabWidget_sistemas.setCurrentIndex(1)

    def editarSistema(self):
        indice = self.tableWidget_sistemas.currentRow()
        if indice != -1:
            sistemas = con.selecionarCampoTabela('sistema', 'codigo')
            codigo = sistemas[indice][0]
            self.numeroId = codigo
            sistema = con.selecionarDadosTabela('sistema', 'codigo', codigo)
            self.label_editarCodSistema.setText(sistema[0][1])
            self.lineEdit_editarNomeSistema.setText(sistema[0][2])
            self.tabWidget_sistemas.setCurrentIndex(3)
        else:
            self.label_msg.setText('Sistema não selecionado.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def atualizarSistema(self):
        codigo = self.numeroId
        if codigo != None and len(codigo) != 0:
            sistema = self.controleSistema.retornarSistema(codigo)
            if sistema:
                sistema.nome = self.lineEdit_editarNomeSistema.text()
                if len(sistema.erroValidacao) != 0:
                    self.label_msg.setText(sistema.erroValidacao)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                    sistema.erroValidacao = ''
                else:
                    campos = ['nome']
                    valores = [sistema.nome]
                    con.atualizarDadosTabela(
                        'sistema', 'codigo', sistema.codigo, campos, valores)
                    msg = 'Sistema atualizado com sucesso!'
                    self.label_msg.setText(msg)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corSucesso)
                    self.label_editarCodSistema.clear()
                    self.lineEdit_editarNomeSistema.clear()
                    self.numeroId = ''
                    self.tabWidget_sistemas.setCurrentIndex(1)
                    self.comboBox_sistemasPAcesso.clear()
                    self.comboBox_sistemas1Matriz.clear()
                    self.comboBox_sistemas2Matriz.clear()
                    self.comboBox_sistemasPUsuario.clear()
                    lsSistemas = ['--- Selecione ---']
                    for sis in self.controleSistema.listaSistemas:
                        lsSistemas.append(sis.nome)
                    self.comboBox_sistemasPAcesso.addItems(lsSistemas)
                    self.comboBox_sistemas1Matriz.addItems(lsSistemas)
                    self.comboBox_sistemas2Matriz.addItems(lsSistemas)
                    self.comboBox_sistemasPUsuario.addItems(lsSistemas)
                    self.listarSistemas()

    def excluirSistema(self):
        indice = self.tableWidget_sistemas.currentRow()
        if indice != -1:
            sistemas = con.selecionarCampoTabela('sistema', 'codigo')
            codigo = sistemas[indice][0]
            perfis = con.selecionarDadosTabela(
                'perfil_acesso', 'cod_sistema', codigo)
            if perfis:
                self.label_msg.setText(
                    'Sistema possui perfil(is) vinculado(s).')
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                con.excluirDadosTabela('sistema', 'codigo', codigo)
                msg = self.controleSistema.excluirSistema(indice)
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.comboBox_sistemasPAcesso.clear()
                self.comboBox_sistemas1Matriz.clear()
                self.comboBox_sistemas2Matriz.clear()
                self.comboBox_sistemasPUsuario.clear()
                lsSistemas = ['--- Selecione ---']
                for sis in self.controleSistema.listaSistemas:
                    lsSistemas.append(sis.nome)
                self.comboBox_sistemasPAcesso.addItems(lsSistemas)
                self.comboBox_sistemas1Matriz.addItems(lsSistemas)
                self.comboBox_sistemas2Matriz.addItems(lsSistemas)
                self.comboBox_sistemasPUsuario.addItems(lsSistemas)
                self.listarSistemas()
        else:
            msg = self.controleSistema.excluirSistema(indice)
            self.label_msg.setText(msg)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def listarPAcessos(self):
        contLinhas = 0
        self.tableWidget_pAcessos.clearContents()
        self.tableWidget_pAcessos.setRowCount(
            len(self.controlePAcesso.listaPAcessos))
        for pAcesso in self.controlePAcesso.listaPAcessos:
            self.tableWidget_pAcessos.setItem(
                contLinhas, 0, QTableWidgetItem(pAcesso.nome))
            self.tableWidget_pAcessos.setItem(
                contLinhas, 1, QTableWidgetItem(pAcesso.codSistema))
            self.tableWidget_pAcessos.setItem(
                contLinhas, 2, QTableWidgetItem(pAcesso.descricao))
            contLinhas += 1

    def salvarPAcesso(self):
        pAcesso = PerfilAcesso()
        pAcesso.nome = self.lineEdit_nomePAcesso.text()
        pAcesso.descricao = self.plainTextEdit_descricaoPAcesso.toPlainText()
        if len(pAcesso.erroValidacao) != 0:
            self.label_msg.setText(pAcesso.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            if self.controlePAcesso.verificarPAcesso(pAcesso.nome):
                pAcesso.erroValidacao = f'Perfil de Acesso {pAcesso.nome} já está cadastrado.'
            nomeSistema = self.comboBox_sistemasPAcesso.currentText()
            if len(nomeSistema) == 0 or 'Selecione' in nomeSistema:
                pAcesso.erroValidacao = f'Selecione o Sistema.'
            if len(pAcesso.erroValidacao) != 0:
                self.label_msg.setText(pAcesso.erroValidacao)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                sistema = con.selecionarCampoTabela(
                    'sistema', 'codigo', 'nome', nomeSistema)
                pAcesso.codSistema = sistema[0][0]
                if len(pAcesso.erroValidacao) != 0:
                    self.label_msg.setText(pAcesso.erroValidacao)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                else:
                    campos = ['nome', 'cod_sistema', 'descricao']
                    valores = [pAcesso.nome,
                               pAcesso.codSistema, pAcesso.descricao]
                    con.inserirDadosTabela(
                        'perfil_acesso', campos, valores, 'nome', pAcesso.nome)
                    msg = self.controlePAcesso.salvarPAcesso(pAcesso)
                    self.label_msg.setText(msg)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corSucesso)
                    self.comboBox_pAcessos1Matriz.addItem(pAcesso.nome)
                    self.comboBox_pAcessos2Matriz.addItem(pAcesso.nome)
                    self.comboBox_pAcessosPUsuario.addItem(pAcesso.nome)
                    self.listarPAcessos()

    def limparPAcesso(self):
        self.lineEdit_nomePAcesso.clear()
        self.plainTextEdit_descricaoPAcesso.clear()
        self.comboBox_sistemasPAcesso.setCurrentIndex(0)

    def consultarPAcesso(self):
        indice = self.tableWidget_pAcessos.currentRow()
        if indice != -1:
            pAcessos = con.selecionarCampoTabela('perfil_acesso', 'nome')
            nome = pAcessos[indice][0]
            pAcesso = con.selecionarDadosTabela('perfil_acesso', 'nome', nome)
            self.label_consultarNomePAcesso.setText(pAcesso[0][1])
            self.label_consultarSistemaPAcesso.setText(pAcesso[0][2])
            self.label_consultarDescricaoPAcesso.setText(pAcesso[0][3])
            self.tabWidget_pAcessos.setCurrentIndex(2)
        else:
            self.label_msg.setText('Perfil de acesso não selecionado.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def voltarListaPAcessos(self):
        self.label_consultarNomePAcesso.clear()
        self.label_consultarSistemaPAcesso.clear()
        self.label_consultarDescricaoPAcesso.clear()
        self.tabWidget_pAcessos.setCurrentIndex(1)

    def editarPAcesso(self):
        indice = self.tableWidget_pAcessos.currentRow()
        if indice != -1:
            pAcessos = con.selecionarCampoTabela('perfil_acesso', 'nome')
            nome = pAcessos[indice][0]
            self.numeroId = nome
            pAcesso = con.selecionarDadosTabela('perfil_acesso', 'nome', nome)
            self.label_editarNomePAcesso.setText(pAcesso[0][1])
            self.label_editarSistemaPAcesso.setText(pAcesso[0][2])
            self.plainTextEdit_editarDescricaoPAcesso.setPlainText(
                pAcesso[0][3])
            self.tabWidget_pAcessos.setCurrentIndex(3)
        else:
            self.label_msg.setText('Perfil de acesso não selecionado.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def atualizarPAcesso(self):
        nome = self.numeroId
        if nome != None and len(nome) != 0:
            pAcesso = self.controlePAcesso.retornarPAcesso(nome)
            if pAcesso:
                pAcesso.descricao = self.plainTextEdit_editarDescricaoPAcesso.toPlainText()
                if len(pAcesso.erroValidacao) != 0:
                    self.label_msg.setText(pAcesso.erroValidacao)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                    pAcesso.erroValidacao = ''
                else:
                    campos = ['descricao']
                    valores = [pAcesso.descricao]
                    con.atualizarDadosTabela(
                        'perfil_acesso', 'nome', pAcesso.nome, campos, valores)
                    msg = 'Perfil de acesso atualizado com sucesso!'
                    self.label_msg.setText(msg)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corSucesso)
                    self.label_editarNomePAcesso.clear()
                    self.label_editarSistemaPAcesso.clear()
                    self.plainTextEdit_editarDescricaoPAcesso.clear()
                    self.numeroId = ''
                    self.tabWidget_pAcessos.setCurrentIndex(1)
                    self.comboBox_pAcessos1Matriz.clear()
                    self.comboBox_pAcessos2Matriz.clear()
                    self.comboBox_pAcessosPUsuario.clear()
                    lsPAcessos = ['--- Selecione ---']
                    for pas in self.controlePAcesso.listaPAcessos:
                        lsPAcessos.append(pas.nome)
                    self.comboBox_pAcessos1Matriz.addItems(lsPAcessos)
                    self.comboBox_pAcessos2Matriz.addItems(lsPAcessos)
                    self.comboBox_pAcessosPUsuario.addItems(lsPAcessos)
                    self.listarPAcessos()

    def excluirPAcesso(self):
        indice = self.tableWidget_pAcessos.currentRow()
        if indice != -1:
            pAcessos = con.selecionarCampoTabela('perfil_acesso', 'nome')
            nome = pAcessos[indice][0]
            matriz1 = con.selecionarDadosTabela(
                'matriz_sod', 'nome_perfil1', nome)
            matriz2 = con.selecionarDadosTabela(
                'matriz_sod', 'nome_perfil2', nome)
            pUsuario = con.selecionarDadosTabela(
                'perfil_usuario', 'nome_perfil', nome)
            if matriz1 or matriz2 or pUsuario:
                self.label_msg.setText(
                    'Perfil está vinculado a um usuário ou à matriz SOD.')
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                con.excluirDadosTabela('perfil_acesso', 'nome', nome)
                msg = self.controlePAcesso.excluirPAcesso(indice)
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.comboBox_pAcessos1Matriz.clear()
                self.comboBox_pAcessos2Matriz.clear()
                self.comboBox_pAcessosPUsuario.clear()
                lsPAcessos = ['--- Selecione ---']
                for pas in self.controlePAcesso.listaPAcessos:
                    lsPAcessos.append(pas.nome)
                self.comboBox_pAcessos1Matriz.addItems(lsPAcessos)
                self.comboBox_pAcessos2Matriz.addItems(lsPAcessos)
                self.comboBox_pAcessosPUsuario.addItems(lsPAcessos)
                self.listarPAcessos()
        else:
            msg = self.controlePAcesso.excluirPAcesso(indice)
            self.label_msg.setText(msg)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def filtrarPAcessos1Matriz(self, index):
        if index != -1:
            nomeSistema = self.comboBox_sistemas1Matriz.itemText(index)
            if nomeSistema != '--- Selecione ---':
                sistema = con.selecionarCampoTabela(
                    'sistema', 'codigo', 'nome', nomeSistema)
                codSistema = sistema[0][0]
                pAcessos = con.selecionarCampoTabela(
                    'perfil_acesso', 'nome', 'cod_sistema', codSistema)
                lista = list(map(lambda p: str(p[0]), pAcessos))
                lista.append('--- Selecione ---')
                lista.sort()
                self.comboBox_pAcessos1Matriz.clear()
                self.comboBox_pAcessos1Matriz.addItems(lista)

    def filtrarPAcessos2Matriz(self, index):
        if index != -1:
            nomeSistema = self.comboBox_sistemas2Matriz.itemText(index)
            if nomeSistema != '--- Selecione ---':
                sistema = con.selecionarCampoTabela(
                    'sistema', 'codigo', 'nome', nomeSistema)
                codSistema = sistema[0][0]
                pAcessos = con.selecionarCampoTabela(
                    'perfil_acesso', 'nome', 'cod_sistema', codSistema)
                lista = list(map(lambda p: str(p[0]), pAcessos))
                lista.append('--- Selecione ---')
                lista.sort()
                self.comboBox_pAcessos2Matriz.clear()
                self.comboBox_pAcessos2Matriz.addItems(lista)

    def filtrarPAcessosPUsuario(self, index):
        if index != -1:
            nomeSistema = self.comboBox_sistemasPUsuario.itemText(index)
            if nomeSistema != '--- Selecione ---':
                sistema = con.selecionarCampoTabela(
                    'sistema', 'codigo', 'nome', nomeSistema)
                codSistema = sistema[0][0]
                pAcessos = con.selecionarCampoTabela(
                    'perfil_acesso', 'nome', 'cod_sistema', codSistema)
                lista = list(map(lambda p: str(p[0]), pAcessos))
                lista.append('--- Selecione ---')
                lista.sort()
                self.comboBox_pAcessosPUsuario.clear()
                self.comboBox_pAcessosPUsuario.addItems(lista)

    def listarMatriz(self):
        contLinhas = 0
        self.tableWidget_matriz.clearContents()
        self.tableWidget_matriz.setRowCount(
            len(self.controleMatriz.listaMatriz))
        for matriz in self.controleMatriz.listaMatriz:
            self.tableWidget_matriz.setItem(
                contLinhas, 0, QTableWidgetItem(matriz.codSistema1))
            self.tableWidget_matriz.setItem(
                contLinhas, 1, QTableWidgetItem(matriz.nomePerfil1))
            self.tableWidget_matriz.setItem(
                contLinhas, 2, QTableWidgetItem(matriz.codSistema2))
            self.tableWidget_matriz.setItem(
                contLinhas, 3, QTableWidgetItem(matriz.nomePerfil2))
            contLinhas += 1

    def salvarMatriz(self):
        matriz = MatrizSOD()
        nomeSistema1 = self.comboBox_sistemas1Matriz.currentText()
        if len(nomeSistema1) == 0 or 'Selecione' in nomeSistema1:
            matriz.erroValidacao = f'Selecione o sistema 1.'
        pAcesso1 = self.comboBox_pAcessos1Matriz.currentText()
        if len(pAcesso1) == 0 or 'Selecione' in pAcesso1:
            matriz.erroValidacao = f'Selecione o perfil de acesso 1.'
        nomeSistema2 = self.comboBox_sistemas2Matriz.currentText()
        if len(nomeSistema2) == 0 or 'Selecione' in nomeSistema2:
            matriz.erroValidacao = f'Selecione o sistema 2.'
        pAcesso2 = self.comboBox_pAcessos2Matriz.currentText()
        if len(pAcesso2) == 0 or 'Selecione' in pAcesso2:
            matriz.erroValidacao = f'Selecione o perfil de acesso 2.'
        if len(matriz.erroValidacao) != 0:
            self.label_msg.setText(matriz.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            codSistema1 = con.selecionarCampoTabela(
                'sistema', 'codigo', 'nome', nomeSistema1)
            matriz.codSistema1 = str(codSistema1[0][0])
            matriz.nomePerfil1 = pAcesso1
            codSistema2 = con.selecionarCampoTabela(
                'sistema', 'codigo', 'nome', nomeSistema2)
            matriz.codSistema2 = str(codSistema2[0][0])
            matriz.nomePerfil2 = pAcesso2
            if len(matriz.erroValidacao) != 0:
                self.label_msg.setText(matriz.erroValidacao)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                if self.controleMatriz.verificarMatriz(matriz.codSistema1, matriz.nomePerfil1, matriz.codSistema2, matriz.nomePerfil2):
                    matriz.erroValidacao = f'Matriz já está cadastrada.'
                    self.label_msg.setText(matriz.erroValidacao)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                else:
                    campos = ['cod_sistema1', 'nome_perfil1',
                              'cod_sistema2', 'nome_perfil2']
                    valores = [matriz.codSistema1, matriz.nomePerfil1,
                               matriz.codSistema2, matriz.nomePerfil2]
                    con.adicionarDadosTabela('matriz_sod', campos, valores)
                    msg = self.controleMatriz.salvarMatriz(matriz)
                    self.label_msg.setText(msg)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corSucesso)
                    self.listarMatriz()

    def limparMatriz(self):
        self.comboBox_sistemas1Matriz.setCurrentIndex(0)
        self.comboBox_pAcessos1Matriz.setCurrentIndex(0)
        self.comboBox_sistemas2Matriz.setCurrentIndex(0)
        self.comboBox_pAcessos2Matriz.setCurrentIndex(0)

    def consultarMatriz(self):
        indice = self.tableWidget_matriz.currentRow()
        if indice != -1:
            matrizI = con.selecionarDadosTabela('matriz_sod')
            cS1 = matrizI[indice][1]
            nP1 = matrizI[indice][2]
            cS2 = matrizI[indice][3]
            nP2 = matrizI[indice][4]
            matriz = self.controleMatriz.retornarMatriz(
                cS1=cS1, nP1=nP1, cS2=cS2, nP2=nP2)
            if matriz:
                self.label_consultarSistema1Matriz.setText(matriz.codSistema1)
                self.label_consultarPAcesso1Matriz.setText(matriz.nomePerfil1)
                self.label_consultarSistema2Matriz.setText(matriz.codSistema2)
                self.label_consultarPAcesso2Matriz.setText(matriz.nomePerfil2)
                self.tabWidget_matriz.setCurrentIndex(2)
        else:
            self.label_msg.setText('Matriz não selecionada.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def voltarListaMatriz(self):
        self.label_consultarSistema1Matriz.clear()
        self.label_consultarPAcesso1Matriz.clear()
        self.label_consultarSistema2Matriz.clear()
        self.label_consultarPAcesso2Matriz.clear()
        self.tabWidget_matriz.setCurrentIndex(1)

    def excluirMatriz(self):
        indice = self.tableWidget_matriz.currentRow()
        if indice != -1:
            matrizI = con.selecionarDadosTabela('matriz_sod', 'cod_sistema1')
            cS1 = matrizI[indice][1]
            nP1 = matrizI[indice][2]
            cS2 = matrizI[indice][3]
            nP2 = matrizI[indice][4]
            matriz = self.controleMatriz.retornarMatriz(cS1, nP1, cS2, nP2)
            if matriz:
                con.excluirDadosTabela(
                    'matriz_sod', 'nome_perfil1', nP1, 'nome_perfil2', nP2)
                msg = self.controleMatriz.excluirMatriz(indice)
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.listarMatriz()
        else:
            msg = self.controleMatriz.excluirMatriz(indice)
            self.label_msg.setText(msg)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def listarUsuarios(self):
        contLinhas = 0
        self.tableWidget_usuarios.clearContents()
        self.tableWidget_usuarios.setRowCount(
            len(self.controleUsuario.listaUsuarios))
        for usuario in self.controleUsuario.listaUsuarios:
            self.tableWidget_usuarios.setItem(
                contLinhas, 0, QTableWidgetItem(usuario.cpf))
            self.tableWidget_usuarios.setItem(
                contLinhas, 1, QTableWidgetItem(usuario.nome))
            self.tableWidget_usuarios.setItem(
                contLinhas, 2, QTableWidgetItem(usuario.senha))
            self.tableWidget_usuarios.setItem(
                contLinhas, 3, QTableWidgetItem(usuario.nivelAcesso))
            contLinhas += 1

    def salvarUsuario(self):
        usuario = Usuario()
        usuario.cpf = self.lineEdit_cpfUsuario.text()
        usuario.nome = self.lineEdit_nomeUsuario.text()
        usuario.senha = self.lineEdit_senhaUsuario.text()
        usuario.nivelAcesso = str(self.spinBox_nAcessoUsuario.value())
        if len(usuario.erroValidacao) != 0:
            self.label_msg.setText(usuario.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            if self.controleUsuario.verificarUsuario(usuario.cpf):
                usuario.erroValidacao = f'Usuario {usuario.cpf} já está cadastrado.'
            if len(usuario.erroValidacao) != 0:
                self.label_msg.setText(usuario.erroValidacao)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                campos = ['cpf', 'nome', 'senha', 'nivel_acesso']
                valores = [usuario.cpf, usuario.nome,
                           usuario.senha, usuario.nivelAcesso]
                con.inserirDadosTabela(
                    'usuario', campos, valores, 'cpf', usuario.cpf)
                msg = self.controleUsuario.salvarUsuario(usuario)
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.listarUsuarios()

    def limparUsuario(self):
        self.lineEdit_cpfUsuario.clear()
        self.lineEdit_nomeUsuario.clear()
        self.lineEdit_senhaUsuario.clear()
        self.spinBox_nAcessoUsuario.setValue(0)

    def consultarUsuario(self):
        indice = self.tableWidget_usuarios.currentRow()
        if indice != -1:
            usuarios = con.selecionarCampoTabela('usuario', 'cpf')
            cpf = usuarios[indice][0]
            usuario = con.selecionarDadosTabela('usuario', 'cpf', cpf)
            self.label_consultarCpfUsuario.setText(usuario[0][1])
            self.label_consultarNomeUsuario.setText(usuario[0][2])
            self.label_consultarSenhaUsuario.setText(usuario[0][3])
            self.label_consultarNAcessoUsuario.setText(usuario[0][4])
            self.tabWidget_usuarios.setCurrentIndex(2)
        else:
            self.label_msg.setText('Usuário não selecionado.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def voltarListaUsuarios(self):
        self.label_consultarCpfUsuario.clear()
        self.label_consultarNomeUsuario.clear()
        self.label_consultarSenhaUsuario.clear()
        self.label_consultarNAcessoUsuario.clear()
        self.tabWidget_usuarios.setCurrentIndex(1)

    def editarUsuario(self):
        indice = self.tableWidget_usuarios.currentRow()
        if indice != -1:
            usuarios = con.selecionarCampoTabela('usuario', 'cpf')
            cpf = usuarios[indice][0]
            self.numeroId = cpf
            usuario = con.selecionarDadosTabela('usuario', 'cpf', cpf)
            self.label_editarCpfUsuario.setText(usuario[0][1])
            self.label_editarNomeUsuario.setText(usuario[0][2])
            self.tabWidget_usuarios.setCurrentIndex(3)
        else:
            self.label_msg.setText('Usuário não selecionado.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def atualizarUsuario(self):
        cpf = self.numeroId
        if cpf != None and len(cpf) != 0:
            usuario = self.controleUsuario.retornarUsuario(cpf)
            if usuario:
                usuario.senha = self.lineEdit_editarSenhaUsuario.text()
                usuario.nivelAcesso = str(
                    self.spinBox_editarNAcessoUsuario.value())
                if len(usuario.erroValidacao) != 0:
                    self.label_msg.setText(usuario.erroValidacao)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                    usuario.erroValidacao = ''
                else:
                    campos = ['senha', 'nivel_acesso']
                    valores = [usuario.senha, usuario.nivelAcesso]
                    con.atualizarDadosTabela(
                        'usuario', 'cpf', usuario.cpf, campos, valores)
                    msg = 'Usuario atualizado com sucesso!'
                    self.label_msg.setText(msg)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corSucesso)
                    self.label_editarCpfUsuario.clear()
                    self.label_editarNomeUsuario.clear()
                    self.lineEdit_editarSenhaUsuario.clear()
                    self.spinBox_editarNAcessoUsuario.setValue(0)
                    self.numeroId = ''
                    self.tabWidget_usuarios.setCurrentIndex(1)
                    self.listarUsuarios()

    def excluirUsuario(self):
        indice = self.tableWidget_usuarios.currentRow()
        if indice != -1:
            usuarios = con.selecionarCampoTabela('usuario', 'cpf')
            cpf = usuarios[indice][0]
            usuario = con.selecionarDadosTabela('usuario', 'cpf', cpf)
            con.excluirDadosTabela('usuario', 'cpf', cpf)
            msg = self.controleUsuario.excluirUsuario(indice)
            self.label_msg.setText(msg)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corSucesso)
            self.listarUsuarios()
        else:
            msg = self.controleUsuario.excluirUsuario(indice)
            self.label_msg.setText(msg)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def listarPUsuarios(self):
        contLinhas = 0
        self.tableWidget_pUsuarios.clearContents()
        self.tableWidget_pUsuarios.setRowCount(
            len(self.controlePUsuario.listaPUsuarios))
        for pUsuario in self.controlePUsuario.listaPUsuarios:
            self.tableWidget_pUsuarios.setItem(
                contLinhas, 0, QTableWidgetItem(pUsuario.cpf))
            self.tableWidget_pUsuarios.setItem(
                contLinhas, 1, QTableWidgetItem(pUsuario.codSistema))
            self.tableWidget_pUsuarios.setItem(
                contLinhas, 2, QTableWidgetItem(pUsuario.nomePAcesso))
            contLinhas += 1

    def verificarPUsuarioMatriz(self, cpf, codSistema, nomePAcesso):
        valida = False
        if self.controlePUsuario.verificarPUsuario(cpf):
            if self.controlePUsuario.retornarPUsuario(cpf, codSistema, nomePAcesso):
                valida = 1
            else:
                pUsuarios = self.controlePUsuario.retornarPUsuarios(cpf)
                if pUsuarios:
                    matriz = self.controleMatriz.listaMatriz
                    if matriz:
                        for ma in matriz:
                            for pu in pUsuarios:
                                if ((pu.codSistema == ma.codSistema1 and pu.nomePAcesso == ma.nomePerfil1) and (codSistema == ma.codSistema2 and nomePAcesso == ma.nomePerfil2)) or ((codSistema == ma.codSistema1 and nomePAcesso == ma.nomePerfil1) and (pu.codSistema == ma.codSistema2 and pu.nomePAcesso == ma.nomePerfil2)):
                                    valida = 2
        return valida

    def salvarPUsuario(self):
        pUsuario = PerfilUsuario()
        pUsuario.cpf = self.lineEdit_cpfPUsuario.text()
        if len(pUsuario.erroValidacao) != 0:
            self.label_msg.setText(pUsuario.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            if not self.controleUsuario.verificarUsuario(pUsuario.cpf):
                pUsuario.erroValidacao = f'Usuário {pUsuario.cpf} não está cadastrado.'
            nomeSistema = self.comboBox_sistemasPUsuario.currentText()
            if len(nomeSistema) == 0 or 'Selecione' in nomeSistema:
                pUsuario.erroValidacao = f'Selecione o sistema.'
            pAcesso = self.comboBox_pAcessosPUsuario.currentText()
            if len(pAcesso) == 0 or 'Selecione' in pAcesso:
                pUsuario.erroValidacao = f'Selecione o perfil de acesso.'
            if len(pUsuario.erroValidacao) != 0:
                self.label_msg.setText(pUsuario.erroValidacao)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                sistema = con.selecionarCampoTabela(
                    'sistema', 'codigo', 'nome', nomeSistema)
                pUsuario.codSistema = sistema[0][0]
                pUsuario.nomePAcesso = pAcesso
                if len(pUsuario.erroValidacao) != 0:
                    self.label_msg.setText(pUsuario.erroValidacao)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                valida = self.verificarPUsuarioMatriz(
                    pUsuario.cpf, pUsuario.codSistema, pUsuario.nomePAcesso)
                if valida:
                    if valida == 1:
                        msg = 'Perfil de usuário já está cadastrado!'
                    elif valida == 2:
                        msg = 'Perfil de usuário em conflito com perfil anterior!'
                    else:
                        msg = 'Não é possível cadastrar perfil.'
                    self.label_msg.setText(msg)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                else:
                    campos = ['cpf', 'cod_sistema', 'nome_perfil']
                    valores = [pUsuario.cpf,
                               pUsuario.codSistema, pUsuario.nomePAcesso]
                    con.adicionarDadosTabela('perfil_usuario', campos, valores)
                    msg = self.controlePUsuario.salvarPUsuario(pUsuario)
                    self.label_msg.setText(msg)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corSucesso)
                    self.listarPUsuarios()

    def limparPUsuario(self):
        self.lineEdit_cpfPUsuario.clear()
        self.comboBox_sistemasPUsuario.setCurrentIndex(0)
        self.comboBox_pAcessosPUsuario.setCurrentIndex(0)

    def consultarPUsuario(self):
        indice = self.tableWidget_pUsuarios.currentRow()
        if indice != -1:
            pUsuarios = con.selecionarCampoTabela('perfil_usuario', 'cpf')
            cpf = pUsuarios[indice][0]
            self.numeroId = cpf
            pUsuario = con.selecionarDadosTabela('perfil_usuario', 'cpf', cpf)
            self.label_consultarCpfPUsuario.setText(pUsuario[0][1])
            self.label_consultarSistemaPUsuario.setText(pUsuario[0][2])
            self.label_consultarPAcessoPUsuario.setText(pUsuario[0][3])
            self.tabWidget_pUsuarios.setCurrentIndex(2)
        else:
            self.label_msg.setText('Perfil de usuário não selecionado.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def voltarListaPUsuarios(self):
        self.label_consultarCpfPUsuario.clear()
        self.label_consultarSistemaPUsuario.clear()
        self.label_consultarPAcessoPUsuario.clear()
        self.numeroId = ''
        self.tabWidget_pUsuarios.setCurrentIndex(1)

    def excluirPUsuario(self):
        indice = self.tableWidget_pUsuarios.currentRow()
        if indice != -1:
            pUsuarios = con.selecionarCampoTabela('perfil_usuario', 'cpf')
            cpf = pUsuarios[indice][0]
            pUsuario = con.selecionarDadosTabela('perfil_usuario', 'cpf', cpf)
            con.excluirDadosTabela('perfil_usuario', 'cpf', cpf)
            msg = self.controlePUsuario.excluirPUsuario(indice)
            self.label_msg.setText(msg)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corSucesso)
            self.listarPUsuarios()
        else:
            msg = self.controlePUsuario.excluirPUsuario(indice)
            self.label_msg.setText(msg)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
