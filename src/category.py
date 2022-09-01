from src.orm import *
from src.db_utilities import *

class Category:
    __table__ = 'categories'
    columns = ['id', 'name']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in columns: {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by_name(self, name, cursor):
        query = """
            SELECT * from %s WHERE name = '%s'""" \
                % (self.__table__, name)
        cursor.execute(query)
        record = cursor.fetchone()
        category = build_from_record(self, record)

        return category

    @classmethod
    def find_or_create_by_name(self, name, conn, cursor):
        name = self.find_by_name(name, cursor)

        if not name:
            query = """
                INSERT INTO %s (name) VALUES ('%s')""" \
                    % (self.__table__, name)
            cursor.execute(query)
            conn.commit()
