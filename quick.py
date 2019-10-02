def quick_sort(arr):
    """Sorts an array by using quick sort algorithm.
    It chooses pivot from the array and compares elements against it, splitting
    it into two arrays(smaller and larger). Then, recursively sorts the arrays.
    """
    if len(arr) < 2:
        return arr

    smaller, equal, larger = [], [], []
    pivot = arr[len(arr)//2]

    for i in arr:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            larger.append(i)
        else:
            equal.append(i)

    return quick_sort(smaller)+equal+quick_sort(larger)
