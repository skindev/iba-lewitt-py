import os
import unittest
import pandas as pd

from data.csv_file import CSVCorpus


class CSVCorpusTests(unittest.TestCase):
    """
    CSVCorpus class tests
    """

    def setUp(self):
        self.csv_file_path = '/Users/skin/repository/iba-lewitt-py/docs/lewitt-corpus/wall_drawing_corpus.csv'
        self.assertTrue(os.path.exists(self.csv_file_path))

        # valid and invalid lewitt instructions
        self.valid_instruction_list = [3, 917, 136, 270, 38]
        self.invalid_instruction_list = [-1, 0, '50 C']

        self.corpus = CSVCorpus(self.csv_file_path)

    def get_instruction(self, query):
        """
        Helper method that prints out the result of a query before returning it

        :param query:   scalar or iterable query
        :return:        pandas DataFrame
        """

        result = self.corpus.get_instruction(query)
        print(result)

        return result

    def test_get_instruction_raises_error(self):
        """
        Does the get_instruction method raise a ValueError if it is queried with a None object?

        :return:
        """

        with self.assertRaises(ValueError):
            self.corpus.get_instruction(None)

    def test_get_instruction_returns_dataframe(self):
        """
        Does the get_instruction method return a DataFrame (if queried with something other than None)?
        :return:
        """

        self.assertIsInstance(self.get_instruction(self.valid_instruction_list[0]), pd.DataFrame)

    def test_single_valid_instruction(self):
        """
        Does a valid scalar and list query return a DataFrame with one instruction?

        :return:
        """

        # query is a scalar
        self.assertEqual(self.get_instruction(self.valid_instruction_list[0]).size, 1)

        # query is a list
        self.assertEqual(self.get_instruction(self.valid_instruction_list[0:1]).size, 1)

    def test_single_invalid_instruction(self):
        """
        Does an invalid query return None?

        :return:
        """

        self.assertIsNone(self.get_instruction(self.invalid_instruction_list[0:1]))

    def test_many_valid_queries(self):
        """
        Does a list of valid queries return the correct number of instructions?

        :return:
        """

        result = self.get_instruction(self.valid_instruction_list)

        self.assertEqual(result.size, len(self.valid_instruction_list))

    def test_many_mixed_queries(self):
        """

        :return:
        """

        # merge the valid and invalid instruction lists
        mixed_query_list = self.invalid_instruction_list + self.valid_instruction_list
        mixed_query_list = list(set(mixed_query_list))

        result = self.get_instruction(mixed_query_list)
        self.assertEqual(result.size, len(mixed_query_list))


if __name__ == '__main__':
    unittest.main()
