"""Merge sort data structure implementation."""


def quick_sort(numbers):
    """Recursively split list and returns quickd list."""
    if len(numbers) <= 1:
        return numbers
    left, right = [], []
    for num in numbers[1:]:
        if num < numbers[0]:
            left.append(num)
        else:
            right.append(num)
    return quick_sort(left) + [numbers[0]] + quick_sort(right)

if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'quick_sort([x for x in range(100)])',
        "from __main__ import quick_sort"
    )
    worst = Timer(
        'quick_sort([x for x in range(100)][::-1])',
        "from __main__ import quick_sort; from random import randint"
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
