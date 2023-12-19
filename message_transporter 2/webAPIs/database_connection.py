import psycopg2
from psycopg2 import sql


class DatabaseHandler:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='transporter',
            user="postgres",
            password="Priy@nka96",
            host="localhost",
            port=5432
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()