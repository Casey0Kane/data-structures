"""This module creates a linked list data structure."""


class Node(object):
    """Node data structure."""

    def __init__(self, value=None, next_node=None):
        """Initalize a node."""
        self.value = value
        self.next_node = next_node


class LinkedList(object):
    """Linked list data Structure."""

    def __init__(self, iterable=None):
        """Initalize a linked list."""
        self.head = None
        self.length = 0
        try:
            for element in iterable:
                self.push(element)
        except TypeError:
            self.head = iterable

    def push(self, val):
        """Add item to linked list."""
        self.length += 1
        new_node = Node(val, self.head)
        self.head = new_node

    def pop(self):
        """Remove item from head and return value."""
        if self.head is None:
            raise IndexError("Cannot pop from an empty linked list.")
        first = self.head.value
        self.head = self.head.next_node
        self.length -= 1
        return first

    def size(self):
        """Return length."""
        return self.length

    def search(self, val):
        """Find value in list and return node."""
        check = self.head
        while check is not None:
            print(check.value)
            if check.value == val:
                return check
            else:
                check = check.next_node
        return None

    def remove(self, node):
        """Remove node from list."""
        check = self.head
        while hasattr(check, 'next_node') and check.next_node is not node:
            check = check.next_node
            if not hasattr(check, 'next_node'):
                raise ValueError("Can not remove node, not found.")
        try:
            check.next_node = check.next_node.next_node
            self.length -= 1
        except AttributeError:
            raise ValueError("Can not remove node, not found.")

    def display(self):
        """Return to list appearing string."""
        string = '('
        head = self.head
        while head is not None:
            string += str(head.value) + ', '
            head = head.next_node
        string = string[:-2] + ')'
        return string

    def __len__(self):
        """Return the length."""
        return self.size()

    def __repr__(self):
        """Print it out."""
        return self.display()
