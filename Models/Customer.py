#This is the file where the child class is created and inherited from person
# import of the file person 
from Models.Person import Person
from database.Model import Model

class Customer(Person): 
    def __init__(self):
        self.__rfc = ""
        self.__credit = ""

    def register(self,values):
        self.values = values
        query =  "INSERT INTO Clientes (nombre, direccion, edad, tel, email, rfc, credito) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        database = Model(query, self.values, 1)
        database.command()

    def delete(self, tel):
        self.__tel = tel
        query = f"UPDATE Clientes SET estatus = 0 WHERE Clientes.tel = '{self.__tel}'"

        database = Model(query, "", 1)
        database.command()

    def consult(self, tel):
        self.__tel = tel
        query = "SELECT * FROM Clientes WHERE Clientes.tel = %s"
        
        database= Model(query, (self.__tel, ), 0)
        return database.command()


    def consultTable(self):
        query = f"SELECT * FROM Clientes"
        
        database = Model(query, "", 0)
        return database.command()

    def consultCustomer(self, nombreCliente): 
        query = f"SELECT Clientes.idCliente FROM Clientes WHERE Clientes.nombre = '{nombreCliente}'"

        database = Model(query,"",0) 
        result  = database.comadno()
        if result:
            return result[0][0]
        else: 
            result1 = input("El cliente no existe, ¿Desesa registarlo? (S/N)")
            if result1 in ("s", "S"):
                self.registar 
            else: 
                return 0 
            
    def getAccessKeys(self):
        query = "SELECT tel FROM Clientes"
        database = Model(query, "", 0)
        return database.command()