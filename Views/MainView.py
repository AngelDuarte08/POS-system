from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

from Views.SelectionsView import SelectionMain

# from Views.UserView import UserView

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

        # Aplicar estilo CSS
        with open("css/mainView.css", "r") as file:
            style = file.read()
        self.setStyleSheet(style)

    def setupUI(self):
        self.setWindowTitle("Tienda Punto de Venta - Menú Principal")
        self.resize(350, 400)
        self.generateForm()
        self.show()

    def generateForm(self):
        central = QWidget(self)
        self.setCentralWidget(central)
        
        contenedor = QWidget()
        contenedor.setObjectName("formulario")
        contenedor.setFixedSize(400,400)

        layout = QVBoxLayout()

        layoutPrincipal = QVBoxLayout(central)
        layoutPrincipal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Etiqueta
        title = QLabel("Menú principal PV")
        title.setObjectName("titulo")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Botones
        self.btnUser = QPushButton("Usuario")
        self.btnCustome = QPushButton("Cliente")
        self.btnSupplier = QPushButton("Proveedor")
        self.btnProduct = QPushButton("Producto")
        self.btnExit = QPushButton("Salir")
        self.btnExit.setObjectName("Exit")

        # Agregar al layout
        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(self.btnUser)
        layout.addWidget(self.btnCustome)
        layout.addWidget(self.btnSupplier)
        layout.addWidget(self.btnProduct)
        layout.addWidget(self.btnExit)
        layout.addStretch()

        contenedor.setLayout(layout)

        layoutPrincipal.addWidget(contenedor)

        

        # Eventos
        self.btnUser.clicked.connect(self.openSelectionUser)
        self.btnCustome.clicked.connect(self.openSelectionCustumer)
        self.btnSupplier.clicked.connect(self.openSelectionSupplier)
        self.btnProduct.clicked.connect(self.openSelectionProduct)
        self.btnExit.clicked.connect(self.close)

    def openSelectionUser(self):
        self.hide()
        self.userSelection = SelectionMain("User",self)
        self.userSelection.show()

    def openSelectionCustumer(self):
        self.hide()
        self.customerSelection = SelectionMain("Customer",self)
        self.customerSelection.show()  

    def openSelectionSupplier(self):
        self.hide()
        self.supplierSelecion = SelectionMain("Supplier", self)
        self.supplierSelecion.show
    
    def openSelectionProduct(self):
        self.hide()
        self.productSelecion = SelectionMain("Product", self)
        self.productSelecion. show