from timeit import timeit
from bubble import bubble_sort
from generator import generate_array


def benchmark(n=[1, 10, 100, 1000]):
    """Prints times taken by different sorting algorithms.\n
        n is list of lengths of arrays that will be used to benchmark.
    """
    
    print('n \tBuilt-in \tBubble')

    for length in n:
        array = generate_array(n=length)

        time_sorted = timeit(
            f'sorted({array})', number=10)
        time_bubble = timeit(
            f"bubble_sort({array})", setup="from bubble import bubble_sort", number=10)

        print(f'{length} \t{time_sorted:.5f} \t{time_bubble:.5f}')


benchmark()
