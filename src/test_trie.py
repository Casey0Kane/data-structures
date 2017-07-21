"""Test module for trie data structure."""
import os
import pytest
from trie import Trie


@pytest.fixture
def trie():
    """Create empty tree for fixture."""
    return Trie()


@pytest.fixture
def simple(trie):
    r"""Test Simple Trie.

         trie
        /    \
       a      d
       |      |
       b      e
      / \     |
     c   $    f
     |        |
     $        $

    Simple.
    """
    trie.insert('abc')
    trie.insert('ab')
    trie.insert('def')
    return trie


def test_insert_one_char_string(trie):
    """Test trie handles one char string."""
    trie.insert('a')
    assert trie.size() == 1
    assert list(trie.keys()) == ['a']
    assert trie['a'] == {'$': None}


def test_insert_two_words_the_same_char(trie):
    """Test trie handles one char string."""
    trie.insert('a')
    assert trie.size() == 1
    assert list(trie.keys()) == ['a']
    assert trie['a'] == {'$': None}
    trie.insert('aa')
    assert trie.size() == 2
    assert list(trie.keys()) == ['a']
    assert trie['a'] == {'$': None, 'a': {'$': None}}


def test_insert_inserts_new_string(trie):
    """Test insert adds new string."""
    trie.insert('abc')
    assert trie.contains('abc') is True
    assert list(trie.keys())[0] == 'a'
    assert list(trie['a'].keys())[0] == 'b'
    assert list(trie['a']['b'].keys())[0] == 'c'
    assert '$' in trie['a']['b']['c']


def test_insert_ignors_duplicate_string(trie):
    """Test insert doesn't add duplicate string."""
    trie.insert('abc')
    with pytest.raises(IndexError):
        list(trie.keys())[1]


def test_insert_raises_TypeError_with_invalid_value(trie):
    """Test raises TypeError."""
    with pytest.raises(TypeError):
        trie.insert('abc$')
    with pytest.raises(TypeError):
        trie.insert(1)
    with pytest.raises(TypeError):
        trie.insert('')


def test_contains_True_if_value_in_trie(trie):
    """Test contains True is value present."""
    trie.insert('abc')
    assert trie.contains('abc') is True


def test_contains_False_if_value_not_in_trie(trie):
    """Test contains False is value not in trie."""
    trie.insert('abc')
    assert trie.contains('not') is False


def test_contains_False_if_value_doesnt_end_with_termination_char(trie):
    """Test contains False without terminator."""
    trie.insert('abc')
    assert trie.contains('ab') is False


def test_size_increases_with_insert(trie):
    """Test trie increase with insert."""
    assert trie.size() == 0
    trie.insert('abc')
    assert trie.size() == 1


def test_size_does_not_increase_with_attempt_to_add_duplicate(trie):
    """Test size doesn't increase with duplicate insert."""
    trie.insert('abc')
    trie.insert('ab')
    assert trie.size() == 2
    trie.insert('abc')
    assert trie.size() == 2


def test_size_decrease_on_remove(trie):
    """Test remove decreases size."""
    trie.insert('abc')
    trie.insert('def')
    assert trie.size() == 2
    trie.remove('abc')
    assert trie.size() == 1


def test_size_doesnt_decrease_if_item_not_found(trie):
    """Test size doesn't decrease if value not in trie."""
    trie.insert('abc')
    trie.insert('def')
    assert trie.size() == 2
    with pytest.raises(KeyError):
        trie.remove('not in tree')
    assert trie.size() == 2


def test_remove_removes_value_from_trie(trie):
    """Test removes value from trie."""
    trie.insert('abc')
    trie.insert('def')
    trie.remove('abc')
    assert not trie.contains('abc')
    assert trie.size() == 1
    assert 'a' not in trie.keys()


def test_remove_removes_only_terminator_when_the_rest_should_remain(simple):
    """Test removes teminator leaving other when required.

    Remove 'ab', 'abc' should remain.
    """
    assert simple.size() == 3
    assert '$' in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert '$' in simple['d']['e']['f']
    simple.remove('ab')
    assert simple.size() == 2
    assert '$' not in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert '$' in simple['d']['e']['f']


def test_remove_repeated_remove_raises_key_error(simple):
    """Test removes teminator leaving other when required.

    Remove 'ab', 'abc' should remain.
    """
    assert simple.size() == 3
    assert '$' in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert '$' in simple['d']['e']['f']
    simple.remove('ab')
    assert simple.size() == 2
    assert '$' not in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert '$' in simple['d']['e']['f']
    with pytest.raises(KeyError):
        simple.remove('ab')
    assert '$' in simple['a']['b']['c']


def test_remove_branch_from_trie(simple):
    """Test remove branch."""
    assert simple.size() == 3
    assert '$' in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert '$' in simple['d']['e']['f']
    simple.remove('abc')
    assert simple.size() == 2
    assert '$' in simple['a']['b']
    assert 'c' not in simple['a']['b']
    assert '$' in simple['d']['e']['f']


def test_remove_branch_from_root_of_trie(simple):
    """Test remove branch."""
    assert simple.size() == 3
    assert '$' in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert '$' in simple['d']['e']['f']
    simple.remove('def')
    assert simple.size() == 2
    assert '$' in simple['a']['b']
    assert '$' in simple['a']['b']['c']
    assert 'd' not in simple


