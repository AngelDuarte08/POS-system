from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget,
    QMainWindow, QComboBox, QMessageBox, QCompleter,QHBoxLayout, QTableWidgetItem, QLineEdit
)
from PyQt6.QtCore import Qt

from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtGui import QTextDocument

from Models.User import User
from Models.Customer import Customer
from Models.Product import Product
from Models.Ticket import Ticket

class SellView(QMainWindow):
    def __init__(self, user , sucursal, mainView):
        super().__init__()
        self.user = user
        self.sucursal = sucursal
        self.mainView = mainView
        self.subTotal = 0
        with open("css/Sell.css","r") as file: 
            style = file.read()
        self.setStyleSheet(style)

        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Tienda Punto de Venta - Menú de Venta")
        self.showFullScreen()
        self.generateForm()
        self.show()

    def generateForm(self):
        central = QWidget()
        self.setCentralWidget(central)

        contenedor = QWidget()
        contenedor.setObjectName("formulario")
        contenedor.setFixedSize(350,350)

        titles = ["Nombre Producto", "Codigo de Barras", "Precio"]
        layoutPrincipal = QHBoxLayout()
        layout = QVBoxLayout()

        #title
        title = QLabel("Menu de Ventas")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ask = QLabel("Inserte el codigo de barras del producto")
        self.ask.setObjectName("aks")
        self.ask.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ask1 = QLabel("Ingrese el numero de telefono del cliente")
        ask1.setObjectName("aks")
        ask1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.lIdTicket = QLabel("Ticket No.")
        self.lSubtotal= QLabel("Subtotal: ")
        self.lIva = QLabel("IVA: ")
        self.lTotal = QLabel("Total: ")

        #input
        self.cbCustomer = QComboBox()
        self.cbCustomer.setEditable(True)
        self.cbCustomer.lineEdit().setPlaceholderText("Selecciona un cliente...")
        values = self.acessItemsCustomer()
        self.cbCustomer.addItems(values)
        self.cbCustomer.setCurrentIndex(-1)

        completer = QCompleter(values)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)

        self.txtProduct = QLineEdit()
        self.txtProduct.setPlaceholderText("Escribe o escanea un código...")
        values = self.acessItemsProduct()
        completer = QCompleter(values)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)

        #button
        self.btnPay = QPushButton("Pagar")
        self.btnExit = QPushButton("Salir")
        self.btnInit = QPushButton("Iniciar venta")
        self.btnExit.setObjectName("Exit")

        self.btnPay.setHidden(True)
        self.btnExit.setHidden(True)
        self.txtProduct.setHidden(True)
        self.ask.setHidden(True)
        self.lSubtotal.setHidden(True)
        self.lIva.setHidden(True)
        self.lTotal.setHidden(True)

        #table
        self.tableSell = QTableWidget()
        self.tableSell.setColumnCount(len(titles))
        self.tableSell.setHorizontalHeaderLabels(titles)

        self.tableSell.setColumnWidth(0,680)
        self.tableSell.setColumnWidth(1,300)
        self.tableSell.setColumnWidth(2,150)

        #layouts
        layout.addWidget(title)
        layout.addWidget(ask1)
        layout.addWidget(self.cbCustomer)
        layout.addWidget(self.lIdTicket)
        layout.addWidget(self.btnInit)
        layout.addWidget(self.ask)
        layout.addWidget(self.txtProduct)
        layout.addWidget(self.lSubtotal)
        layout.addWidget(self.lIva)
        layout.addWidget(self.lTotal)
        layout.addWidget(self.btnPay)
        layout.addWidget(self.btnExit)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #events
        self.btnPay.clicked.connect(self.mostrarTicket)
        self.btnExit.clicked.connect(self.backView)
        self.btnInit.clicked.connect(self.createTicket)
        self.txtProduct.returnPressed.connect(self.addProduct)


        contenedor.setLayout(layout)

        layoutPrincipal.addWidget(contenedor, alignment=Qt.AlignmentFlag.AlignCenter)
        layoutPrincipal.addWidget(self.tableSell)

        central.setLayout(layoutPrincipal)


    def acessItemsCustomer(self):
        customer = Customer()
        keys = customer.getAccessKeys()
        onlyValues = [row[0] for row in keys]
        return onlyValues
    
    def acessItemsProduct(self):
        product = Product()
        keys = product.getBarcode()
        onlyValues = [row[0] for row in keys]
        return onlyValues
    

    def backView(self):
        self.close()
        self.mainView.show()

    def deleteEntity(self):
        pass
    
    def addProduct(self):
        dataProduct = self.ticket.addProduct(self.txtProduct.text(), self.idTicket)

        if not dataProduct:
            QMessageBox.warning(self, "Error", "Producto no encontrado")
            return

        # dataProduct[0] = id, nombre, codigo, precio, ...
        productInfo = dataProduct[0]

        # Puedes elegir qué columnas mostrar (ej. nombre, código, precio)
        nombre   = productInfo[1]
        codigo   = productInfo[2]
        precio   = productInfo[3]

        # Agregar a la tabla existente
        rowPosition = self.tableSell.rowCount()
        self.tableSell.insertRow(rowPosition)

        self.tableSell.setItem(rowPosition, 0, QTableWidgetItem(str(nombre)))
        self.tableSell.setItem(rowPosition, 1, QTableWidgetItem(str(codigo)))
        self.tableSell.setItem(rowPosition, 2, QTableWidgetItem(f"${precio:.2f}"))

        self.subTotal +=  precio
        self.iva = self.subTotal * 0.16
        self.Total = self.subTotal * 1.16

        self.lSubtotal.setText(f"Subtotal: {self.subTotal}")
        self.lIva.setText(f"IVA: {self.iva}")
        self.lTotal.setText(f"Total: {self.Total}")


        self.txtProduct.setText("")

    def createTicket(self):
        self.ticket = Ticket()
        self.idTicket = self.ticket.crearTicket(self.cbCustomer.currentText(), self.sucursal, self.user)
        self.lIdTicket.setText(f"Ticket No. {self.idTicket}")

        self.btnInit.setHidden(True)
        self.btnPay.setHidden(False)
        self.btnExit.setHidden(False)
        self.txtProduct.setHidden(False)
        self.ask.setHidden(False)
        self.lSubtotal.setHidden(False)
        self.lIva.setHidden(False)
        self.lTotal.setHidden(False)


    def mostrarTicket(self):
        if self.tableSell.rowCount() == 0:
            QMessageBox.information(self, "Sin productos", "No se ha agregado ningún producto al ticket.")
            return

        resumen = f"📋 Ticket No. {self.idTicket}\n"
        resumen += f"Cliente: {self.cbCustomer.currentText()}\n"
        resumen += f"Sucursal: {self.sucursal}\n"
        resumen += "-" * 40 + "\n"

        total = 0.0

        for row in range(self.tableSell.rowCount()):
            nombre = self.tableSell.item(row, 0).text()
            codigo = self.tableSell.item(row, 1).text()
            precio = self.tableSell.item(row, 2).text().replace("$", "")
            resumen += f"{nombre} | {codigo} | ${precio}\n"
            total += float(precio)

        resumen += "-" * 40 + f"\n💰 Total: ${total:.2f}\n\n"
        resumen += "Gracias por su compra 🛒"

        # Mostrar y preguntar si desea imprimir
        reply = QMessageBox.question(self, "Ticket generado", resumen + "\n\n¿Desea imprimir el ticket?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.imprimirTicket(resumen)

        # Reiniciar vista
        self.reiniciarVenta()

    def reiniciarVenta(self):
        self.cbCustomer.setCurrentIndex(-1)
        self.cbCustomer.lineEdit().clear()

        self.txtProduct.clear()
        self.txtProduct.setHidden(True)

        self.tableSell.setRowCount(0)
        self.btnInit.setHidden(False)
        self.btnPay.setHidden(True)
        self.btnExit.setHidden(True)
        self.ask.setHidden(True)
        self.lIdTicket.setText("Ticket No.")


    def imprimirTicket(self, texto):
        printer = QPrinter()
        doc = QTextDocument()
        doc.setPlainText(texto)
        doc.print(printer)