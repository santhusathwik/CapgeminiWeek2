from abc import ABC,abstractmethod

class IDatabaseOperations:
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting Data in SQL database")
    def update(self):
        print("Updating Data in SQL database")
    def delete(self):
        print("Deleting Data in SQL database")
class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting Data in NoSQL database")
    def update(self):
        print("Updating Data in NoSQL database")
    def delete(self):
        print("Deleting Data in NoSQL database")
sql=SQLDatabase()
no=NoSQLDatabase()
sql.insert()
sql.update()
sql.delete()
no.insert()
no.update()
no.delete()