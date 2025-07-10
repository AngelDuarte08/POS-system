#This is the file where the class of database is created 
#import library 
import mysql.connector

class Model():
    def __init__(self, query, values, confirmation):
        #conection with database
        self.__connection = mysql.connector.connect(host = "localhost",
                                                    user = "Angel",
                                                    passwd = "123569",
                                                    database = "PuntoDeVenta2") 
        self.__cursor = self.__connection.cursor()
        self.__query = query 
        self.__values = values
        self.__confirmation = confirmation
    
    def command(self):
        self.__cursor.execute(self.__query, self.__values, self.__confirmation)
        if self.__confirmation == 1: 
            self.__connection.commit()
        result = self.__cursor.fetchall()
        self.__connection.close()
        return result
    
    def procedure(self, procedureName, data):
        self.__cursor.callproc(procedureName,data)
        resultProcedure = self.__cursor.stored_results()
        valueRecived = [0]
        
        for result in resultProcedure: 
            for dato in result:
                valueRecived = dato
        self.__connection.commit()
        self.__connection.close()
        return valueRecived