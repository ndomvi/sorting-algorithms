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
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort_inplace(arr: List[int], low: int = 0, high: int = None) -> None:
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index-1)
        quick_sort_inplace(arr, pivot_index+1, high)
