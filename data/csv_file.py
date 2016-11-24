import pandas as pd
import os
import collections

# import data
import data.data


class CSVCorpus(data.data.Data):
    """
    CSV Corpus
    """

    def __init__(self, csv_file=None):
        """
        :param csv_file:    Path to CSV file
        """

        assert(os.path.isfile(csv_file))

        tmp_corpus = pd.read_csv(csv_file, quotechar="'")
        self.corpus = tmp_corpus.set_index('title')

    def get_instruction(self, drawing_list):
        """
        Queries the corpus for a set of instructions

        :param drawing_list:    list of instruction names
        :return:                Pandas DataFrame
        """

        if drawing_list is None:
            raise ValueError

        if not isinstance(drawing_list, collections.Iterable):
            drawing_list = {drawing_list}

        drawing_list_str = [str(i) for i in drawing_list]

        try:
            result = self.corpus.loc[drawing_list_str]
        except KeyError:
            result = None

        return result

if __name__ == "__main__":

    file_path = '/Users/skin/repository/iba-lewitt-py/docs/lewitt-corpus/wall_drawing_corpus.csv'
    corpus = CSVCorpus(file_path)

    query_instruction_list = [20, 37, 123123123]

    response = corpus.get_instruction(query_instruction_list)
    print(response)