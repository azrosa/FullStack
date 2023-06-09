# Form implementation generated from reading ui file 'telaLogin.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 531)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_login = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_login.setGeometry(QtCore.QRect(0, 0, 411, 531))
        self.widget_login.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"    color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115, 128, 142, 255);\n"
"}")
        self.widget_login.setObjectName("widget_login")
        self.label = QtWidgets.QLabel(parent=self.widget_login)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("border-image: url(:/images/background.png);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_bordaLogin = QtWidgets.QLabel(parent=self.widget_login)
        self.label_bordaLogin.setGeometry(QtCore.QRect(0, 0, 381, 531))
        self.label_bordaLogin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;")
        self.label_bordaLogin.setText("")
        self.label_bordaLogin.setObjectName("label_bordaLogin")
        self.label_bgLogin = QtWidgets.QLabel(parent=self.widget_login)
        self.label_bgLogin.setGeometry(QtCore.QRect(-1, -1, 381, 531))
        self.label_bgLogin.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_bgLogin.setText("")
        self.label_bgLogin.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.label_bgLogin.setObjectName("label_bgLogin")
        self.label_titLogin = QtWidgets.QLabel(parent=self.widget_login)
        self.label_titLogin.setGeometry(QtCore.QRect(135, 115, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_titLogin.setFont(font)
        self.label_titLogin.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_titLogin.setObjectName("label_titLogin")
        self.lineEdit_nomeLogin = QtWidgets.QLineEdit(parent=self.widget_login)
        self.lineEdit_nomeLogin.setGeometry(QtCore.QRect(80, 185, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_nomeLogin.setFont(font)
        self.lineEdit_nomeLogin.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_nomeLogin.setObjectName("lineEdit_nomeLogin")
        self.lineEdit_senhaLogin = QtWidgets.QLineEdit(parent=self.widget_login)
        self.lineEdit_senhaLogin.setGeometry(QtCore.QRect(80, 250, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_senhaLogin.setFont(font)
        self.lineEdit_senhaLogin.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_senhaLogin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_senhaLogin.setObjectName("lineEdit_senhaLogin")
        self.pushButton_entrarLogin = QtWidgets.QPushButton(parent=self.widget_login)
        self.pushButton_entrarLogin.setGeometry(QtCore.QRect(80, 330, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_entrarLogin.setFont(font)
        self.pushButton_entrarLogin.setObjectName("pushButton_entrarLogin")
        self.frame_msgBar = QtWidgets.QFrame(parent=self.widget_login)
        self.frame_msgBar.setGeometry(QtCore.QRect(70, 400, 251, 44))
        self.frame_msgBar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_msgBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_msgBar.setObjectName("frame_msgBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_msgBar)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_msg = QtWidgets.QLabel(parent=self.frame_msgBar)
        self.label_msg.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_msg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_msg.setObjectName("label_msg")
        self.horizontalLayout_2.addWidget(self.label_msg)
        self.pushButton_fecharMsg = QtWidgets.QPushButton(parent=self.frame_msgBar)
        self.pushButton_fecharMsg.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pushButton_fecharMsg.setStyleSheet("QPushButton{\n"
"    border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: rgb(200, 200, 200)\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200)\n"
"}\n"
"")
        self.pushButton_fecharMsg.setObjectName("pushButton_fecharMsg")
        self.horizontalLayout_2.addWidget(self.pushButton_fecharMsg)
        self.label_logo = QtWidgets.QLabel(parent=self.widget_login)
        self.label_logo.setGeometry(QtCore.QRect(10, 10, 101, 101))
        self.label_logo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_logo.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titLogin.setText(_translate("MainWindow", "Log In"))
        self.lineEdit_nomeLogin.setPlaceholderText(_translate("MainWindow", "  Usuário"))
        self.lineEdit_senhaLogin.setPlaceholderText(_translate("MainWindow", "  Senha"))
        self.pushButton_entrarLogin.setText(_translate("MainWindow", "E n t r a r"))
        self.label_msg.setText(_translate("MainWindow", "Mensagem"))
        self.pushButton_fecharMsg.setText(_translate("MainWindow", "X"))
