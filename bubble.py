def bubble_sort(arr):
    """Sorts an array using bubble sort algorithm"""
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                sorted = False
    return arr
