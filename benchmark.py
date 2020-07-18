from timeit import timeit
from generator import generate_array


def benchmark(n=[1, 10, 100, 1000]):
    """Prints times taken by different sorting algorithms.\n
    n is list of lengths of arrays that will be used to benchmark.
    """

    # TODO find out WHY do we need 2 spaces before '\tSelection'
    # TODO okay, '\tQuick' needs THREE spaces to be correctly aligned.
    print('n\tBuilt-in\tBubble  \tSelection\tInsertion\tMerge   \tQuick \tQuick(in-place)')

    for length in n:
        # reuse the same array to make testing fair
        array = generate_array(n=length)

        time_sort = timeit(
            f"sorted({array})",
            number=10)

        time_bubble = timeit(
            f"sort({array})",
            setup="from bubble import bubble_sort as sort",
            number=10)

        time_selection = timeit(
            f"sort({array})",
            setup="from selection import selection_sort as sort",
            number=10)

        time_insertion = timeit(
            f"sort({array})",
            setup="from insertion import insertion_sort as sort",
            number=10)

        time_merge = timeit(
            f"sort({array})",
            setup="from merge import merge_sort as sort",
            number=10)

        time_quick = timeit(
            f"sort({array})",
            setup="from quick import quick_sort as sort",
            number=10)

        time_quick_inplace = timeit(
            f"sort({array})",
            setup="from quick import quick_sort_inplace as sort",
            number=10)

        # Print the row
        print(f'{length}', end='')

        # :.5f makes it show digits after a comma
        print(f' \t{time_sort:.5f}', end='')
        print(f' \t{time_bubble:.5f}', end='')
        print(f' \t{time_selection:.5f}', end='')
        print(f' \t{time_insertion:.5f}', end='')
        print(f' \t{time_merge:.5f}', end='')
        print(f' \t{time_quick:.5f}', end='')
        print(f' \t{time_quick_inplace:.5f}', end='')

        print()


benchmark()
