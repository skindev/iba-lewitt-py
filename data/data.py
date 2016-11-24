from abc import ABCMeta


class Data(metaclass=ABCMeta):
    """
    Data/Corpus Abstract Base Class.
    """

    def get_instruction(self, drawing_list):
        """
        Get drawing instruction(s)

        :param drawing_list:    list of drawing title(s)
        :return:                instruction(s)
        """

        # assert(drawing_list, isinstance(drawing_list, 'list'))
