#libraries for the views 
import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QCheckBox, QMessageBox
from PyQt6.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt6.QtCore import Qt

#libraries that inmport a method
from Models.User import User
from Views.MainView import MainView

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        with open("css/login.css","r") as file: 
            style = file.read()
        self.setStyleSheet(style)

    def setupUI(self):
        self.setWindowTitle("Tienda Punto de Venta - Menú Principal")
        self.resize(350, 400)
        self.generateForm()
        self.show()

    def generateForm(self):
        # Widget central y layout principal
        central = QWidget(self)
        self.setCentralWidget(central)

        layout_exterior = QVBoxLayout(central)
        layout_exterior.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Contenedor del formulario
        contenedor = QWidget()
        contenedor.setObjectName("formulario")
        contenedor.setFixedWidth(400)

        layout_formulario = QVBoxLayout()
        layout_formulario.setSpacing(12)

        # Título
        titulo = QLabel("Inicio de sesión")
        titulo.setObjectName("titulo")
        titulo.setFont(QFont("Arial", 20))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Campos
        self.email = QLineEdit()
        self.email.setPlaceholderText("Nombre de usuario")

        self.lePasswd = QLineEdit()
        self.lePasswd.setPlaceholderText("Contraseña")
        self.lePasswd.setEchoMode(QLineEdit.EchoMode.Password)

        # Botones
        acceder = QPushButton("Acceder")
        acceder.setFixedWidth(120)
        acceder.setObjectName("acceder")
        acceder.clicked.connect(self.Login)

        #Check box
        self.CheckViewPasswd = QCheckBox(self)
        self.CheckViewPasswd.setText("Ver contraseña")
        self.CheckViewPasswd.clicked.connect(self.showPasswd)

        # Agregar al layout
        layoutAccess = QHBoxLayout()
        layoutAccess.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutAccess.addWidget(acceder)

        layoutForget = QHBoxLayout()
        layoutForget.setSpacing(0)
        layoutForget.setContentsMargins(0,0,0,0)
        layout_formulario.addWidget(titulo)


        layout_formulario.addWidget(self.email)
        layout_formulario.addWidget(self.lePasswd)
        layout_formulario.addWidget(self.CheckViewPasswd)
        layout_formulario.addLayout(layoutAccess)
        layout_formulario.addLayout(layoutForget)

        contenedor.setLayout(layout_formulario)
        layout_exterior.addWidget(contenedor)         

    def showPasswd(self, clicked): 
        if clicked:
            self.lePasswd.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lePasswd.setEchoMode(QLineEdit.EchoMode.Password)

    def Login(self): 
        user = User()
        try: 
            emailLogin = self.email.text()
            passwdLogin = self.lePasswd.text()

            loginUser = user.consult(emailLogin)
            if loginUser is None:
                raise ValueError("Usuario no encontrado")
            
            row = loginUser[0]
            emailDatabase = row[8]
            passwdDatabase = row[9]

            if emailDatabase == emailLogin and passwdDatabase == passwdLogin:
                self.mainView = MainView(emailDatabase, "404: Precios No Encontrados")
                self.mainView.show()
                self.close()
            else: 
                QMessageBox.warning(self, "Error", "Credenciales incorectas")

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))