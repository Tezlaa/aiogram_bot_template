import logging
import sqlite3
import abc

from config.settings import DATABASE


class DatabaseConfig:
    """
    Connect to the database and create cursor.
    """
    
    def __init__(self) -> None:
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


class DatabaseTable(DatabaseConfig, abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.create_table()
    
    def sql_query_and_commit(self, sql: str, variables: tuple = ()) -> None:
        self.cursor.execute(sql, variables)
        self.connect.commit()
        
    @abc.abstractmethod
    def create_table(self):
        """ Initial database table """