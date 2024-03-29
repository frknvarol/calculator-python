import pytest
import source.shunting_yard as shunting_yard

def test_shunting_yard():
    result = shunting_yard.infix_to_postfix('4+18/(9-3)')
    assert result == ['4', '18', '9', '3', '-', '/', '+']