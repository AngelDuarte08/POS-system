from Models.Customer import Customer
from Models.Product import Product
from database.Model import Model
import mysql.connector


class Ticket():
    def __init__(self):
        self.__idTicket = ""
        self.__producto = ""
        self.__fecha = ""
        self.__direccion = ""
        self.__precio = ""
        self.__cantidad = ""
        self.__caja = ""
        self.__correo = ""
        self.__tel = ""
        self.__total = ""
        self.__iva = ""
        self.__sucursal = ""

    def crearTicket(self):

        customer = Customer()
        product = Product()

        try: 
            datoCliente = customer.consultCustomer(input("Nombre del cliente: "))
            if datoCliente == 0: 
                pass
            else: 
                database = Model("", "", 1)
                self.__idTicket = database.procedure("crearTicket" , [datoCliente])[0]
                otro = "s"
                while otro in ("s","S"):
                    datoProduct = product.consultProduct(input("Codigo de barras del producto: "))
                    if datoProduct == 0: 
                        pass 
                    else: 
                        idProducto = datoProduct[0][0]
                    database = Model("", "", 1)
                    database.procedimiento("insertar" ,(self.__idTicket, idProducto))

                    database = Model("", "", 1)
                    database.procedure("actualizarTotal" ,(self.__idTicket, idProducto))
                    otro = input("Deseas agregar otro producto (s/n): ")
                

        except mysql.connector.Error as err:
            print("se genero un ERROR") 
        finally: 
            pass 