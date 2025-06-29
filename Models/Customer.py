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

    def eliminate(self):
        self.__name = input("Ingresa el nombre del cliente a eliminar: ")
        query = f"UPDATE Clientes SET status = 0 WHERE Clientes.nombre = '{self.__name}'"

        database = Model(query, "", 1)
        database.command()

        print(f"Cliente {self.__name} eliminado corectamente.")

    def consult(self, name):
        self.__name = name
        query = "SELECT * FROM Clientes WHERE Clientes.nombre = %s"
        
        database= Model(query, (self.__name, ), 0)
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