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
        """

        self.assertTrue(os.path.exists(SQLHandlerTests.DATABASE_FILE))
        self.database_file = SQLHandlerTests.DATABASE_FILE

        # valid and invalid lewitt instructions
        self.valid_instructions = (11, 45, 97, 1180)
        self.invalid_instructions = (-1, 0, '50 C')

    def test_database_connection(self):
        """
        Is the connection an instance of an sqlite3.Connection?
        """

        handler = SQLiteHandler(SQLHandlerTests.DATABASE_FILE)
        self.assertIsInstance(handler.connection, sqlite3.Connection)

    def test_get_instruction_raises_value_error(self):
        """
        Does the get_instruction method raise a ValueError if it is queried with anything other than a tuple object?
        """

        handler = SQLiteHandler(SQLHandlerTests.DATABASE_FILE)

        with self.assertRaises(ValueError):
            generator = handler.get_instruction([])
            next(generator)

            generator = handler.get_instruction(None)
            next(generator)

    def test_get_instruction_returns_none_invalid_instructions(self):
        """
        Does the get_instruction method return None for invalid queries?
        """

        handler = SQLiteHandler(SQLHandlerTests.DATABASE_FILE)

        for row in handler.get_instruction(self.invalid_instructions):
            self.assertIsNone(row)

    def test_get_instruction_returns_valid_instruction_string(self):
        """
        Does the get_instruction method return non empty tuples for valid queries?
        """

        handler = SQLiteHandler(SQLHandlerTests.DATABASE_FILE)

        valid_count = 0
        for row in handler.get_instruction(self.valid_instructions):
            self.assertIsInstance(row, tuple)
            self.assertGreater(len(row), 0)
            valid_count += 1

        self.assertEqual(len(self.valid_instructions), valid_count)

    def test_get_instruction_returns_valid_instruction_string_two(self):
        """
        Does the get_instruction method return the correct number of non empty tuples for valid queries?
        """

        handler = SQLiteHandler(SQLHandlerTests.DATABASE_FILE)

        instruction_list = tuple(set(self.valid_instructions + self.invalid_instructions))

        valid_count = 0
        for row in handler.get_instruction(instruction_list):
            self.assertIn(type(row), (tuple, None))

            if isinstance(row, tuple) and len(row) > 0:
                valid_count += 1

        self.assertEqual(len(self.valid_instructions), valid_count)

if __name__ == '__main__':
    unittest.main()
