from models.base import database


class TestTable(database.Table):
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS test(
                id INTEGER PRIMARY KEY,
                message TEXT
            )
        """
        self.sql_query_and_commit(sql)