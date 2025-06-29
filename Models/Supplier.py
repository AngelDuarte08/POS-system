#Proveedor
#This is the file where the child class is created and inherited from person
# import of the file person 
from Models.Person import Person
from database.Model import Model

class Supplier(Person): 
    def __init__(self):
        self.__rfc = ""
        self.__credit = ""
        self.__products = ""
        self.__Schedules = "" #horarios

    def register(self, values):
        self.values = values 
        query =  "INSERT INTO Provedores (nombre, direccion, edad, tel, email, rfc, producto, horarios, credito) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        database = Model(query, self.values, 1)
        database.command()

    def delete(self, email):
        self.__email = email
        query = f"UPDATE Provedores SET estatus = 0 WHERE Provedores.email = '{self.__email}'"

        database = Model(query, "", 1)
        database.command()

    def consult(self, email):
        self.__email = email
        query = "SELECT * FROM Provedores WHERE Provedores.email = %s"
        
        database= Model(query, (self.__email, ), 0)
        return database.command()

    def consultTable(self):
        query = f"SELECT * FROM Provedores"
        
        database = Model(query, "", 0)
        return database.command()
    
    def getAccessKeys(self):
        query = "SELECT email FROM Provedores"
        database = Model(query, "", 0)
        return database.command()