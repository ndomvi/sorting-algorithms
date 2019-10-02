from pytest import fixture
from generator import generate_array

from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort
from merge import merge_sort
from quick import quick_sort


@fixture(scope='function')
def array():
    return generate_array()


def test_bubble_sort(array):
    """Checks that returned array is the same as result of sorted()"""
    assert sorted(array) == bubble_sort(array)


def test_selection_sort(array):
    """Checks that returned array is the same as result of sorted()"""
    assert sorted(array) == selection_sort(array)


def test_insertion_sort(array):
    """Checks that returned array is the same as result of sorted()"""
    assert sorted(array) == insertion_sort(array)


def test_merge_sort(array):
    """Checks that returned array is the same as result of sorted()"""
    assert sorted(array) == merge_sort(array)


def test_quick_sort(array):
    """Checks that returned array is the same as result of sorted()"""
    assert sorted(array) == quick_sort(array)
