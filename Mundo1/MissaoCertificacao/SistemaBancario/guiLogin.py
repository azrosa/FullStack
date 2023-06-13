import data.conexao as con
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from model.usuario import Usuario
from view.telaLogin import Ui_MainWindow
from controller.usuarioControl import UsuarioControl
from guiAdministrador import GUIAdministrador
from guiGerente import GUIGerente
from guiEscriturario import GUIEscriturario
from guiCaixa import GUICaixa


class GUILogin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.numeroId = ''
        self.controleUsuario = UsuarioControl()
        self.init_components()
        self.corSucesso = "background-color: rgb(209, 255, 209);"
        self.corErro = "background-color: rgb(250, 185, 185);"

    def init_components(self):
        self.label_logo.setPixmap(QPixmap('img\logo.png'))
        self.pushButton_entrarLogin.clicked.connect(self.entrarLogin)
        self.frame_msgBar.hide()
        self.pushButton_fecharMsg.clicked.connect(
            lambda: self.frame_msgBar.hide())
        self.initBD()

    def initBD(self):
        usuarios = con.selecionarDadosTabela('usuario')
        if usuarios:
            for u in usuarios:
                usuario = Usuario(u[1], u[2], u[3], u[4])
                self.controleUsuario.salvarUsuario(usuario)

    def entrarLogin(self):
        usuario = Usuario()
        usuario.nome = self.lineEdit_nomeLogin.text()
        usuario.senha = self.lineEdit_senhaLogin.text()
        if len(usuario.erroValidacao) != 0:
            self.label_msg.setText(usuario.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            usuario = self.controleUsuario.retornarUsuario(nome=usuario.nome)
            if usuario:
                if usuario.nivelAcesso == '4':
                    gui = GUIAdministrador()
                elif usuario.nivelAcesso == '3':
                    gui = GUIGerente()
                elif usuario.nivelAcesso == '2':
                    gui = GUIEscriturario()
                elif usuario.nivelAcesso == '1':
                    gui = GUICaixa()
                self.close()
                return gui
            else:
                self.label_msg.setText('Usuario/senha inválido.')
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
                return False
