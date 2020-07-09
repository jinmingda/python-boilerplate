"""Tests for module boilerplate.py."""
import pytest

from boilerplate.boilerplate import add


@pytest.mark.parametrize(
    "x,y,expected", [(1, 2, 3), (-1, -2, -3), (0, 0, 0), (1, -1, 0)]
)
def test_add_with_integers(x, y, expected):
    assert add(x, y) == expected
