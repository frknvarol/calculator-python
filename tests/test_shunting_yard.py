import pytest
import source.calculator as calcualtor


def test_calculator(string: str):
    assert calcualtor.calculate(string) == eval(string)