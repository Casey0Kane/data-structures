"""Module implements bubble sort."""


def bubble_sort(numbers):
    """Bubble-Sort a list of numbers."""
    idx = len(numbers) - 1
    for _ in range(idx):
        change = False
        for i, num in enumerate(numbers[:-1]):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                if numbers[i + 1] is numbers[idx]:
                    idx -= 1
                change = True
        if not change:
            return numbers
    return numbers


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'bubble_sort([x for x in range(100)])',
        "from __main__ import bubble_sort"
    )
    worst = Timer(
        'bubble_sort([x for x in range(100)][::-1])',
        "from __main__ import bubble_sort; from random import randint"
    )
    print("""
Bubble sort is a simple sorting algorithm that repeatedly steps through
the list to be sorted, compares each pair of adjacent items and swaps
them if they are in the wrong order.
""")
    print("#================= best case search 10000x ==============#")
    print(best.timeit(number=1000))
    print('')
    print("#================= worse case search 10000x==============#")
    print(worst.timeit(number=1000))
    print('')
