"""Implementation of hash table data structure."""


class HashTable(object):
    """Hash class for data structure."""

    def __init__(self, size=17, func=None):
        """Initialize the hash."""
        self._table = [[] for x in range(size)]
        if not func:
            func = naive
        self._hash = func  # <-------This is the _hash method.

    def get(self, key):
        """Return the value stored at hash of given key."""
        hash_val = self._hash(key) % len(self._table)
        for item in self._table[hash_val]:
            if item[0] == key:
                return item[1]

    def set(self, key, val):
        """Store value based on given key."""
        hash_val = self._hash(key) % len(self._table)
        for item in self._table[hash_val]:
            if item[0] == key:
                item[1] = val
                return
        self._table[hash_val].append([key, val])


def naive(key):
    """Additive hashing method."""
    base = 0
    for char in key:
        base += ord(char)
    return base


def optimus_prime_hash(key):
    """The most optimal hashing obviously."""
    base = ""
    for char in key:
        base += str(ord(char))
    base = int(base) * 4001
    return base
