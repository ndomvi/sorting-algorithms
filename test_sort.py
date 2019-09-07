from pytest import fixture
from generator import generate_array

from bubble import bubble_sort
from selection import selection_sort


@fixture(scope='function')
def array():
    return generate_array()


def test_bubble_sort(array):
    """Compares array sorted with bubble sort with python built-in sort"""
    assert sorted(array) == bubble_sort(array)


def test_selection_sort(array):
    """Compares array sorted with selection sort with python built-in sort"""
    assert sorted(array) == selection_sort(array)
