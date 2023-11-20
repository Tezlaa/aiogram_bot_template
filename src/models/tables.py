from models.base import DatabaseTable


class TestTable(DatabaseTable):
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS test(
                id INTEGER PRIMARY KEY,
                message TEXT
            )
        """
        self.sql_query_and_commit(sql)
