# note to self: run these tests with `pytest test_factors.py`

from my_server import get_all_factors
import pytest

def test_composite_number():
    # Test for 12, which should return [1, 2, 2, 3]
    assert get_all_factors(12) == [1, 2, 2, 3]

def test_prime_number():
    # Test for 7, which should return [7]
    assert get_all_factors(7) == [7]
    
def test_small_number():
    # Test for 1, which should return [1]
    assert get_all_factors(1) == [1]

def test_large_composite():
    # Test for 360, which should return [1, 2, 2, 2, 3, 3, 5]
    assert get_all_factors(360) == [1, 2, 2, 2, 3, 3, 5]