"""Module tests binheap."""
import pytest


@pytest.fixture
def binheap_empty():
    """Create a binary heap."""
    from binheap import Binheap
    return Binheap()


@pytest.fixture
def binheap_five_rand_num():
    """Create a binary heap 5 random numbers."""
    from binheap import Binheap
    return Binheap([5, 4, 1, 3, 2])


@pytest.fixture
def binheap_100_rand():
    """Random 100 fixture."""
    from binheap import Binheap
    from random import randint
    heap = Binheap([randint(1, 1000) for _ in range(100)])
    return heap


def test_pop_removes_smallest_num(binheap_five_rand_num):
    """Return lowest."""
    assert binheap_five_rand_num.pop() == 1
    assert binheap_five_rand_num.pop() == 2
    assert binheap_five_rand_num.pop() == 3
    assert binheap_five_rand_num.pop() == 4
    assert binheap_five_rand_num.pop() == 5


def test_pop_empty_heap_returns_None(binheap_empty):
    """Pop returns None on empty heap."""
    assert binheap_empty.pop() is None


def test_push_to_empty_heap_increases_heap_length(binheap_empty):
    """Push increases heap length."""
    binheap_empty.push(1)
    assert len(binheap_empty) == 1


def test_push_smaller_num_to_heap_changes_order_of_heap(binheap_five_rand_num):
    """Push smaller num changes order os heap."""
    binheap_five_rand_num.push(0)
    assert binheap_five_rand_num.pop() == 0


def test_heap_rand_100_placed_in_order(binheap_100_rand):
    """Random 100 in order."""
    for index, num in enumerate(binheap_100_rand):
        if index * 2 + 1 <= len(binheap_100_rand) - 1:
            assert num < binheap_100_rand[index * 2 + 1]
        if index * 2 + 2 <= len(binheap_100_rand) - 1:
            assert num < binheap_100_rand[index * 2 + 2]


def test_heap_rand_100_remove_retains_correct_order(binheap_100_rand):
    """Random 100 in order."""
    binheap_100_rand.pop()
    binheap_100_rand.pop()
    for index, num in enumerate(binheap_100_rand):
        if index * 2 + 1 <= len(binheap_100_rand) - 1:
            assert num < binheap_100_rand[index * 2 + 1]
        if index * 2 + 2 <= len(binheap_100_rand) - 1:
            assert num < binheap_100_rand[index * 2 + 2]


def test_heap_rand_100_removes_in_order(binheap_100_rand):
    """Remove in order."""
    temp_a = binheap_100_rand.pop()
    temp_b = binheap_100_rand.pop()
    for _ in range(len(binheap_100_rand) - 1):
        assert temp_a < temp_b
        temp_a, temp_b = temp_b, binheap_100_rand.pop()


def test_heap_handles_push_pops_with_correct_ordering():
    """Pop out in correct order."""
    from binheap import Binheap
    heap = Binheap([3, 5, 6, 2, 7, 8, 1, 0, 0, 10])
    assert heap.__repr__() == '[0, 1, 2, 3, 7, 8, 6, 5, 10]'
    assert heap.pop() == 0
    assert heap.__repr__() == '[1, 3, 2, 5, 7, 8, 6, 10]'


def test_initalizing_with_non_iterable_or_not_numbers_raises_ValueError():
    """Value Error on non iterable or number."""
    from binheap import Binheap
    with pytest.raises(TypeError):
        Binheap("dfsdfadgasdg")
