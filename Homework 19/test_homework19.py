import game_class
import pytest
import custom_exceptions


@pytest.fixture()
def new_game():
    return game_class.Game()


@pytest.mark.parametrize("first, second, third, scores", [(2, 1, 5, 8),
                                                          (5, 5, 5, 500),
                                                          (3, 3, 2, 30),
                                                          (1, 6, 6, 60)])
def test_variations(new_game, first, second, third, scores):
    assert new_game.throw(first, second, third) == scores


@pytest.mark.parametrize("first, second, third, exception", [(6, 6, 0, custom_exceptions.DiceZeroError),
                                                             (-5, 3, 2, custom_exceptions.DiceNegativeError),
                                                             (2, 9, 2, custom_exceptions.DiceRangeError),
                                                             (4, 4.4, 1, custom_exceptions.DiceTypeError)])
def test_exceptions(new_game, first, second, third, exception):
    with pytest.raises(exception):
        new_game.throw(first, second, third)
