import os

import sqlite3
from abc import ABCMeta, abstractmethod


class Data(metaclass=ABCMeta):
    """
    Data/Corpus Abstract Base Class.

    Abstract Factory
    """

    Handlers = {'SQLite'}

    def __int__(self, handler_type, **kwargs):
        """

        :param handler_type:
        :param kwargs:
        :return:
        """

        assert(handler_type in Data.Handlers)

    @abstractmethod
    def get_instruction(self, drawing_list, **kwargs):
        """
        Get drawing instruction(s)

        :param drawing_list:    list of drawing title(s)
        :return:                instruction(s)
        """
        pass


class SQLiteHandler(Data):
    """
    SQLite Handler
    """

    DEFAULT_TABLE_NAME = 'instructions'

    query = 'select * ' \
            'from {} ' \
            'where id in {};'

    def __init__(self, db_file_name, **kwargs):
        """
        :param db_file_name:
        :param kwargs
        """

        if not os.path.exists(db_file_name):
            raise FileNotFoundError(db_file_name)

        self.file = db_file_name

        # connect to the sqlite database and get a cursor
        self.connection = sqlite3.connect(self.file)
        self.cursor = self.connection.cursor()

    def get_instruction(self, drawing_ids, **kwargs):
        """
        Get an instruction from the Lewitt Corpus

        :param drawing_ids: tuple of drawing ids
        :param kwargs:
        :return:            tuple or None
        """

        if not isinstance(drawing_ids, tuple):
            raise ValueError

        if 'instruction_table' in kwargs:
            table_name = kwargs.get('instruction_table')
        else:
            table_name = SQLiteHandler.DEFAULT_TABLE_NAME

        # construct the query
        query_statement = SQLiteHandler.query.format(table_name, drawing_ids)
        if not sqlite3.complete_statement(query_statement):
            raise sqlite3.ProgrammingError

        with self.connection:
            try:
                for row in self.cursor.execute(query_statement):
                    yield row
            except sqlite3.Error as error:
                return None


if __name__ == "__main__":
    handler = SQLiteHandler('/Users/skin/repository/iba-lewitt-py/data/lewitt_corpus.db')

    drawing_ids = (11, 45, 97, 1180)

    for i in handler.get_instruction(drawing_ids, instruction_table='instructions'):
        print(i)
