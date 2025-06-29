#This is the file where the child class is created and inherited from person
# import of the file person 
from Models.Person import Person
from database.Model import Model

class User(Person): 
    def __init__(self):
        self.__role = "" 
        self.__accessKey = ""
        self.__password  = ""

    def register(self,values):
        self.values = values
        query =  "INSERT INTO Usuarios (nombre, direccion, edad, tel, email, rol, claveDeAcceso, passwd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        
        database = Model(query, self.values, 1)
        database.command()

    def eliminate(self):
        self.__name = input("Ingresa el nombre del usuario a eliminar: ")
        query = f"UPDATE Usuarios SET estatus = 0 WHERE Usuarios.claveDeAcceso = '{self.__name}'"

        database = Model(query, "", 1)
        database.command()

        # print(f"Usuario {self.__name} eliminado corectamente.")

    def consult(self, name):
        self.__name = name
        query = "SELECT * FROM Usuarios WHERE Usuarios.claveDeAcceso = %s"
        
        database= Model(query, (self.__name, ), 0)
        return database.command()

    def consultTable(self):
        query = f"SELECT * FROM Usuarios"

        database = Model(query, "", 0)
        return database.command()