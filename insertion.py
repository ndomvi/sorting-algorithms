def insertion_sort(arr):
    """Sorts an array using insertion sort algorithm"""
    for index, val in enumerate(arr):
        while index > 0 and arr[index-1] > val:
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = val

    return arr
