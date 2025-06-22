#This is the file where the child class is created and inherited from person
# import of the file person 
from Models.Person import Person
from database.Model import Model

class Customer(Person): 
    def __init__(self):
        self.__rfc = ""
        self.__credit = ""

    def register(self):
        self.__name = input("Ingrese su nombre: ")
        self.__direction = input("Ingrese su dirección: ")
        self.__age = input("Ingrese su edad: ")
        self.__tel = input("Ingrese su numero de telefono: ")
        self.__email = input("Ingrese su correo electronico: ")
        self.__status = 1 
        self.__rfc = input("Ingrese su RFC: ")
        self.__credit = input("Ingrese su credito: ")
        proceed = input("¿Desea proceder con el registro? (S/N)").upper()

        if proceed == "S" or proceed == "SI": 
            print("Registrando Cliente...")

            query =  "INSERT INTO Clientes (nombre, direccion, edad, tel, email, status, rfc, credito) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.__name, self.__direction, self.__age, self.__tel, self.__email, self.__status, self.__rfc, self.__credit)

            database = Model(query, values, 1)
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