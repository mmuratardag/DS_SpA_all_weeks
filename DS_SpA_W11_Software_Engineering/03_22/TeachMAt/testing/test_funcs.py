from funcs import add_one, recommend_movie, first_letter
import pytest


EXAMPLE =[(5, 6), (0, 1), (-5, -4), (10000, 10001)]   # pairs of (input, expected output)

@pytest.mark.parametrize(['inp', 'exp_out'], EXAMPLE)   # decorator that adds functionality to the function below
def test_add_one(inp, exp_out):
    assert add_one(inp) == exp_out


def test_recommend_movie():
    result = recommend_movie(['Star Wars', 'Toy Story', 'Night on Earth'])
    assert isinstance(result, str)
    assert result.isupper()   # only in the same function because if the assert above fails, this will also fail.

def test_wrong_input_first_letter():  # check if the error is raised
    with pytest.raises(TypeError):
        first_letter(5)