"""Merge sort data structure implementation."""


def merge(left, right):
    """Combine lists in correct order."""
    results = []
    i, j = 0, 0
    while len(results) < len(left) + len(right):
        if left[i] < right[j]:
            results += [left[i]]
            i += 1
        else:
            results += [right[j]]
            j += 1
        if i == len(left) or j == len(right):
            results += left[i:] or right[j:]
            return results


def merge_sort(numbers):
    """Recursively split list and returns merged list."""
    if len(numbers) <= 1:
        return numbers
    middle_idx = int(len(numbers) / 2)
    left = merge_sort(numbers[:middle_idx])
    right = merge_sort(numbers[middle_idx:])
    return merge(left, right)


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'merge_sort([x for x in range(100)])',
        "from __main__ import merge_sort"
    )
    worst = Timer(
        'merge_sort([x for x in range(100)][::-1])',
        "from __main__ import merge_sort; from random import randint"
    )
    print("""
Merge sort is an efficient, general-purpose,
comparison-based sorting algorithm. Most implementations
produce a stable sort, which means that the implementation
preserves the input order of equal elements in the sorted output.
Merge sort is a divide and conquer algorithm.
""")
    print("#================= best case search 10000x ==============#")
    print(best.timeit(number=1000))
    print('')
    print("#================= worse case search 10000x==============#")
    print(worst.timeit(number=1000))
    print('')
