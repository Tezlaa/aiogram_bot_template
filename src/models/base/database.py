import logging
import sqlite3
import abc

from config.settings import DATABASE

from models.base.singleton import Singleton


class DatabaseConfig(metaclass=Singleton):
    """
    Connect to the database and create cursor.
    """
    
    def __init__(self):
        self.connect = sqlite3.connect(
            '{}.db'.format(
                DATABASE.get('DATABASE_NAME', 'database')
            )
        )

        if self.connect:
            logging.info('Database is connected!')
        else:
            logging.warning(self.connect)
            return
        
        self.cursor = self.connect.cursor()


class Table:
    _database = DatabaseConfig()
     
    def __init__(self) -> None:
        self.create_table()
        
    def sql_query_and_commit(self, sql: str, variables: tuple = ()) -> None:
        self._database.cursor.execute(sql, variables)
        self._database.connect.commit()
        
    @abc.abstractmethod
    def create_table(self):
        """ Initial database table """