"""Test Module for Bubble sort."""
import pytest
from radix_sort import radix_sort
from random import randint


@pytest.fixture
def short_list():
    """Create short list."""
    return [randint(1, 1000) for _ in range(100)]


@pytest.fixture
def sorted_list():
    """Create short list."""
    return [x for x in range(100)]


@pytest.fixture
def long_and_large():
    """Create long list."""
    return [randint(1, 100000) for _ in range(1000)]


def test_empty_list_returns_empty_list():
    """Empty list retruns None."""
    assert radix_sort([]) == []


def test_radix_sorts(long_and_large):
    """Test radix_sorts a long large list."""
    result = radix_sort(long_and_large)
    long_and_large.sort()
    assert long_and_large == result


def test_radix_sorts_short(short_list):
    """Test radix_sort on short list."""
    result = radix_sort(short_list)
    short_list.sort()
    assert result == short_list


def test_radix_sort_perfectly_backwards_list(sorted_list):
    """Test with sorted list."""
    result = radix_sort(sorted_list)
    sorted_list.sort()
    assert result == sorted_list


def test_radix_sorted_perfectly_forward_list(sorted_list):
    """Test best case."""
    result = radix_sort(sorted_list[::-1])
    sorted_list.sort()
    assert result == sorted_list


def test_radix_sorted_multiple_duplicates(short_list):
    """Test best case."""
    result = radix_sort(short_list[::-1] + short_list)
    short_list += short_list
    short_list.sort()
    assert result == short_list


def test_radixs():
    """Another radix test."""
    sorted_list = [99, 22, 55, 4, 66, 87, 23, 11]
    sorted_list.sort()
    assert radix_sort([99, 22, 55, 4, 66, 87, 23, 11]) == sorted_list


def test_radixs_0_1():
    """Another radix test."""
    sorted_list = [11, 1, 11, 11, 11, 11, 11]
    sorted_list.sort()
    assert radix_sort([11, 11, 11, 11, 11, 11, 1]) == sorted_list


def test_odd_list():
    """Making sure the radix sort works with an odd list."""
    numbers = [17, 11, 14, 99, 20]
    assert radix_sort(numbers) == sorted(numbers)


def test_single_item_in_list():
    """When there is only one value, what will it do."""
    assert radix_sort([1]) == [1]


def test_all_zeros_in_ones_place():
    """Handels zeros in ones place."""
    assert radix_sort([110, 10, 20, 150]) == [10, 20, 110, 150]
