from random import randint


def generate_array(max=100, n=15):
    """Generates an array of N random numbers ranged from 0 to MAX
    """
    return [randint(0, max) for _ in range(n)]
