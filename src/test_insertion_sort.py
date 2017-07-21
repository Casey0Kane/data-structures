"""Test Module for insertion sort."""
from insertion_sort import insertion_sort
import pytest
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
    assert insertion_sort([]) == []


def test_insertion_sorts(long_and_large):
    """Test insertion sorts a long large list."""
    result = insertion_sort(long_and_large)
    long_and_large.sort()
    assert long_and_large == result


def test_insertion_sorts_short(short_list):
    """Test insertion sort on short list."""
    result = insertion_sort(short_list)
    short_list.sort()
    assert result == short_list


def test_insertion_sort_perfectly_backwards_list(sorted_list):
    """Test with sorted list."""
    result = insertion_sort(sorted_list)
    sorted_list.sort()
    assert result == sorted_list


def test_insertion_sorted_perfectly_forward_list(sorted_list):
    """Test best case."""
    result = insertion_sort(sorted_list[::-1])
    sorted_list.sort()
    assert result == sorted_list


def test_insertion_sorted_multiple_duplicates(short_list):
    """Test best case."""
    result = insertion_sort(short_list[::-1] + short_list)
    short_list += short_list
    short_list.sort()
    assert result == short_list


def test_insertions():
    """Another quick test."""
    sorted_list = [99, 22, 55, 4, 66, 87, 23, 11]
    sorted_list.sort()
    assert insertion_sort([99, 22, 55, 4, 66, 87, 23, 11]) == sorted_list
