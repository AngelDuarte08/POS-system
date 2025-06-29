from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit,
    QMainWindow, QComboBox, QMessageBox, QCompleter
)
from PyQt6.QtCore import Qt

from Models.User import User
from Models.Customer import Customer
from Models.Supplier import Supplier
from Models.Product import Product

class DeleteView(QMainWindow):
    def __init__(self, typeEntity, selectionView):
        super().__init__()
        self.typeEntity = typeEntity
        self.selectionView = selectionView
        with open("css/Delete.css","r") as file: 
            style = file.read()
        self.setStyleSheet(style)

        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Tienda Punto de Venta - Menú de Registro")
        self.resize(600, 500)
        self.generateForm()
        self.show()

    def generateForm(self):
        central = QWidget()
        self.setCentralWidget(central)

        contenedor = QWidget()
        contenedor.setObjectName("formulario")
        contenedor.setFixedSize(500,500)

        if self.typeEntity == "User":
            self.Entity = "Usuario"
            acess = "Nombre de Usuario"
            self.model = User()
        elif self.typeEntity == "Customer":
            self.Entity = "Cliente"
            acess = "Numero de telefono"
            self.model = Customer()
        elif self.typeEntity == "Supplier": 
            self.Entity = "Proveedor"
            acess = "Correo electronico"
            self.model = Supplier()
        else:
            self.Entity = "Producto"
            acess = "Nombre del producto"
            self.model = Product()

        layoutPrincipal = QVBoxLayout()

        layout = QVBoxLayout()

        #title
        title = QLabel(f"Menu de {self.Entity}")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ask = QLabel(f"Inserte el {acess}")
        ask.setObjectName("aks")
        ask.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #input
        self.cbAcess = QComboBox()
        self.cbAcess.setEditable(True)
        values = self.acessItems()
        self.cbAcess.addItems(values)

        completer = QCompleter(values)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)


        #button
        btnSave = QPushButton("Guardar")
        btnExit = QPushButton("Cancelar")
        btnExit.setObjectName("Exit")
        
        layout.addWidget(title)
        layout.addWidget(ask)
        layout.addWidget(self.cbAcess)
        layout.addWidget(btnSave)
        layout.addWidget(btnExit)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #events
        btnSave.clicked.connect(self.deleteEntity)
        btnExit.clicked.connect(self.backView)

        contenedor.setLayout(layout)

        layoutPrincipal.addWidget(contenedor, alignment=Qt.AlignmentFlag.AlignCenter)

        central.setLayout(layoutPrincipal)


    def acessItems(self):
        keys = self.model.getAccessKeys()
        onlyValues = [row[0] for row in keys]
        return onlyValues
    

    def backView(self):
        self.close()
        self.selectionView.show()

    def deleteEntity(self):
        self.key = self.cbAcess.currentText()
        self.model.delete(self.key)

        QMessageBox.information(self, "Éxito",f"{self.Entity} eliminado Exitosamente.")
