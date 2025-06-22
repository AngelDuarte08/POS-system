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

    def register(self):
        self.__name = input("Ingrese su nombre: ")
        self.__direction = input("Ingrese su dirección: ")
        self.__age = input("Ingrese su edad: ")
        self.__tel = input("Ingrese su numero de telefono: ")
        self.__email = input("Ingrese su correo electronico: ")
        self.__status = 1 
        self.__rfc = input("Ingrese su RFC: ")
        self.__products = input("Ingrese los productos que vende: ")
        self.__Schedules = input("Ingrese los horaios de assitencia: ")
        self.__credit = input("Ingrese su credito: ")
        proceed = input("¿Desea proceder con el registro? (S/N)").upper()

        if proceed == "S" or proceed == "SI": 
            print("Registrando Proveedor...")

            query =  "INSERT INTO Provedores (nombre, direccion, edad, tel, email, status, rfc, produto, horaios, credito) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.__name, self.__direction, self.__age, self.__tel, self.__email, self.__status, self.__rfc, self.__products, self.__Schedules, self.__credit)

            database = Model(query, values, 1)
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