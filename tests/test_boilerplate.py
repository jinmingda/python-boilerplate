"""Tests for module boilerplate.py."""
import pytest
from hypothesis import given
from hypothesis import strategies as st

from boilerplate.boilerplate import add


@pytest.mark.parametrize(
    "x,y,expected", [(1, 2, 3), (-1, -2, -3), (0, 0, 0), (1, -1, 0)]
)
def test_add_with_integers(x, y, expected):
    assert add(x, y) == expected


@given(x=st.integers(), y=st.integers())
def test_add_is_commutative(x, y):
    assert add(x, y) == add(y, x)
