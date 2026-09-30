from hypothesis import given, strategies as st
from app import add, total

def test_add():
    assert add(2, 3) == 5

def test_total():
    assert total([1, 2, 3]) == 6

@given(st.integers(), st.integers())
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)
