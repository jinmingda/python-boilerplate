"""Tests for module boilerplate.py."""
from boilerplate.boilerplate import add


def test_add_with_integers():
    assert add(1, 2) == 3
