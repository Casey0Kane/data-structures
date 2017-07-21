"""Insertion sort data structure implementation."""


def insertion_sort(numbers):
    """Sort with insertion."""
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
    return numbers


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'insertion_sort([x for x in range(100)])',
        "from __main__ import insertion_sort"
    )
    worst = Timer(
        'insertion_sort([x for x in range(100)][::-1])',
        "from __main__ import insertion_sort; from random import randint"
    )
    print("""
Insertion sort is a simple sorting algorithm that builds the final sorted
array ist one item at a time. It is much less efficient on large lists than
more advanced algorithms such as quicksort, heapsort, or merge sort.
""")
    print("#================= best case search 10000x ==============#")
    print(best.timeit(number=1000))
    print('')
    print("#================= worse case search 10000x==============#")
    print(worst.timeit(number=1000))
    print('')
