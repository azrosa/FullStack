import data.conexao as con
from datetime import datetime as dt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from model.cliente import Cliente
from model.conta import Conta
from model.transacao import Transacao
from view.telaCaixa import Ui_MainWindow
from controller.clienteControl import ClienteControl
from controller.contaControl import ContaControl
from controller.transacaoControl import TransacaoControl


class GUICaixa(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.numeroId = ''
        self.controleCliente = ClienteControl()
        self.controleConta = ContaControl()
        self.controleTransacao = TransacaoControl()
        self.corSucesso = "background-color: rgb(209, 255, 209);"
        self.corErro = "background-color: rgb(250, 185, 185);"
        self.init_components()

    def init_components(self):
        self.label_logo.setPixmap(QPixmap('img\logoV.png'))
        self.pushButton_cliente.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_cliente))
        self.pushButton_conta.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_conta))
        self.pushButton_deposito.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_depositos))
        self.pushButton_saque.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_saques))
        self.pushButton_transacoes.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_transacoes))

        self.pushButton_consultarCliente.clicked.connect(self.consultarCliente)
        self.pushButton_voltarConsultaCliente.clicked.connect(
            self.voltarConsultaCliente)

        self.pushButton_consultarConta.clicked.connect(self.consultarConta)
        self.pushButton_voltarConsultaConta.clicked.connect(
            self.voltarConsultaConta)

        self.pushButton_salvarDeposito.clicked.connect(self.salvarDeposito)
        self.pushButton_voltarDepositar.clicked.connect(self.voltarDepositar)

        self.pushButton_salvarSaque.clicked.connect(self.salvarSaque)
        self.pushButton_voltarSacar.clicked.connect(self.voltarSacar)

        self.pushButton_listarTransacoes.clicked.connect(
            self.listarTransacoesConta)
        self.dateEdit_transacaoDataInicial.setDate(dt.today())
        self.dateEdit_transacaoDataFinal.setDate(dt.today())

        self.frame_msgBar.hide()
        self.pushButton_fecharMsg.clicked.connect(
            lambda: self.frame_msgBar.hide())
        self.initBD()

    def initBD(self):
        clientes = con.selecionarDadosTabela('cliente')
        if clientes:
            for c in clientes:
                cliente = Cliente(c[1], c[2], c[3], c[4])
                self.controleCliente.salvarCliente(cliente)
        contas = con.selecionarDadosTabela('conta')
        if contas:
            for co in contas:
                conta = Conta(co[1], co[2], co[3], co[4],
                              co[5], co[6], co[7])
                self.controleConta.salvarConta(conta)
        transacoes = con.selecionarDadosTabela('transacao')
        if transacoes:
            for t in transacoes:
                transacao = Transacao(t[1], t[2], t[3], t[4])
                self.controleTransacao.salvarTransacao(transacao)

    def consultarCliente(self):
        validarCliente = Cliente()
        validarCliente.cpf = self.lineEdit_consultaCPFCliente.text()
        if len(validarCliente.erroValidacao) != 0:
            self.label_msg.setText(validarCliente.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            validar = self.controleCliente.verificarCliente(validarCliente.cpf)
            if not validar:
                self.label_msg.setText('Cliente não existe.')
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                cliente = con.selecionarDadosTabela(
                    'cliente', 'cpf', validarCliente.cpf)
                self.label_consultarCPFCliente.setText(cliente[0][1])
                self.label_consultarNomeCliente.setText(cliente[0][2])
                self.label_consultarEnderecoCliente.setText(cliente[0][3])
                self.label_consultarContatoCliente.setText(cliente[0][4])
                msg = 'Cliente verificado com sucesso!'
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.lineEdit_consultaCPFCliente.clear()
                self.tabWidget_cliente.setCurrentIndex(1)

    def voltarConsultaCliente(self):
        self.label_consultarCPFCliente.clear()
        self.label_consultarNomeCliente.clear()
        self.label_consultarEnderecoCliente.clear()
        self.label_consultarContatoCliente.clear()
        self.tabWidget_cliente.setCurrentIndex(0)

    def consultarConta(self):
        validarConta = Conta()
        validarConta.numero = self.lineEdit_consultaNumConta.text()
        if len(validarConta.erroValidacao) != 0:
            self.label_msg.setText(validarConta.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            validar = self.controleConta.verificarConta(validarConta.numero)
            if not validar:
                self.label_msg.setText('Conta não existe.')
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                conta = con.selecionarDadosTabela(
                    'conta', 'numero', validarConta.numero)
                self.label_consultarNumConta.setText(conta[0][1])
                self.label_consultarTipoConta.setText(conta[0][2])
                self.label_consultarCPFConta.setText(conta[0][3])
                self.label_consultarAgenciaConta.setText(conta[0][4])
                self.label_consultarSaldoConta.setText(
                    f'R${conta[0][5]:10,.2f}')
                self.label_consultarLimiteConta.setText(
                    f'R${conta[0][6]:10,.2f}')
                self.label_consultarDataAberturaConta.setText(
                    conta[0][7].strftime('%d/%m/%Y'))
                msg = 'Conta verificada com sucesso!'
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.lineEdit_consultaNumConta.clear()
                self.tabWidget_conta.setCurrentIndex(1)

    def voltarConsultaConta(self):
        self.label_consultarNumConta.clear()
        self.label_consultarTipoConta.clear()
        self.label_consultarCPFConta.clear()
        self.label_consultarAgenciaConta.clear()
        self.label_consultarSaldoConta.clear()
        self.label_consultarLimiteConta.clear()
        self.label_consultarDataAberturaConta.clear()
        self.tabWidget_conta.setCurrentIndex(0)

    def salvarDeposito(self):
        transacao = Transacao()
        transacao.numConta = self.lineEdit_depositoNumConta.text()
        transacao.descricao = ' + ' + self.lineEdit_depositoDescricao.text()
        transacao.valor = self.doubleSpinBox_depositoValor.value()
        transacao.data = dt.today()
        if len(transacao.erroValidacao) != 0:
            self.label_msg.setText(transacao.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            if not self.controleConta.verificarConta(transacao.numConta):
                transacao.erroValidacao = f'Conta {transacao.numConta} não existe.'
                self.label_msg.setText(transacao.erroValidacao)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                conta = self.controleConta.retornarConta(transacao.numConta)
                if conta:
                    depositou = conta.depositar(transacao.valor)
                    con.atualizarCampoTabela(
                        'conta', 'saldo', conta.saldo, 'numero', conta.numero)
                    campos = ['num_conta', 'descricao', 'valor', 'data']
                    valores = [transacao.numConta, transacao.descricao,
                               transacao.valor, transacao.data]
                    con.adicionarDadosTabela('transacao', campos, valores)
                    self.controleTransacao.salvarTransacao(transacao)
                    self.label_msg.setText(depositou)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corSucesso)
                    self.lineEdit_depositoNumConta.clear()
                    self.lineEdit_depositoDescricao.clear()
                    self.doubleSpinBox_depositoValor.setValue(0)
                    self.label_visualizarDepositoNumConta.setText(
                        transacao.numConta)
                    self.label_visualizarDepositoDescricao.setText(
                        transacao.descricao)
                    self.label_visualizarDepositoValor.setText(
                        f'R${transacao.valor:10,.2f}')
                    self.label_visualizarDepositoData.setText(
                        transacao.data.strftime('%d/%m/%Y'))
                    self.tabWidget_deposito.setCurrentIndex(1)

    def voltarDepositar(self):
        self.label_visualizarDepositoNumConta.clear()
        self.label_visualizarDepositoDescricao.clear()
        self.label_visualizarDepositoValor.clear()
        self.label_visualizarDepositoData.clear()
        self.tabWidget_deposito.setCurrentIndex(0)

    def salvarSaque(self):
        transacao = Transacao()
        transacao.numConta = self.lineEdit_saqueNumConta.text()
        transacao.descricao = ' - ' + self.lineEdit_saqueDescricao.text()
        transacao.valor = self.doubleSpinBox_saqueValor.value()
        transacao.data = dt.today()
        if len(transacao.erroValidacao) != 0:
            self.label_msg.setText(transacao.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            if not self.controleConta.verificarConta(transacao.numConta):
                transacao.erroValidacao = f'Conta {transacao.numConta} não existe.'
                self.label_msg.setText(transacao.erroValidacao)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                conta = self.controleConta.retornarConta(transacao.numConta)
                if conta:
                    sacou = conta.sacar(transacao.valor)
                    if not sacou:
                        msg = f"Não existe saldo suficiente na conta {conta.numero}"
                        self.label_msg.setText(msg)
                        self.frame_msgBar.show()
                        self.label_msg.setStyleSheet(self.corErro)
                    else:
                        con.atualizarCampoTabela(
                            'conta', 'saldo', conta.saldo, 'numero', conta.numero)
                        campos = ['num_conta', 'descricao', 'valor', 'data']
                        valores = [transacao.numConta, transacao.descricao,
                                   transacao.valor, transacao.data]
                        con.adicionarDadosTabela('transacao', campos, valores)
                        self.controleTransacao.salvarTransacao(transacao)
                        self.label_msg.setText(sacou)
                        self.frame_msgBar.show()
                        self.label_msg.setStyleSheet(self.corSucesso)
                        self.lineEdit_saqueNumConta.clear()
                        self.lineEdit_saqueDescricao.clear()
                        self.doubleSpinBox_saqueValor.setValue(0)
                        self.label_visualizarSaqueNumConta.setText(
                            transacao.numConta)
                        self.label_visualizarSaqueDescricao.setText(
                            transacao.descricao)
                        self.label_visualizarSaqueValor.setText(
                            f'R${transacao.valor:10,.2f}')
                        self.label_visualizarSaqueData.setText(
                            transacao.data.strftime('%d/%m/%Y'))
                        self.tabWidget_saque.setCurrentIndex(1)

    def voltarSacar(self):
        self.label_visualizarSaqueNumConta.clear()
        self.label_visualizarSaqueDescricao.clear()
        self.label_visualizarSaqueValor.clear()
        self.label_visualizarSaqueData.clear()
        self.tabWidget_saque.setCurrentIndex(0)

    def listarTransacoesConta(self):
        self.dateEdit_transacaoDataInicial.setDate(dt.today())
        self.dateEdit_transacaoDataFinal.setDate(dt.today())
        numConta = self.lineEdit_transacaoNumConta.text()
        self.numeroId = f'{numConta:0>11}'
        if numConta != None and len(numConta) != 0:
            transacao = Transacao()
            transacao.numConta = numConta
            dataInicial = self.dateEdit_transacaoDataInicial.date()
            dataFinal = self.dateEdit_transacaoDataFinal.date()
            if len(transacao.erroValidacao) != 0:
                self.label_msg.setText(transacao.erroValidacao)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                if not self.controleConta.verificarConta(transacao.numConta):
                    transacao.erroValidacao = f'Conta {transacao.numConta} não existe.'
                    self.label_msg.setText(transacao.erroValidacao)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                else:
                    contLinhas = 0
                    self.tableWidget_transacoes.clearContents()
                    self.tableWidget_transacoes.setRowCount(
                        len(self.controleTransacao.listaTransacoes))
                    if dataInicial == dataFinal:
                        for t in self.controleTransacao.listaTransacoes:
                            if t.numConta == transacao.numConta:
                                self.tableWidget_transacoes.setItem(
                                    contLinhas, 0, QTableWidgetItem(t.numConta))
                                self.tableWidget_transacoes.setItem(
                                    contLinhas, 1, QTableWidgetItem(t.descricao))
                                self.tableWidget_transacoes.setItem(
                                    contLinhas, 2, QTableWidgetItem(f'R${t.valor:10,.2f}'))
                                self.tableWidget_transacoes.setItem(contLinhas, 3, QTableWidgetItem(
                                    t.data.strftime('%d/%m/%Y')))
                                contLinhas += 1
                    else:
                        for t in self.controleTransacao.listaTransacoes:
                            if t.numConta == transacao.numConta and (dataInicial <= t.data <= dataFinal):
                                self.tableWidget_transacoes.setItem(
                                    contLinhas, 0, QTableWidgetItem(t.numConta))
                                self.tableWidget_transacoes.setItem(
                                    contLinhas, 1, QTableWidgetItem(t.descricao))
                                self.tableWidget_transacoes.setItem(
                                    contLinhas, 2, QTableWidgetItem(f'R${t.valor:10,.2f}'))
                                self.tableWidget_transacoes.setItem(contLinhas, 3, QTableWidgetItem(
                                    t.data.strftime('%d/%m/%Y')))
                                contLinhas += 1
                    self.tabWidget_transacoes.setCurrentIndex(1)
                    self.lineEdit_transacaoNumConta.clear()
                    self.dateEdit_transacaoDataInicial.setDate(dt.today())
                    self.dateEdit_transacaoDataFinal.setDate(dt.today())
        else:
            self.label_msg.setText('Número de conta inválido.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
