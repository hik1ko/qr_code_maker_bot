# Object Relation Mapping
import psycopg2


class DB:
    connection = psycopg2.connect(
        dbname="qr_code_database",
        user="postgres",
        host="localhost",
        port=5432,
        password=7484728
    )
    cursor = connection.cursor()

    def insert(self):
        self_dict = self.__dict__
        table_name = self.__class__.__name__.lower() + "s"
        col_name = " , ".join(self_dict.keys())
        format = " , ".join(["%s"] * len(self_dict.values()))
        params = tuple(self_dict.values())
        query = f"insert into {table_name} ({col_name}) values ({format})"
        self.cursor.execute(query, params)
        self.connection.commit()


class User(DB):
    def __init__(self, first_name, last_name, username, telegram_id):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.telegram_id = telegram_id
