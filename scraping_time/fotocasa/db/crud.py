from typing import Dict, List
import sqlite3
import os
import logging

# You can see the DB manually throw the DB Browser for SQLite
# https://sqliteonline.com


class CRUD:

    path_db = "db/fotocasa.db"

    def execute(func):
        def wrapper(*args, **kwargs):
            # Creates a connection
            cursor = sqlite3.connect(CRUD.path_db)

            # Executes the command
            cursor.execute(func(*args, **kwargs))

            # Commit the changes
            cursor.commit()
            cursor.close()
        return wrapper

    @classmethod
    @execute
    def insert(cls, table: str, values: Dict[str, str]) -> str:

        # Parses the values to add the quotes
        key = [f"'{key}'" for key in values.keys()]
        val = [f"'{val}'" for val in values.values()]

        logging.debug(f"INSERT INTO {table} ({', '.join(key)})"
                      f" VALUES ({', '.join(val)});")

        # Returns the query
        return f"INSERT INTO {table} ({', '.join(key)})"\
            f" VALUES ({', '.join(val)});"

    @classmethod
    @execute
    def select(cls, table: str, columns: List[str]) -> str:
        return f"SELECT {','.join(columns)} FROM {table};"

    @classmethod
    @execute
    def update(cls, table: str, values: Dict[str, str]) -> str:
        # TODO: Pending to implement
        raise NotImplementedError('Not implemented yet')

    @classmethod
    @execute
    def delete(cls, table: str, values: Dict[str, str]) -> str:
        # TODO: Pending to implement
        raise NotImplementedError('Not implemented yet')


# Testing
if __name__ == "__main__":
    CRUD.path_db = "scraping_time/fotocasa/db/fotocasa.db"
    CRUD.insert('fotocasa_tb', {'text': '1', 'author': 'test'})
