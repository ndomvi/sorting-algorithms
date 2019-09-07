from timeit import timeit
from generator import generate_array


def benchmark(n=[1, 10, 100, 1000]):
    """Prints times taken by different sorting algorithms.\n
        n is list of lengths of arrays that will be used to benchmark.
    """

    # TODO find why do we need 2 spaces before '\tSelection'
    print('n \tBuilt-in \tBubble  \tSelection')

    for length in n:
        array = generate_array(n=length)

        time_sort = timeit(
            f'sorted({array})', number=10)

        time_bubble = timeit(
            f"bubble_sort({array})", setup="from bubble import bubble_sort", number=10)

        time_selection = timeit(
            f"selection_sort({array})", setup="from selection import selection_sort", number=10)

        print(f'{length}', end='')

        print(f' \t{time_sort:.5f}', end='')
        print(f' \t{time_bubble:.5f}', end='')
        print(f' \t{time_selection:.5f}', end='')

        print()


benchmark()
