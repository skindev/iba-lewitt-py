import csv

from data.data import Data


class CSVCorpus(Data):
    """

    """

    def __init__(self, csv_file=None):
        """

        :param csv_file:    Path to CSV file
        """


if __name__ == "__main__":
    corpus = CSVCorpus('/Users/skin/repository/iba-lewitt-py/docs/lewitt-corpus/wall_drawing_corpus.csv')