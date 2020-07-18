from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """Sorts an array using selection sort algorithm.
    It is similar to Bubble sort, but finds smallest element and swaps it with
    current first unsorted element.
    """
    for last_sorted, _ in enumerate(arr):
        min_index = last_sorted  # index of the smallest element in the array
        for i, num in enumerate(arr[last_sorted:]):
            if num < arr[min_index]:
                min_index = last_sorted + i
        arr[last_sorted], arr[min_index] = arr[min_index], arr[last_sorted]

    return arr


def selection_sort_pythonic(arr: List[int]) -> List[int]:
    """Speeded up version of the sort by using more built-in features of Python.
        Benchmarks show about 4x the speed of 'normal' sort.
    """
    for i, _ in enumerate(arr):
        # TODO find out why is it necessary to store min index in a variable
        min_index = arr.index(min(arr[i:]), i)
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def selection_sort_oneline(arr: List[int]) -> List[int]:
    """Selection sort implemented in one line.
        Speed is the same as selection_sort_pythonic().
    """
    return [arr.pop(arr.index(min(arr))) for _ in range(len(arr))]
