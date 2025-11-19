# pip install pytest

import pytest
from Function import is_even_number

def test_valid():
    assert is_even_number(2)
    assert is_even_number(4)

def test_invalid():
    assert is_even_number(1) is False
    assert is_even_number(3) is False

def test_edge_cases():
    assert is_even_number(0) is True
    assert is_even_number(-2) is True
    assert is_even_number(-3) is False
    assert is_even_number(10**6) is True

def test_error():
    with pytest.raises(ValueError):
        is_even_number("2")

    with pytest.raises(ValueError):
        is_even_number(1.5)

    with pytest.raises(ValueError):
        is_even_number(True)

    with pytest.raises(ValueError):
        is_even_number(())

    with pytest.raises(ValueError):
        is_even_number({2})

    with pytest.raises(ValueError):
        is_even_number([3])

@pytest.mark.parametrize("value, expected", [
    (0, True),
    (2, True),
    (3, False),
    (10**6, True),
    (-5, False),
])
def test_even_param(value, expected):
    assert is_even_number(value) is expected
