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

    def registar(self):
        self.__nombreProducto = input("Ingrese el nombre del producto: ")
        self.__cantidad = input("Ingrese la cantidad del producto: ")
        self.__fechaDeCaducidad = input("Ingrese la fecha de caducidad (AAAA-MM-DD): ")
        self.__fechaDeEntrega = input("Ingrese la fecha de entrega (AAAA-MM-DD): ")
        self.__codigoDeBarra = input("Ingrese el código de barra del producto: ")
        self.__status = 1  # Asignamos un estado por defecto
        self.__precio = input("Ingrese el precio del producto: ")
        proceder = input("¿Desea proceder con el registro? (S/N): ").upper()

        if proceder == "S" or proceder == "SI":
            print("Registrando producto...")
            query = "INSERT INTO Productos (nombreProducto, cantidad, fechaDeCaducidad, fechaDeEntrega, codigoDeBarra, status, precio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (self.__nombreProducto, self.__cantidad, self.__fechaDeCaducidad, self.__fechaDeEntrega, self.__codigoDeBarra, self.__status, self.__precio)

            database = Model(query, values, 1)
            database.comando


    def eliminar(self):
        self.__name = print("Ingrese el nombre del producto a eliminar: ")
        query = f"UPDATE Productos SET status = 0 WHERE Productos.nombreProducto '{self.__name}'"

        database = Model(query, "", 1)
        database.comando

    def consult(self, name):
        self.__name = name
        query = "SELECT * FROM Productos WHERE Productos.nombreProducto = %s"

        database = Model(query, (self.__name,), 0)
        return database.command()


    def consultTable(self):
        query = "SELECT * FROM Productos"

        database = Model(query, "", 0)
        dato = database.command()

        for dato in dato:
            print("Datos los Productos:")
            print(f": {dato[0]}, {dato[1]} {dato[2]} {dato[3]} {dato[4]} {dato[5]} {dato[6]} {dato[7]}") 

    def consultProduct(self, codigoDeBarras): 
        query = f"SELECT Productos.idProducto FROM Productos WHERE Productos.codigoDeBarra = '{codigoDeBarras}'"

        database = Model(query,"",0) 
        result = database.comadno()
        if result: 
            return result[0][0]
        else: 
            result1 = input("El producto no exite ¿Deseas registarlo? ")
            if result1 in ("s","S"):
                self.registar
            else: 
                return 0