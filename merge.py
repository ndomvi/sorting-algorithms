def merge(a, b):
    """Merges sorted arrays a and b by placing smallest element
    from each array into a temporary array and returning it"""
    result = []
    a_index, b_index = 0, 0

    # iterate until one of the arrays ends
    while a_index < len(a) and b_index < len(b):
        # add smallest number to resulting array
        if a[a_index] < b[b_index]:
            result.append(a[a_index])
            a_index += 1
        else:
            result.append(b[b_index])
            b_index += 1

    # check which array ended and put remaining elements from second array
    if a_index == len(a):
        result.extend(b[b_index:])
    else:
        result.extend(a[a_index:])

    return result


def merge_sort(arr):
    """Sorts an array by using merge sort algorithm.
    It splits the array in two and performs recursive sort on each of them.
    Then, it merges two sorted arrays back with merge().
    """
    # if a list contains 1 or 0 elements it doesn't need sorting
    if len(arr) < 2:
        return arr

    # split the array into two; they will be sorted afterwards
    a, b = merge_sort(arr[len(arr)//2:]), merge_sort(arr[:len(arr)//2])

    # return merged arrays a and b
    return merge(a, b)
