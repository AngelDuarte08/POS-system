from database.Model import Model

class Product():
    def __init__(self):
        self.__idDeProducto = "" 
        self.__nombreProducto = ""
        self.__cantidad = ""
        self.__fechaDeCaducidad = ""
        self.__fechaDeEntrega = ""
        self.__codigoDeBarra = ""
        self.__status = ""
        self.__precio = ""

    def register(self, values):
        self.values = values 
        query = "INSERT INTO Productos (nombreProducto, cantidad, fechaDeCaducidad, fechaDeEntrega, codigoDeBarra, precio) VALUES (%s, %s, %s, %s, %s, %s)"

        database = Model(query, self.values, 1)
        database.command()


    def delete(self, name):
        self.__name = name 
        query = f"UPDATE Productos SET estatus = 0 WHERE Productos.nombreProducto = '{self.__name}'"

        database = Model(query, "", 1)
        database.command()

    def consult(self, name):
        self.__name = name
        query = "SELECT * FROM Productos WHERE Productos.nombreProducto = %s"

        database = Model(query, (self.__name,), 0)
        return database.command()


    def consultTable(self):
        query = "SELECT * FROM Productos"

        database = Model(query, "", 0)
        return database.command()

    def consultProduct(self, codigoDeBarras): 
        query = f"SELECT Productos.idProducto FROM Productos WHERE Productos.codigoDeBarra = '{codigoDeBarras}'"

        database = Model(query,"",0) 
        result = database.command()
        if result: 
            return result[0][0]
        else: 
            result1 = input("El producto no exite ¿Deseas registarlo? ")
            if result1 in ("s","S"):
                self.registar
            else: 
                return 0
            
    def getAccessKeys(self):
        query = "SELECT nombreProducto FROM Productos"
        database = Model(query, "", 0)
        return database.command()
    
    def getBarcode(self):
        query = "SELECT codigoDeBarra FROM Productos"
        database = Model(query, "" , 0)
        return database.command()
    
    def getdataProduct(self, barCode):
        query = "SELECT idProducto, nombreProducto , codigoDeBarra, Precio FROM Productos WHERE Productos.codigoDeBarra = %s"
        database = Model(query, [barCode] , 0)
        return database.command()