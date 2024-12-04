import psycopg2
from psycopg2 import Error

class Database:
    def __init__(self):
        self.connection = None
        try:
            self.connection = psycopg2.connect(
                dbname="library_db",
                user="postgres",
                password="1234",
                host="127.0.0.1",
                port="5432"
            )
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error executing query: {e}")
            return False

    def fetch_one(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Error as e:
            print(f"Error fetching data: {e}")
            return None

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()