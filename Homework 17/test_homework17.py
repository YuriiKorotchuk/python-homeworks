import unittest
import game_class
import custom_exceptions


class TestDiceGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.joker = game_class.Game()

    def test_default_score(self):
        self.assertEqual(self.joker.dices[0].scores, 1)

    def test_set_score(self):
        self.joker.dices[0].set_scores(5)
        self.assertEqual(self.joker.dices[0].scores, 5)

    def test_simple_game(self):
        self.assertEqual(self.joker.throw(1, 4, 6), 11)

    def test_three_same_variable(self):
        self.assertEqual(self.joker.throw(6, 6, 6), 600)

    def test_first_another_variable(self):
        self.assertEqual(self.joker.throw(6, 5, 6), 60)

    def test_second_another_variable(self):
        self.assertEqual(self.joker.throw(3, 5, 5), 50)

    def test_zero_exception(self):
        with self.assertRaises(custom_exceptions.DiceZeroError):
            self.joker.throw(0, 0, 2)

    def test_negatives_exception(self):
        with self.assertRaises(custom_exceptions.DiceNegativeError):
            self.joker.throw(1, -2, 2)

    def test_type_exception(self):
        with self.assertRaises(custom_exceptions.DiceTypeError):
            self.joker.throw(1, "5.22", 2)

    def test_range_exception(self):
        with self.assertRaises(custom_exceptions.DiceRangeError):
            self.joker.throw(1, 7, 2)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
