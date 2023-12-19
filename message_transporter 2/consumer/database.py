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

    def save_product_data(self, meta_info, available_price, stock, source):
        query = sql.SQL("""
            INSERT INTO product_data (meta_info, available_price, stock, source)
            VALUES (%s, %s, %s, %s)
        """)
        values = (meta_info, available_price, stock, source)
        self.cursor.execute(query, values)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()