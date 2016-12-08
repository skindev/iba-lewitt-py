import os
import unittest
import sqlite3

from data.data import SQLiteHandler


class SQLHandlerTests(unittest.TestCase):
    """
    SQLHandler Tests
    """

    DATABASE_FILE = "/Users/skin/repository/iba-lewitt-py/data/lewitt_corpus.db"

    def setUp(self):
        """

        :return:
        """

        self.assertTrue(os.path.exists(SQLHandlerTests.DATABASE_FILE))
        self.database_file = SQLHandlerTests.DATABASE_FILE

        # valid and invalid lewitt instructions
        self.valid_instruction_list = [3, 917, 136, 270, 38]
        self.invalid_instruction_list = [-1, 0, '50 C']

    def test_database_connection(self):
        """
        Test Database connection. Is the connection an instance of sqlite3.Connection?

        :return:
        """

        handler = SQLiteHandler(SQLHandlerTests.DATABASE_FILE)
        self.assertIsInstance(handler.connection, sqlite3.Connection)

    def test_get_instruction_raises_value_error(self):
        """
        Does the get_instruction method raise a ValueError if it is queried with anything other than a tuple object?

        :return:
        """

        handler = SQLiteHandler(SQLHandlerTests.DATABASE_FILE)

        with self.assertRaises(ValueError):
            generator = handler.get_instruction([])
            next(generator)

            generator = handler.get_instruction(None)
            next(generator)


if __name__ == '__main__':
    unittest.main()
