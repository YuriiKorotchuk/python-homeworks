import custom_exceptions


class Dice(object):
    def __init__(self):
        self.__scores = 1

    @property
    def scores(self):
        return self.__scores

    def set_scores(self, num):
        if not type(num) == int:
            raise custom_exceptions.DiceTypeError
        elif num == 0:
            raise custom_exceptions.DiceZeroError
        elif num < 0:
            raise custom_exceptions.DiceNegativeError
        elif num > 6:
            raise custom_exceptions.DiceRangeError
        else:
            self.__scores = num

