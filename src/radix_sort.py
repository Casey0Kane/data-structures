"""Radix Sort Implementation."""


def radix_sort(numbers):
    """Sort some numbers."""
    modulus = 10
    divisor = 1
    while True:
        keepgoing = False
        container = [list() for _ in range(10)]
        for num in numbers:
            idx = int(num % modulus / divisor)
            container[idx].append(num)
            if num >= modulus * 10:
                keepgoing = True
        divisor, modulus = modulus, modulus * 10
        if not keepgoing and len(container[0]) == len(numbers):
            return container[0]
        numbers = []
        for numerals in container:
            for num in numerals:
                numbers.append(num)


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'radix_sort([x for x in range(100)])',
        "from __main__ import radix_sort"
    )
    worst = Timer(
        'radix_sort([x for x in range(100)][::-1])',
        "from __main__ import radix_sort; from random import randint"
    )
    print("""
Quicksort (sometimes called partition-exchange sort) is an efficient sorting
algorithm, serving as a systematic method for placing the elements of an
array in order.
""")
    print("#================= best case search 10000x ==============#")
    print(best.timeit(number=1000))
    print('')
    print("#================= worse case search 10000x==============#")
    print(worst.timeit(number=1000))
    print('')
