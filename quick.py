from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    """Sorts an array by using quick sort algorithm.
    It chooses pivot from the array and compares elements against it, splitting
    it into two arrays(smaller and larger). Then, recursively sorts the arrays.
    """
    if len(arr) < 2:
        return arr

    smaller, equal, larger = [], [], []
    pivot = arr[len(arr) // 2]

    for i in arr:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            larger.append(i)
        else:
            equal.append(i)

    return quick_sort(smaller) + equal + quick_sort(larger)


def partition(arr: List[int], low: int, high: int) -> int:
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort_inplace(arr: List[int], low: int = 0, high: int = None) -> None:
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index-1)
        quick_sort_inplace(arr, pivot_index+1, high)
