# Data Structures [![Build Status](https://travis-ci.org/Casey0Kane/data-structures.svg?branch=master)](https://travis-ci.org/Casey0Kane/data-structures)
This will hold sample code for a number of classic data structures implemented in Python.

## Linked List
- push(val) will insert the value ‘val’ at the head of the list
- pop() will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
- size() will return the length of the list
- search(val) will return the node containing ‘val’ in the list, if present, else None
- remove(node) will remove the given node from the list, wherever it might be (node must be an item in the list). If the node is not in the list, it should raise an exception with an appropriate message.
- display() will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”

- len(the_list) returns the size of the list
- print(the_list) returns what the display() method returns


## Stack
- push(value) - Adds a value to the stack. The parameter is the value to be added to the stack.
- pop() - Removes a value from the stack and returns that value. If the stack is empty, attempts to call pop should raise an appropriate Python exception with message.

## Doubly-Linked List

- push(val) will insert the value val at the head of the list
- append(val) will append the value val at the tail of the list
- pop() will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
- shift() will remove the last value from the tail of the list and return it. Raises an exception with an appropriate message if there are no values to return.
- remove(val) will remove the first instance of val found in the list, starting from the head. If val is not present, it will raise an appropriate Python exception.

## Binary heap

- push(val): puts a new value into the heap, maintaining the heap property.
- pop(): removes the “top” value in the heap, maintaining the heap property.

## Priority Queue
- insert(data, priority=0): Inserts value into the pqueue.
- pop(): Will pop the first priority value from the pqueue and return it, will raise an index
error if there is no values in the pqueue.
- peek(): Will take a look at the highest priority value in the pqueue but will not return it.

## Graph

- nodes(): return a list of all nodes in the graph
- edges(): return a list of all edges in the graph
- add_node(val): adds a new node with value ‘n’ to the graph
- add_edge(val1, val2): adds a new edge to the graph connecting the node containing ‘val1’ and the node containing ‘val2’. If either val1 or val2 are not already present in the graph, they should be added. If an edge already exists, overwrite it.
- del_node(val): deletes the node containing ‘val’ from the graph; raises an error if no such node exists
- del_edge(val1, val2): deletes the edge connecting ‘val1’ and ‘val2’ from the graph; raises an error if no such edge exists
- has_node(val): True if node containing ‘val’ is contained in the graph, False if not.
- neighbors(val): returns the list of all nodes connected to the node containing ‘val’ by edges; raises an error if val is not in graph.
- adjacent(val1, val2): returns True if there is an edge connecting val1 and val2, False if not; raises an error if either of the supplied values are not in graph.
- depth_first_traversal(start_val): Perform a full depth-first traversal of the graph beginning at start_val. Return the full visited path when traversal is complete.
- breadth_first_traversal(start_val): Perform a full breadth-first traversal of the graph, beginning at start_val. Return the full visited path when traversal is complete.

```python graph.py ```
Should return examples of both depth and breadth transversal

## Weighted Graph

- adds weights to each route of the graph.

## Binary Search Tree (BST)

- insert(self, val): will insert the value val into the BST. If val is already present, it will be ignored.
- search(self, val): will return the node containing that value, else None
- size(self): will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty.
- depth(self): will return an integer representing the total number of levels in the tree. If there are no values, depth is 0, if one value the depth should be 1, if two values it will be 2, if three values it may be 2 or 3, depending, etc.
- contains(self, val): will return True if val is in the BST, False if not.
- balance(self): will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.
- delete(self, val): remove val from the tree if present, if not present this method is a no-op. Return None in all cases.

Transversals on the BST [Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal)
- in_order(self): will return a generator that will return the values in the tree using in-order traversal, one at a time.
- pre_order(self): will return a generator that will return the values in the tree using pre-order traversal, one at a time.
- post_order(self): will return a generator that will return the values in the tree using post_order traversal, one at a time.
- breadth_first(self): will return a generator that will return the values in the tree using breadth-first traversal, one at a time.

## AVL Tree (self balancing - bbst)
- all the same properties of the bst above but added auto balancing. Search, should always be logN.
### Related reading and inspiration
- [Tim Rijavec's how-to-implement-avl-tree-in-python](http://blog.coder.si/2014/02/how-to-implement-avl-tree-in-python.html)
- [Geeks for geeks - avl-tree-set-2-deletion](http://www.geeksforgeeks.org/avl-tree-set-2-deletion/)

## Hash Table
- this implementation takes a size and an optional hashing function as parameters. It uses a addative hashing function by default. Very sub optimal. The file also has a better custom hashing function included - optimus_prime_hash.
- get(key) - should return the value stored with the given key - Big(O) - O(1) less collisions
- set(key, val) - should store the given val using the given key - Big(O) - O(1) less collisions
- _hash(key) - should hash the key provided (note that this is an internal api)

## Trie
- insert(string): will insert the input string into the trie. If character in the input string is already present, it will be ignored. Big(O) - O(1)
- contains(string): will return True if the string is in the trie, False if not. Big(O) - O(1)
- size(): will return the total number of words contained within the trie. 0 if empty. Big(O) - O(1)
- remove(string): will remove the given string from the trie. If the word doesn’t exist, will raise an appropriate exception. Big(O) - O(1)
- word_traverse(start_string): depth-first traversal returning all of the words in the trie tree that start with start_string. Returns a generator. Big(O) - O(1)
- treverse(start_string): depth-first traversal returning all of the characters in the trie tree that start with start_string. Returns a generator. Big(O) - O(1)

# To install
### Clone repo with ssh or https

- ssh:
```git clone git@github.com:Casey0Kane/data-structures.git```

- https:
```git clone https://github.com/Casey0Kane/data-structures.git```
- change into data-structures direrctoy
```cd data-structures```

### Install dependencies and/or those for testing

- without testing:
```pip install -e .```
- or with:
```pip install -e .[testing]```

### Runing tests
- single file where test_bbst.py is the file to run tests on.
```pytest src/test_bbst.py -v```
- all files with coverage report
```py.test -v src/ --cov=src/ --cov-report term-missing```
- to test both python 2.7 and 3.6 simply run:
```tox```
