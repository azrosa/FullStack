import data.conexao as con
from datetime import datetime as dt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from model.agencia import Agencia
from model.cliente import Cliente
from model.conta import Conta
from model.transacao import Transacao
from view.telaEscriturario import Ui_MainWindow
from controller.agenciaControl import AgenciaControl
from controller.clienteControl import ClienteControl
from controller.contaControl import ContaControl
from controller.transacaoControl import TransacaoControl


class GUIEscriturario(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.numeroId = ''
        self.controleAgencia = AgenciaControl()
        self.controleCliente = ClienteControl()
        self.controleConta = ContaControl()
        self.controleTransacao = TransacaoControl()
        self.init_components()
        self.corSucesso = "background-color: rgb(209, 255, 209);"
        self.corErro = "background-color: rgb(250, 185, 185);"

    def init_components(self):
        self.label_logo.setPixmap(QPixmap('img\logoV.png'))
        self.pushButton_cliente.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_clientes))
        self.pushButton_conta.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_contas))
        self.pushButton_transacoes.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_transacoes))

        self.pushButton_salvarCliente.clicked.connect(self.salvarCliente)
        self.pushButton_limparCliente.clicked.connect(self.limparCliente)
        self.pushButton_editarCliente.clicked.connect(self.editarCliente)
        self.pushButton_consultarCliente.clicked.connect(self.consultarCliente)
        self.pushButton_excluirCliente.clicked.connect(self.excluirCliente)
        self.pushButton_atualizarCliente.clicked.connect(self.atualizarCliente)
        self.pushButton_voltarListaClientes.clicked.connect(
            self.voltarListaClientes)

        self.pushButton_salvarConta.clicked.connect(self.salvarConta)
        self.pushButton_limparConta.clicked.connect(self.limparConta)
        self.pushButton_editarConta.clicked.connect(self.editarConta)
        self.pushButton_consultarConta.clicked.connect(self.consultarConta)
        self.pushButton_excluirConta.clicked.connect(self.excluirConta)
        self.pushButton_atualizarConta.clicked.connect(self.atualizarConta)
        self.pushButton_voltarListaContas.clicked.connect(
            self.voltarListaContas)

        self.pushButton_listarTransacoes.clicked.connect(self.listarTransacoes)
        self.pushButton_excluirTransacao.clicked.connect(
            self.excluirTransacoes)
        self.dateEdit_transacaoDataInicial.setDate(dt.today())
        self.dateEdit_transacaoDataFinal.setDate(dt.today())

        self.frame_msgBar.hide()
        self.pushButton_fecharMsg.clicked.connect(
            lambda: self.frame_msgBar.hide())
        self.initBD()

    def initBD(self):
        agencias = con.selecionarDadosTabela('agencia')
        lsAgencias = ['--- Selecione ---']
        if agencias:
            for a in agencias:
                agencia = Agencia(a[1], a[2])
                self.controleAgencia.salvarAgencia(agencia)
            for ag in self.controleAgencia.listaAgencias:
                lsAgencias.append(ag.cidade)
            self.comboBox_agenciasConta.addItems(lsAgencias)
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
        tipos = ['--- Selecione ---']
        listaTiposConta = con.selecionarDadosTabela('tipo_conta')
        for t in listaTiposConta:
            tipos.append(t[1])
        self.comboBox_tiposConta.addItems(tipos)
        self.listarClientes()
        self.listarContas()

    def listarClientes(self):
        contLinhas = 0
        self.tableWidget_clientes.clearContents()
        self.tableWidget_clientes.setRowCount(
            len(self.controleCliente.listaClientes))
        for cliente in self.controleCliente.listaClientes:
            self.tableWidget_clientes.setItem(
                contLinhas, 0, QTableWidgetItem(cliente.nome))
            self.tableWidget_clientes.setItem(
                contLinhas, 1, QTableWidgetItem(cliente.cpf))
            self.tableWidget_clientes.setItem(
                contLinhas, 2, QTableWidgetItem(cliente.endereco))
            self.tableWidget_clientes.setItem(
                contLinhas, 3, QTableWidgetItem(cliente.contato))
            contLinhas += 1

    def salvarCliente(self):
        cliente = Cliente()
        cliente.cpf = self.lineEdit_cpfCliente.text()
        cliente.nome = self.lineEdit_nomeCliente.text()
        cliente.endereco = self.lineEdit_enderecoCliente.text()
        cliente.contato = self.lineEdit_contatoCliente.text()
        if len(cliente.erroValidacao) != 0:
            self.label_msg.setText(cliente.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            if self.controleCliente.verificarCliente(cliente.cpf):
                cliente.erroValidacao = f'Cliente {cliente.cpf} já está cadastrado.'
            if len(cliente.erroValidacao) != 0:
                self.label_msg.setText(cliente.erroValidacao)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                campos = ['cpf', 'nome', 'endereco', 'contato']
                valores = [cliente.cpf, cliente.nome,
                           cliente.endereco, cliente.contato]
                con.inserirDadosTabela(
                    'cliente', campos, valores, 'cpf', cliente.cpf)
                msg = self.controleCliente.salvarCliente(cliente)
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.listarClientes()

    def limparCliente(self):
        self.lineEdit_cpfCliente.clear()
        self.lineEdit_nomeCliente.clear()
        self.lineEdit_enderecoCliente.clear()
        self.lineEdit_contatoCliente.clear()

    def consultarCliente(self):
        indice = self.tableWidget_clientes.currentRow()
        if indice != -1:
            clientes = con.selecionarCampoTabela('cliente', 'cpf')
            cpf = clientes[indice][0]
            self.numeroId = cpf
            cliente = con.selecionarDadosTabela('cliente', 'cpf', cpf)
            self.label_consultarCPFCliente.setText(cliente[0][1])
            self.label_consultarNomeCliente.setText(cliente[0][2])
            self.label_consultarEnderecoCliente.setText(cliente[0][3])
            self.label_consultarContatoCliente.setText(cliente[0][4])
            self.tabWidget_clientes.setCurrentIndex(2)
        else:
            self.label_msg.setText('Cliente não selecionado.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def voltarListaClientes(self):
        self.label_consultarCPFCliente.clear()
        self.label_consultarNomeCliente.clear()
        self.label_consultarEnderecoCliente.clear()
        self.label_consultarContatoCliente.clear()
        self.numeroId = ''
        self.tabWidget_clientes.setCurrentIndex(1)

    def editarCliente(self):
        indice = self.tableWidget_clientes.currentRow()
        if indice != -1:
            clientes = con.selecionarCampoTabela('cliente', 'cpf')
            cpf = clientes[indice][0]
            self.numeroId = cpf
            cliente = con.selecionarDadosTabela('cliente', 'cpf', cpf)
            self.label_editarCPFCliente.setText(cliente[0][1])
            self.lineEdit_editarNomeCliente.setText(cliente[0][2])
            self.lineEdit_editarEnderecoCliente.setText(cliente[0][3])
            self.lineEdit_editarContatoCliente.setText(cliente[0][4])
            self.tabWidget_clientes.setCurrentIndex(3)
        else:
            self.label_msg.setText('Cliente não selecionado.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def atualizarCliente(self):
        cpf = self.numeroId
        if cpf != None and len(cpf) != 0:
            cliente = self.controleCliente.retornarCliente(cpf)
            if cliente:
                cliente.nome = self.lineEdit_editarNomeCliente.text()
                cliente.endereco = self.lineEdit_editarEnderecoCliente.text()
                cliente.contato = self.lineEdit_editarContatoCliente.text()
                if len(cliente.erroValidacao) != 0:
                    self.label_msg.setText(cliente.erroValidacao)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                    cliente.erroValidacao = ''
                else:
                    campos = ['nome', 'endereco', 'contato']
                    valores = [cliente.nome, cliente.endereco, cliente.contato]
                    con.atualizarDadosTabela(
                        'cliente', 'cpf', cliente.cpf, campos, valores)
                    msg = 'Cliente atualizado com sucesso!'
                    self.label_msg.setText(msg)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corSucesso)
                    self.label_editarCPFCliente.clear()
                    self.lineEdit_editarNomeCliente.clear()
                    self.lineEdit_editarEnderecoCliente.clear()
                    self.lineEdit_editarContatoCliente.clear()
                    self.numeroId = ''
                    self.tabWidget_clientes.setCurrentIndex(1)
                    self.listarClientes()

    def excluirCliente(self):
        indice = self.tableWidget_clientes.currentRow()
        if indice != -1:
            clientes = con.selecionarCampoTabela('cliente', 'cpf')
            cpf = clientes[indice][0]
            contas = con.selecionarCampoTabela('conta', 'numero',  'cpf', cpf)
            if contas:
                self.label_msg.setText('Cliente possui conta(s) vinculada(s).')
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                con.excluirDadosTabela('cliente', 'cpf', cpf)
                msg = self.controleCliente.excluirCliente(indice)
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.listarClientes()
        else:
            msg = self.controleCliente.excluirCliente(indice)
            self.label_msg.setText(msg)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def listarContas(self):
        contLinhas = 0
        self.tableWidget_contas.clearContents()
        self.tableWidget_contas.setRowCount(
            len(self.controleConta.listaContas))
        for conta in self.controleConta.listaContas:
            self.tableWidget_contas.setItem(
                contLinhas, 0, QTableWidgetItem(conta.numero))
            self.tableWidget_contas.setItem(
                contLinhas, 1, QTableWidgetItem(conta.tipoConta))
            self.tableWidget_contas.setItem(
                contLinhas, 2, QTableWidgetItem(conta.cpf))
            self.tableWidget_contas.setItem(
                contLinhas, 3, QTableWidgetItem(conta.numAgencia))
            self.tableWidget_contas.setItem(
                contLinhas, 4, QTableWidgetItem(f'{conta.saldo:10,.2f}'))
            self.tableWidget_contas.setItem(
                contLinhas, 5, QTableWidgetItem(f'{conta.limite:10,.2f}'))
            self.tableWidget_contas.setItem(contLinhas, 6, QTableWidgetItem(
                conta.dataAbertura.strftime('%d/%m/%Y')))
            contLinhas += 1

    def salvarConta(self):
        conta = Conta()
        conta.cpf = self.lineEdit_cpfConta.text()
        conta.saldo = self.doubleSpinBox_saldoConta.value()
        conta.limite = self.doubleSpinBox_limiteConta.value()
        conta.dataAbertura = dt.today()
        if len(conta.erroValidacao) != 0:
            self.label_msg.setText(conta.erroValidacao)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)
        else:
            tipoConta = self.comboBox_tiposConta.currentText()
            cidadeAgencia = self.comboBox_agenciasConta.currentText()
            if not self.controleCliente.verificarCliente(conta.cpf):
                conta.erroValidacao = f'Cliente {conta.cpf} não está cadastrado.'
            if len(tipoConta) == 0 or 'Selecione' in tipoConta:
                conta.erroValidacao = f'Selecione o Tipo de Conta.'
            if len(cidadeAgencia) == 0 or 'Selecione' in cidadeAgencia:
                conta.erroValidacao = f'Selecione a Agência.'
            if len(conta.erroValidacao) != 0:
                self.label_msg.setText(conta.erroValidacao)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                conta.tipoConta = tipoConta
                agencia = con.selecionarCampoTabela(
                    'agencia', 'numero', 'cidade', cidadeAgencia)
                conta.numAgencia = agencia[0][0]
                conta.numero = self.controleConta.gerarNumConta()
                if len(conta.erroValidacao) != 0:
                    self.label_msg.setText(conta.erroValidacao)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                else:
                    self.label_numConta.setText(conta.numero)
                    self.label_dataAberturaConta.setText(
                        conta.dataAbertura.strftime('%d/%m/%Y'))
                    campos = ['numero', 'tipo', 'cpf', 'num_agencia',
                              'saldo', 'limite', 'data_abertura']
                    valores = [conta.numero, conta.tipoConta, conta.cpf,
                               conta.numAgencia, conta.saldo, conta.limite, conta.dataAbertura]
                    con.inserirDadosTabela(
                        'conta', campos, valores, 'numero', conta.numero)
                    msg = self.controleConta.salvarConta(conta)
                    self.label_msg.setText(msg)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corSucesso)
                    self.listarContas()

    def limparConta(self):
        self.lineEdit_cpfConta.clear()
        self.label_numConta.clear()
        self.label_dataAberturaConta.clear()
        self.doubleSpinBox_saldoConta.setValue(0)
        self.doubleSpinBox_limiteConta.setValue(0)
        self.comboBox_agenciasConta.setCurrentIndex(0)
        self.comboBox_tiposConta.setCurrentIndex(0)

    def consultarConta(self):
        indice = self.tableWidget_contas.currentRow()
        if indice != -1:
            contas = con.selecionarCampoTabela('conta', 'numero')
            numero = contas[indice][0]
            self.numeroId = numero
            conta = con.selecionarDadosTabela('conta', 'numero', numero)
            self.label_consultarNumConta.setText(conta[0][1])
            self.label_consultarTipoConta.setText(conta[0][2])
            self.label_consultarCPFConta.setText(conta[0][3])
            self.label_consultarAgenciaConta.setText(conta[0][4])
            self.label_consultarSaldoConta.setText(f'R${conta[0][5]:10,.2f}')
            self.label_consultarLimiteConta.setText(f'R${conta[0][6]:10,.2f}')
            self.label_consultarDataAberturaConta.setText(
                conta[0][7].strftime('%d/%m/%Y'))
            self.tabWidget_contas.setCurrentIndex(2)
        else:
            self.label_msg.setText('Conta não selecionada.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def voltarListaContas(self):
        self.label_consultarNumConta.clear()
        self.label_consultarTipoConta.clear()
        self.label_consultarCPFConta.clear()
        self.label_consultarAgenciaConta.clear()
        self.label_consultarSaldoConta.clear()
        self.label_consultarLimiteConta.clear()
        self.label_consultarDataAberturaConta.clear()
        self.tabWidget_contas.setCurrentIndex(1)

    def editarConta(self):
        indice = self.tableWidget_contas.currentRow()
        if indice != -1:
            contas = con.selecionarCampoTabela('conta', 'numero')
            numero = contas[indice][0]
            self.numeroId = numero
            conta = con.selecionarDadosTabela('conta', 'numero', numero)
            self.label_editarNumConta.setText(conta[0][1])
            self.label_editarTipoConta.setText(conta[0][2])
            self.label_editarCPFConta.setText(conta[0][3])
            self.label_editarAgenciaConta.setText(conta[0][4])
            self.doubleSpinBox_editarSaldoConta.setValue(conta[0][5])
            self.doubleSpinBox_editarLimiteConta.setValue(conta[0][6])
            self.label_editarDataAberturaConta.setText(
                conta[0][7].strftime('%d/%m/%Y'))
            self.tabWidget_contas.setCurrentIndex(3)
        else:
            self.label_msg.setText('Conta não selecionada.')
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corErro)

    def atualizarConta(self):
        numero = self.numeroId
        if numero != None and len(numero) != 0:
            conta = self.controleConta.retornarConta(numero)
            if conta:
                conta.saldo = self.doubleSpinBox_editarSaldoConta.value()
                conta.limite = self.doubleSpinBox_editarLimiteConta.value()
                if len(conta.erroValidacao) != 0:
                    self.label_msg.setText(conta.erroValidacao)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corErro)
                    conta.erroValidacao = ''
                else:
                    campos = ['saldo', 'limite']
                    valores = [conta.saldo, conta.limite]
                    con.atualizarDadosTabela(
                        'conta', 'numero', conta.numero, campos, valores)
                    msg = 'Conta atualizada com sucesso!'
                    self.label_msg.setText(msg)
                    self.frame_msgBar.show()
                    self.label_msg.setStyleSheet(self.corSucesso)
                    self.label_editarNumConta.clear()
                    self.label_editarTipoConta.clear()
                    self.label_editarCPFConta.clear()
                    self.label_editarAgenciaConta.clear()
                    self.doubleSpinBox_editarSaldoConta.setValue(0)
                    self.doubleSpinBox_editarLimiteConta.setValue(0)
                    self.label_editarDataAberturaConta.clear()
                    self.numeroId = ''
                    self.tabWidget_contas.setCurrentIndex(1)
                    self.listarContas()

    def excluirConta(self):
        indice = self.tableWidget_contas.currentRow()
        if indice != -1:
            contas = con.selecionarCampoTabela('conta', 'numero')
            numero = contas[indice][0]
            transacoes = con.selecionarDadosTabela(
                'transacao', 'num_conta', numero)
            if transacoes:
                self.label_msg.setText('Conta possui transações vinculadas.')
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
            else:
                con.excluirDadosTabela('conta', 'numero', numero)
                msg = self.controleConta.excluirConta(indice)
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.listarContas()

    def listarTransacoes(self):
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
        else:
            contLinhas = 0
            self.tableWidget_transacoes.clearContents()
            self.tableWidget_transacoes.setRowCount(
                len(self.controleTransacao.listaTransacoes))
            for transacao in self.controleTransacao.listaTransacoes:
                self.tableWidget_transacoes.setItem(
                    contLinhas, 0, QTableWidgetItem(transacao.numConta))
                self.tableWidget_transacoes.setItem(
                    contLinhas, 1, QTableWidgetItem(transacao.descricao))
                self.tableWidget_transacoes.setItem(
                    contLinhas, 2, QTableWidgetItem(f'R${transacao.valor:10,.2f}'))
                self.tableWidget_transacoes.setItem(contLinhas, 3, QTableWidgetItem(
                    transacao.data.strftime('%d/%m/%Y')))
                contLinhas += 1
        self.tabWidget_transacoes.setCurrentIndex(1)
        self.lineEdit_transacaoNumConta.clear()
        self.dateEdit_transacaoDataInicial.setDate(dt.today())
        self.dateEdit_transacaoDataFinal.setDate(dt.today())

    def excluirTransacoes(self):
        indice = self.tableWidget_transacoes.currentRow()
        numConta = self.numeroId
        if self.controleConta.verificarConta(numConta):
            con.excluirDadosTabela('transacao', 'num_conta', numConta)
            msg = self.controleTransacao.excluirTransacoes(numConta)
            self.label_msg.setText(msg)
            self.frame_msgBar.show()
            self.label_msg.setStyleSheet(self.corSucesso)
            self.tableWidget_transacoes.clearContents()
            self.numeroId = ''
            self.tabWidget_transacoes.setCurrentIndex(0)
        else:
            if indice != -1:
                transacoes = con.selecionarCampoTabela('transacao', 'id')
                id = transacoes[indice][0]
                con.excluirDadosTabela('transacao', 'id', id)
                msg = self.controleTransacao.excluirTransacao(indice)
                self.label_msg.setText(msg)
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corSucesso)
                self.tableWidget_transacoes.clearContents()
                self.numeroId = ''
                self.tabWidget_transacoes.setCurrentIndex(0)
            else:
                self.label_msg.setText('Nenhuma transação selecionada.')
                self.frame_msgBar.show()
                self.label_msg.setStyleSheet(self.corErro)
