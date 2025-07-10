import mysql.connector

from Models.User import User
from database.Model import Model
from Models.Customer import Customer
from Models.Product import Product

class Ticket():
    def __init__(self):
        self.idTicket = ""
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

    def crearTicket(self, tel, sucursal, user):
        self.tel = tel
        self.sucursal = sucursal
        self.user = user 
        self.customer = Customer()
        self.dbUser = User()

        try: 
            dataCustumer = self.customer.consult(self.tel)
            rowC = dataCustumer[0]
            dataUser = self.dbUser.consult(self.user)
            rowU = dataUser[0]

            if dataCustumer == 0:
                pass
            else: 
                database = Model("","",1)
                rows = database.procedure('crearTicket', (rowC[0], rowU[0], f'{self.sucursal}'))
                print(rows)
                if not rows:
                    raise ValueError("No se pudo crear el ticket")
                self.idTicket = rows[0]
                return self.idTicket

        except mysql.connector.Error as err: 
            print(f"ERROR{err}")
        finally:
            print("Venta finalizada")


    def addProduct(self, barCode, idTicket):
        self.barCode = barCode
        self.idTicket = idTicket
        self.product = Product()


        try: 
            dataProcduct = self.product.getdataProduct(self.barCode)
            row = dataProcduct[0]
            self.idProduct = row[0]

            if dataProcduct == 0: 
                pass
            else: 
                database = Model("","",1)
                database.procedure('insertar', (self.idTicket, self.idProduct))
                database = Model("","",1)
                database.procedure('actualizarTotal',(self.idTicket, self.idProduct))

                return dataProcduct

        except mysql.connector.Error as err:
            print(f"Error {err}")
        finally: 
            print("Venta finalizada")