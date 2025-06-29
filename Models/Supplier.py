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

    def eliminate(self):
        self.__name = input("Ingresa el nombre del proveedor a eliminar: ")
        query = f"UPDATE Provedores SET status = 0 WHERE Provedores.nombre = '{self.__name}'"

        database = Model(query, "", 1)
        database.command()

        print(f"Proveedor {self.__name} eliminado corectamente.")

    def consult(self, name):
        self.__name = name
        query = "SELECT * FROM Provedores WHERE Provedores.nombre = %s"
        
        database= Model(query, (self.__name, ), 0)
        return database.command()

    def consultTable(self):
        query = f"SELECT * FROM Provedores"
        
        database = Model(query, "", 0)
        return database.command()