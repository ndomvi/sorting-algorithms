from pytest import fixture
from generator import generate_array

from bubble import bubble_sort


@fixture(scope='session')
def array():
    return generate_array()


def test_bubble_sort(array):
    assert sorted(array) == bubble_sort(array)
