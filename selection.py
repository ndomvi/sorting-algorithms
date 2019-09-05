def selection_sort(arr):
    """Sorts an array using selection sort algorithm"""
    for last_sorted in arr:
        min_index = None  # index of the smallest element in the array
        for i, num in enumerate(arr[last_sorted:]):
            if min_index == None or num < arr[min_index]:
                min_index = last_sorted + i
            arr[last_sorted], arr[min_index] = arr[min_index], arr[last_sorted]

    return arr
