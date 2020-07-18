from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """Sorts an array using bubble sort algorithm.
    It compares two adjacent variables and swaps them if needed.
    Exits when no swaps were done(and thus the array is sorted).
    """
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                sorted = False
    return arr
