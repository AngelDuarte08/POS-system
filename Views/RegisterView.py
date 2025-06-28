from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QPushButton, QLabel, QLineEdit,
    QMainWindow, QSpinBox, QComboBox
)
from PyQt6.QtCore import Qt

class RegisterView(QMainWindow):
    def __init__(self, typeEntity, selectionView):
        super().__init__()
        self.typeEntity = typeEntity
        self.selectionView = selectionView
        self.campos = {}
        with open("css/Register.css","r") as file: 
            style = file.read()
        self.setStyleSheet(style)
        
        self.fieldsByEntity = {
            "User": {
                "Nombre": "text",
                "Dirección": "text",
                "Edad": "spinbox",
                "Teléfono": "text",
                "Email": "text",
                "Rol": "combo",
                "Clave de acceso": "text",
                "Contraseña": "text"
            },
            "Customer": {
                "Nombre": "text",
                "Dirección": "text",
                "Edad": "spinbox",
                "Teléfono": "text",
                "Email": "text",
                "RFC": "text",
                "Crédito": "text"
            },
            "Supplier": {
                "Nombre": "text",
                "Dirección": "text",
                "Edad": "spinbox",
                "Teléfono": "text",
                "Email": "text",
                "RFC": "text",
                "Productos": "text",
                "Horarios": "text",
                "Crédito": "text"
            },
            "Product": {
                "Nombre": "text",
                "Cantidad": "spinbox",
                "Fecha de Caducidad": "text",
                "Fecha de Entrega": "text",
                "Código de Barras": "text",
                "Precio": "text"
            }
        }

        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Tienda Punto de Venta - Menú de Registro")
        self.resize(600, 500)
        self.generateForm()
        self.show()

    def generateForm(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        if self.typeEntity == "User":
            Entity = "Usuario"
        elif self.typeEntity == "Customer":
            Entity = "Cliente"
        elif self.typeEntity == "Supplier": 
            Entity = "Proveedor"
        else:
            Entity = "Producto"

        titulo = QLabel(f"Registrar {Entity}")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setObjectName("titulo")

        layout.addWidget(titulo)

        self.form = QFormLayout()
        layout.addLayout(self.form)

        self.generar_campos()

        # Botones
        self.btnSave = QPushButton("Guardar")
        self.btnCancel = QPushButton("Cancelar")
        self.btnCancel.clicked.connect(self.backView)

        layout.addWidget(self.btnSave)
        layout.addWidget(self.btnCancel)

        #Events
        self.btnSave.clicked.connect()

    def generar_campos(self):
        estructura = self.fieldsByEntity.get(self.typeEntity, {})

        for etiqueta, tipo in estructura.items():
            if tipo == "text":
                entrada = QLineEdit()
            elif tipo == "spinbox":
                entrada = QSpinBox()
                entrada.setRange(0, 199)
            elif tipo == "combo":
                entrada = QComboBox()
                entrada.addItems(["Administrador", "Empleado", "Gerente", "Jefe"])
            else:
                continue

            self.form.addRow(f"{etiqueta}:", entrada)
            self.campos[etiqueta] = entrada

    def backView(self):
        self.close()
        self.selectionView.show()


    def register():
        pass