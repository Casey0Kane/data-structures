"""Test Module for Bubble sort."""
import pytest
from quick_sort import quick_sort
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
    return [randint(-100, 100000) for _ in range(1000)]


def test_empty_list_returns_empty_list():
    """Empty list retruns None."""
    assert quick_sort([]) == []


def test_quick_sorts(long_and_large):
    """Test bubble sorts a long large list."""
    result = quick_sort(long_and_large)
    long_and_large.sort()
    assert long_and_large == result


def test_quick_sorts_short(short_list):
    """Test bubble sort on short list."""
    result = quick_sort(short_list)
    short_list.sort()
    assert result == short_list


def test_quick_sort_perfectly_backwards_list(sorted_list):
    """Test with sorted list."""
    result = quick_sort(sorted_list)
    sorted_list.sort()
    assert result == sorted_list


def test_quick_sorted_perfectly_forward_list(sorted_list):
    """Test best case."""
    result = quick_sort(sorted_list[::-1])
    sorted_list.sort()
    assert result == sorted_list


def test_quick_sorted_multiple_duplicates(short_list):
    """Test best case."""
    result = quick_sort(short_list[::-1] + short_list)
    short_list += short_list
    short_list.sort()
    assert result == short_list


def test_quicks():
    """Another quick test."""
    sorted_list = [99, 22, 55, 4, 66, 87, 23, 11]
    sorted_list.sort()
    assert quick_sort([99, 22, 55, 4, 66, 87, 23, 11]) == sorted_list


def test_odd_list():
    """Making sure the quick sort works with an odd list."""
    numbers = [17, 11, 14, 99, 20]
    assert quick_sort(numbers) == sorted(numbers)


def test_single_item_in_list():
    """When there is only one value, what will it do."""
    assert quick_sort([1]) == [1]
