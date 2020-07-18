from random import randint
from typing import List


def generate_array(n: int = 15, max: int = 100) -> List[int]:
    """
    Generates an array of `N` random numbers between `0` and `MAX`
    """
    return [randint(0, max) for _ in range(n)]
