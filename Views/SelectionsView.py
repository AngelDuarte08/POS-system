from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
from Models.User import User
from Models.Customer import Customer
from Models.Supplier import Supplier
from Models.Product import Product

class SelectionMain(QMainWindow):
    def __init__(self, typeEntity, mainView):
        super().__init__()
        self.typeEntity = typeEntity
        self.mainView = mainView
        self.setupUI()

        # Aplicar estilo CSS
        with open("css/User.css", "r") as file:
            style = file.read()
        self.setStyleSheet(style)

    def setupUI(self):
        self.setWindowTitle("Tienda Punto de Venta - Menu selecion")
        self.setFixedSize(1512, 830)
        self.generateForm()
        self.show()

    def generateForm(self):
        # Widget central
        central = QWidget(self)
        self.setCentralWidget(central)
        # Layout principal
        layout = QVBoxLayout(central)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        if self.typeEntity == "User":
            Entity = "Usuario"
        elif self.typeEntity == "Customer":
            Entity = "Cliente"
        elif self.typeEntity == "Supplier": 
            Entity = "Proveedor"
        else:
            Entity = "Producto"

        # Título
        lUser = QLabel(f"Menú de {Entity}")
        lUser.setObjectName("titulo")
        lUser.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lAsk = QLabel("¿Qué deseas hacer?")
        lAsk.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Table 
        self.tableUser = QTableWidget()
        self.tableUser.setFixedSize(900,200)
        self.showUsers()
        palette = self.tableUser.palette()

        # Botones
        self.btnRegister = QPushButton("Registrar")
        self.btnDelete = QPushButton("Eliminar")
        self.btnConsult = QPushButton("Consultar")
        self.btnExit = QPushButton("Salir")
        self.btnExit.setObjectName("Exit")

        # Agregar al layout
        layout.addStretch()
        layout.addWidget(lUser)
        layout.addWidget(lAsk)
        layout.addWidget(self.tableUser)
        layout.addWidget(self.btnRegister)
        layout.addWidget(self.btnDelete)
        layout.addWidget(self.btnConsult)
        layout.addWidget(self.btnExit)
        layout.addStretch()

        # Eventos
        self.btnExit.clicked.connect(self.backView)

    def showUsers(self):
        if self.typeEntity== "User":
                model = User()
                titles = ["ID", "Nombre", "Dirección", "Edad", "Teléfono", "Email", "Status", "Rol", "Clave de acceso", "Contraseña"]
        elif self.typeEntity == "Customer":
            model = Customer()
            titles = ["ID", "Nombre", "Dirección", "Edad", "Teléfono", "Email", "Status", "RFC", "Crédito"]
        elif self.typeEntity == "Supplier":
            model = Supplier()
            titles = ["ID", "Nombre", "Dirección", "Edad", "Teléfono", "Email", "Status", "RFC", "Productos", "Horarios", "Crédito"]
        else:  # Producto
            model = Product()
            titles = ["ID", "Nombre", "Cantidad", "Fecha de Caducidad", "Fecha de Entrega", "Código de Barras", "Status", "Precio"]

        data = model.consultTable()
            

        if data:
            self.tableUser.setRowCount(len(data))
            self.tableUser.setColumnCount(len(data[0]))
            self.tableUser.setHorizontalHeaderLabels(titles)

            for i, fila in enumerate(data):
                for j, valor in enumerate(fila):
                    item = QTableWidgetItem(str(valor))
                    self.tableUser.setItem(i, j, item)
        else:
            self.tableUser.setRowCount(0)
            self.tableUser.setColumnCount(0)

    def backView(self):
        self.close()
        self.mainView.show()