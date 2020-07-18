from pytest import fixture
from typing import List
from generator import generate_array

from bubble import bubble_sort
from insertion import insertion_sort
from merge import merge_sort
from quick import quick_sort, quick_sort_inplace
from selection import selection_sort


@fixture(scope='function')
def array() -> List[int]:
    return generate_array()


def test_bubble_sort(array: List[int]):
    """Checks that returned array is the same as result of sorted()"""
    assert sorted(array) == bubble_sort(array)


def test_insertion_sort(array: List[int]):
    """Checks that returned array is the same as result of sorted()"""
    assert sorted(array) == insertion_sort(array)


def test_merge_sort(array: List[int]):
    """Checks that returned array is the same as result of sorted()"""
    assert sorted(array) == merge_sort(array)


def test_quick_sort(array: List[int]):
    """Checks that returned array is the same as result of sorted()"""
    assert sorted(array) == quick_sort(array)


def test_quick_sort_inplace(array: List[int]):
    """Checks that returned array is the same as result of sorted()"""
    sorted_array = array.copy()
    quick_sort_inplace(sorted_array)
    assert sorted(array) == sorted_array


def test_selection_sort(array: List[int]):
    """Checks that returned array is the same as result of sorted()"""
    assert sorted(array) == selection_sort(array)
