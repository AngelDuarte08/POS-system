#This is the file where the child class is created and inherited from person
# import of the file person 
from Models.Person import Person
from database.Model import Model

class User(Person): 
    def __init__(self):
        self.__role = "" 
        self.__accessKey = ""
        self.__password  = ""

    def register(self):
        self.__name = input("Ingrese su nombre: ")
        self.__direction = input("Ingrese su dirección: ")
        self.__age = input("Ingrese su edad: ")
        self.__tel = input("Ingrese su numero de telefono: ")
        self.__email = input("Ingrese su correo electronico: ")
        self.__status = 1 
        self.__role = input("Ingrese su rol: ")
        self.__accessKey = input("Cree su nombre de usuario: ")
        self.__password = input("Cree su contraseña: ")
        proceed = input("¿Desea proceder con el registro? (S/N)").upper()

        if proceed == "S" or proceed == "SI": 
            print("Registrando usuario...")

            query =  "INSERT INTO Usuarios (nombre, direccion, edad, tel, email, estatus, rol, claveDeAcceso, passwd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.__name, self.__direction, self.__age, self.__tel, self.__email, self.__status, self.__role, self.__accessKey, self.__password)

            database = Model(query, values, 1)
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