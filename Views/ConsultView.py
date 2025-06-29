from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget,
    QMainWindow, QComboBox, QTableWidgetItem, QCompleter, QMessageBox
)
from PyQt6.QtCore import Qt

from Models.User import User
from Models.Customer import Customer
from Models.Supplier import Supplier
from Models.Product import Product

class ConsultView(QMainWindow):
    def __init__(self, typeEntity, selectionView):
        super().__init__()
        self.typeEntity = typeEntity
        self.selectionView = selectionView
        with open("css/Consult.css","r") as file: 
            style = file.read()
        self.setStyleSheet(style)

        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Tienda Punto de Venta - Menú de Consulta")
        self.resize(600, 500)
        self.generateForm()
        self.show()

    def generateForm(self):
        central = QWidget()
        self.setCentralWidget(central)

        contenedor = QWidget()
        contenedor.setObjectName("formulario")
        contenedor.setFixedSize(350,350)

        self.data = []

        if self.typeEntity == "User":
            self.Entity = "Usuario"
            acess = "Nombre de Usuario"
            self.model = User()
            self.titles = ["ID", "Nombre", "Dirección", "Edad", "Teléfono", "Email", "Status", "Rol", "Clave de acceso", "Contraseña"]
        elif self.typeEntity == "Customer":
            self.Entity = "Cliente"
            acess = "Numero de telefono"
            self.model = Customer()
            self.titles = ["ID", "Nombre", "Dirección", "Edad", "Teléfono", "Email", "Status", "RFC", "Crédito"]
        elif self.typeEntity == "Supplier": 
            self.Entity = "Proveedor"
            acess = "Correo electronico"
            self.model = Supplier()
            self.titles = ["ID", "Nombre", "Dirección", "Edad", "Teléfono", "Email", "Status", "RFC", "Productos", "Horarios", "Crédito"]
        else:
            self.Entity = "Producto"
            acess = "Nombre del producto"
            self.model = Product()
            self.titles = ["ID", "Nombre", "Cantidad", "Fecha de Caducidad", "Fecha de Entrega", "Código de Barras", "Status", "Precio"]

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

        #genrate table
        self.tConsult = QTableWidget()
        self.tConsult.setFixedSize(900,50)
        self.tConsult.setColumnCount(len(self.titles))  # Para que se vean las cabeceras desde el inicio
        self.tConsult.setHorizontalHeaderLabels(self.titles)
        self.tConsult.setRowCount(0)  # Vacía al inicio
        layout.addWidget(self.tConsult)

        
        layout.addWidget(title)
        layout.addWidget(ask)
        layout.addWidget(self.cbAcess)
        layout.addWidget(btnSave)
        layout.addWidget(btnExit)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #events
        btnSave.clicked.connect(self.consultEntity)
        btnExit.clicked.connect(self.backView)

        contenedor.setLayout(layout)

        layoutPrincipal.addWidget(contenedor, alignment=Qt.AlignmentFlag.AlignCenter)
        layoutPrincipal.addWidget(self.tConsult)

        central.setLayout(layoutPrincipal)


    def acessItems(self):
        keys = self.model.getAccessKeys()
        onlyValues = [row[0] for row in keys]
        return onlyValues
    

    def backView(self):
        self.close()
        self.selectionView.show()

    def consultEntity(self):
        self.key = self.cbAcess.currentText()
        self.data = self.model.consult(self.key)
        

        if self.data:
            self.tConsult.setRowCount(len(self.data))
            self.tConsult.setColumnCount(len(self.data[0]))
            self.tConsult.setHorizontalHeaderLabels(self.titles)

            for i, fila in enumerate(self.data):
                for j, valor in enumerate(fila):
                    item = QTableWidgetItem(str(valor))
                    self.tConsult.setItem(i, j, item)
        else:
            QMessageBox.information(self, "Sin resultados", f"No se encontró ningún {self.Entity.lower()} con ese dato.")
            self.tConsult.setRowCount(0)
            self.tConsult.setColumnCount(len(self.titles))
            self.tConsult.setHorizontalHeaderLabels(self.titles)
        