def test_word_traverse_two_suffixes(simple):
    """Test simple depth first."""
    assert tuple(simple.word_traverse('a')) in (
        ('ab', 'abc'),
        ('abc', 'ab')
    )


def test_word_traverse_two_suffixes_comlete_word(simple):
    """Test simple depth first."""
    assert tuple(simple.word_traverse('ab')) in (
        ('ab', 'abc'),
        ('abc', 'ab')
    )


def test_word_traverse_one_suffix(simple):
    """Test simple depth first."""
    assert next(simple.word_traverse('d')) == 'def'


def test_word_traverse_value_not_in_trie(simple):
    """Test value not in trie."""
    with pytest.raises(KeyError):
        next(simple.word_traverse('test'))


def test_traverse_on_short_trie_0_0(simple):
    """Test should return chars."""
    assert tuple(simple.traverse('a')) == ('a', 'b', 'c')


def test_traverse_on_short_trie_0_1(simple):
    """Test should return chars."""
    assert tuple(simple.traverse('d')) == ('d', 'e', 'f')


def test_traverse_on_short_trie_0_3(simple):
    """Test should return charss."""
    assert tuple(simple.traverse('de')) == ('d', 'e', 'f')


def test_traverse_on_short_trie_0_4(simple):
    """Test should return charss."""
    assert tuple(simple.traverse('ab')) == ('a', 'b', 'c')


def test_traverse_on_short_value_not_in_trie(simple):
    """Test should return charss."""
    with pytest.raises(KeyError):
        next(simple.traverse('xyzzy'))


# ========== Short Test Fixture ============== @

def populate_short_words():
    """Populate our words set."""
    words = set()
    dictfile = "/src/test/short_words"
    path = os.getcwd() + dictfile
    with open(path, 'r') as words_file:
        for line in words_file:
            words.add(line[:-1].lower())
    return words


SHORT_WORDS = populate_short_words()


@pytest.fixture
def short(trie):
    """Large Trie."""
    for word in SHORT_WORDS:
        trie.insert(word)
    return trie


def test_short_trie_handles_remove(short):
    """Test large trie remove."""
    assert short.size() == len(SHORT_WORDS)
    short.remove('a')
    assert not short.contains('a')
    assert short.size() == len(SHORT_WORDS) - 1
    assert '$' not in short['a'].keys()
    with pytest.raises(KeyError):
        short.remove('a')


def test_word_traverse_on_short_trie_empty_strng(short):
    """Test should return entire set of words."""
    results = tuple(short.word_traverse(''))
    for word in SHORT_WORDS:
        assert word in results


# ===================== Large Test ===================== #

def populate_words():
    """Populate our words set."""
    words = set()
    dictfile = "/src/test/words"
    path = os.getcwd() + dictfile
    with open(path, 'r') as words_file:
        for line in words_file:
            words.add(line[:-1].lower())
    return words


WORDS = list(populate_words())


def random_words_to_remove():
    """Create set of random words to remove."""
    import random
    words_to_remove = set()
    for _ in range(10000):
        words_to_remove.add(random.choice(WORDS))
    return words_to_remove


WORDS_TO_REMOVE = list(random_words_to_remove())


@pytest.fixture
def large(trie):
    """Large Trie."""
    for word in WORDS:
        trie.insert(word)
    return trie


def test_large_trie_handles_remove(large):
    """Test large trie remove."""
    assert large.size() == len(WORDS)
    large.remove('apple')
    assert not large.contains('apple')
    assert large.size() == len(WORDS) - 1


def test_remove_random_words(large):
    """Test random removals."""
    length = len(WORDS)
    assert large.size() == length
    for word in WORDS_TO_REMOVE:
        large.remove(word)
        length -= 1
        assert not large.contains(word)
        assert large.size() == length
        with pytest.raises(KeyError):
            large.remove(word)


def test_word_traverse_on_large_trie(large):
    """Test on large trie."""
    a_letter_words = [
        word for word in WORDS if word[0] == 'a'
    ]
    results = tuple(large.word_traverse('a'))
    for word in results:
        assert word in a_letter_words
    for word in a_letter_words:
        assert word in results


def test_word_traverse_on_large_trie_0_1(large):
    """Test on large tire."""
    a_letter_words = [
        word for word in WORDS if len(word) > 1 and
        word[0] == 'd' and word[1] == 'e'
    ]
    results = tuple(large.word_traverse('de'))
    for word in results:
        assert word in a_letter_words
    for word in a_letter_words:
        assert word in results
    for word in results:
        large.remove(word)
    assert large.size() == len(WORDS) - len(results)
    for word in results:
        with pytest.raises(KeyError):
            large.remove(word)


def test_traverse_on_large_trie_0_0(large):
    """Test should return charss."""
    assert tuple(large.traverse('aard')) in (
        ('a', 'a', 'r', 'd', 'v', 'a', 'r', 'k', 'w', 'o', 'l', 'f'),
        ('a', 'a', 'r', 'd', 'w', 'o', 'l', 'f', 'v', 'a', 'r', 'k')
    )
