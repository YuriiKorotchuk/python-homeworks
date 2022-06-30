from homework5 import math_examples, float_transformator
import pytest


# Task 2
@pytest.mark.parametrize("firstly, expected_result", [(0, 0.0),
                                                      (2.5, 2.5),
                                                      ("25.5", 25.5),
                                                      ("Float", 0.0),
                                                      (True, 0.0),
                                                      (None, 0.0),
                                                      (("231", 1), 0.0),
                                                      ({"tryitout": False}, 0.0),
                                                      (["correct", None, 1], 0.0)])
def test_float_transformator(firstly, expected_result):
    assert float_transformator(firstly) == expected_result


# Task 3
@pytest.mark.parametrize("firstly, secondary, expected_result", [(1, 0, 1),
                                                                 (5.5, 2.1, 3.4),
                                                                 (-10, 8, -18),
                                                                 ("Слава ", "Україні", "Слава Україні"),
                                                                 ("-123", "321.2", "-123321.2"),
                                                                 ("True or ", "False", "True or False"),
                                                                 ("Road", 66, {"Road": 66}),
                                                                 ("123", 321, {"123": 321}),
                                                                 ("True", False, {"True": False}),
                                                                 (321, None, (321, None)),
                                                                 (True, 231, (True, 231)),
                                                                 (True, -321, (True, -321)),
                                                                 ((3, 2, "1"), [1, 5.2], ((3, 2, "1"), [1, 5.2])),
                                                                 ({"Task": True}, False, ({"Task": True}, False))])
def test_int_float_flow(firstly, secondary, expected_result):
    assert math_examples(firstly, secondary) == expected_result
