"""Tests for bst module."""

import pytest


@pytest.fixture
def bst_empty():
    """Create a binary search tree."""
    from bst import Bst
    return Bst()


@pytest.fixture
def bst_left_balance():
    r"""Create a binary search tree 5 numbers snake.

                    5
                   /
                  4
                 /
                1
                 \
                  3
                 /
                2
    depth: 5
    balance: -4
    === Search Transversals ===
    in_order: (1, 2, 3, 4, 5)
    pre_order: (5, 4, 1, 3, 2)
    breadth_first: (5, 4, 1, 3, 2)
    post_order: (2, 3, 1, 4, 5)
    """
    from bst import Bst
    return Bst([5, 4, 1, 3, 2])


@pytest.fixture
def bst_balanced():
    r"""Create a binary search tree 5 numbers.

                     5
                   /   \
                  2     6
                 / \     \
                1   3     7
    depth: 3
    balance: 0
    === Search Transversals ===
    in_order: (1, 2, 3, 5, 6, 7)
    pre_order: (5, 2, 1, 3, 6, 7)
    breadth_first: (5, 2, 6, 1, 3, 7)
    post_order: (1, 3, 2, 7, 6, 5)
    """
    from bst import Bst
    return Bst([5, 6, 2, 3, 1, 7])


@pytest.fixture
def bst_right_balance():
    r"""Create a binary search tree 5 numbers.

                     5
                   /   \
                  2     8
                       / \
                      6   9
                       \
                        7
    depth: 4
    balance: 2
    === Search Transversals ===
    in_order: (2, 5, 6, 7, 8, 9)
    pre_order: (5, 2, 8, 6, 7, 9)
    breadth_first: (5, 2, 8, 6, 9, 7)
    post_order: (2, 7, 6, 9, 8, 5)
    """
    from bst import Bst
    return Bst([5, 8, 6, 9, 2, 7])


@pytest.fixture
def bst_100_rand():
    """100 random numbers in bst."""
    from bst import Bst
    from random import shuffle
    rando = [num for num in range(100)]
    shuffle(rando)
    tree = Bst(rando)
    return tree


def test_initalizing_with_non_iterable_or_not_numbers_raises_ValueError():
    """Init returns Value error with with non-numbers or non-iterables."""
    from bst import Bst
    with pytest.raises(TypeError):
        Bst("dfsdfadgasdg")


def test_insert_must_be_a_number(bst_empty):
    """Raise TypeError on non number insert."""
    with pytest.raises(TypeError):
        bst_empty.insert("dfsdfadgasdg")


def test_insert_to_empty_tree_increases_tree_length(bst_empty):
    """Insert increses length."""
    bst_empty.insert(1)
    assert len(bst_empty) == 1


def test_insert_adds_value_to_tree(bst_balanced):
    """Value added to tree."""
    bst_balanced.insert(15)
    assert bst_balanced.contains(15) is True
    assert bst_balanced.search(15).val == 15


def test_insert_will_not_duplicate_value(bst_balanced):
    """Value not added twice."""
    bst_balanced.insert(6)
    assert bst_balanced.size() == 6


def test_insert_to_balanced_tree_changes_balance(bst_balanced):
    """Balance changes."""
    assert bst_balanced.balance() == 0
    bst_balanced.insert(4)
    assert bst_balanced.balance() == -1


def test_search_finds_node(bst_balanced):
    """Search returns node with value."""
    assert bst_balanced.search(1).val == 1


def test_search_returns_none_when_value_not_in_tree_right(bst_balanced):
    """Search returns None."""
    assert bst_balanced.search(25) is None


def test_search_returns_none_when_value_notin_tree_left(bst_left_balance):
    """Catch case value less than tree values."""
    assert bst_left_balance.search(0) is None


def test_size_is_correct_on_empty_tree(bst_empty):
    """Tree size is accurate."""
    assert bst_empty.size() == 0


def test_size_is_correct_on_filled_tree(bst_100_rand):
    """Tree size is accurate."""
    assert bst_100_rand.size() == 100


def test_depth_returns_zero_on_empty_tree(bst_empty):
    """Return 0 on empty tree."""
    assert bst_empty.depth() == 0


def test_depth_returns_correct_value_balanced_tree(bst_balanced):
    """Return value on tree."""
    assert bst_balanced.depth() == 3


def test_depth_returns_correct_value_right_balanced_tree(bst_right_balance):
    """Return value on empty tree."""
    assert bst_right_balance.depth() == 4


def test_depth_returns_correct_value_left_balanced_tree(bst_left_balance):
    """Return value on empty tree."""
    assert bst_left_balance.depth() == 5


def test_contains_returns_false_on_empty_tree(bst_empty):
    """False on empty tree."""
    assert bst_empty.contains(4) is False


def test_contains_returns_false_on_balanced_tree(bst_balanced):
    """False on balanced tree."""
    assert bst_balanced.contains(25) is False


def test_contains_returns_false_on_right_balanced_tree(bst_right_balance):
    """False on right balanced tree."""
    assert bst_right_balance.contains(25) is False


def test_contains_returns_false_on_left_balanced_tree(bst_left_balance):
    """False on left balanced tree."""
    assert bst_left_balance.contains(25) is False


def test_contains_returns_true_on_tree_with_value_left(bst_left_balance):
    """Tree has value true."""
    assert bst_left_balance.contains(3) is True
    assert bst_left_balance.contains(1) is True
    assert bst_left_balance.contains(2) is True


def test_contains_returns_true_on_tree_with_value_right(bst_right_balance):
    """Tree has value true."""
    assert bst_right_balance.contains(6) is True
    assert bst_right_balance.contains(2) is True


def test_contains_returns_true_on_tree_with_value(bst_balanced):
    """Tree has value true."""
    assert bst_balanced.contains(6) is True
    assert bst_balanced.contains(3) is True


def test_balance_right_tree(bst_right_balance):
    """Tree balanced right returns 2."""
    assert bst_right_balance.balance() == 2


def test_balance_left_tree(bst_left_balance):
    """Tree balanced right returns -4."""
    assert bst_left_balance.balance() == -4


def test_balance_balanced_tree(bst_balanced):
    """Tree balanced right returns 0."""
    assert bst_balanced.balance() == 0


def test_balance_empty_tree(bst_empty):
    """Tree balanced right returns 0."""
    assert bst_empty.balance() == 0

# =================== Transversal Tests ================== #


@pytest.fixture
def bst_wiki():
    r"""Wikipedia's example tree structure.

                      6
                   /     \
                  2       7
                /   \      \
               1     4      9
                    /  \    /
                   3    5  8
    depth: 4
    balance: 0
    === Search Transversals ===
    in_order: (1, 2, 3, 4, 5, 6, 7, 8, 9)
    pre_order: (6, 2, 1, 4, 3, 5, 7, 9, 8)
    breadth_first: (6, 2, 7, 1, 4, 9, 3, 5, 8)
    post_order: (1, 3, 5, 4, 2, 8, 9, 7, 6)
    """
    from bst import Bst
    tree = Bst([6, 7, 9, 8, 2, 1, 4, 3, 5])
    return tree


def test_in_order_0_0(bst_empty):
    """Test in order Transversal with various tress."""
    assert tuple(bst_empty.in_order()) == ()


def test_in_order_one_item_tree(bst_empty):
    """Test in order works on one item tree."""
    bst_empty.insert(10)
    assert next(bst_empty.in_order()) == 10


def test_in_order_0_1(bst_balanced):
    """Test in order Transversal with various tress."""
    assert tuple(bst_balanced.in_order()) == (1, 2, 3, 5, 6, 7)


def test_in_order_0_2(bst_left_balance):
    """Test in order Transversal with various tress."""
    assert tuple(bst_left_balance.in_order()) == (1, 2, 3, 4, 5)


def test_in_order_0_3(bst_right_balance):
    """Test in order Transversal with various tress."""
    assert tuple(bst_right_balance.in_order()) == (2, 5, 6, 7, 8, 9)


def testin_order_0_4(bst_wiki):
    """Test in order Transversal with various tress."""
    assert tuple(bst_wiki.in_order()) == (1, 2, 3, 4, 5, 6, 7, 8, 9)


def test_pre_order_0_0(bst_empty):
    """Test pre order Transversal with various tress."""
    assert tuple(bst_empty.pre_order()) == ()


def test_pre_order_0_1(bst_balanced):
    """Test pre order Transversal with various tress."""
    assert tuple(bst_balanced.pre_order()) == (5, 2, 1, 3, 6, 7)


def test_pre_order_0_2(bst_left_balance):
    """Test pre order Transversal with various tress."""
    assert tuple(bst_left_balance.pre_order()) == (5, 4, 1, 3, 2)


def test_pre_order_0_3(bst_right_balance):
    """Test pre order Transversal with various tress."""
    assert tuple(bst_right_balance.pre_order()) == (5, 2, 8, 6, 7, 9)


def test_pre_order_0_4(bst_wiki):
    """Test pre order Transversal with various tress."""
    assert tuple(bst_wiki.pre_order()) == (6, 2, 1, 4, 3, 5, 7, 9, 8)


def test_post_order_0_0(bst_empty):
    """Test post_order Transversal with various tress."""
    assert tuple(bst_empty.post_order()) == ()


def test_post_order_0_1(bst_balanced):
    """Test post_order Transversal with various tress."""
    assert tuple(bst_balanced.post_order()) == (1, 3, 2, 7, 6, 5)


def test_post_order_0_2(bst_left_balance):
    """Test post_order Transversal with various tress."""
    assert tuple(bst_left_balance.post_order()) == (2, 3, 1, 4, 5)


def test_post_order_0_3(bst_right_balance):
    """Test post_order Transversal with various tress."""
    assert tuple(bst_right_balance.post_order()) == (2, 7, 6, 9, 8, 5)


def test_post_order_0_4(bst_wiki):
    """Test post_order Transversal with various tress."""
    assert tuple(bst_wiki.post_order()) == (1, 3, 5, 4, 2, 8, 9, 7, 6)


def test_breadth_first_0_0(bst_empty):
    """Test breadth_first Transversal with various tress."""
    assert tuple(bst_empty.breadth_first()) == ()


def test_breadth_first_0_1(bst_balanced):
    """Test breadth_first Transversal with various tress."""
    assert tuple(bst_balanced.breadth_first()) == (5, 2, 6, 1, 3, 7)


def test_breadth_first_0_2(bst_left_balance):
    """Test breadth_first Transversal with various tress."""
    assert tuple(bst_left_balance.breadth_first()) == (5, 4, 1, 3, 2)


def test_breadth_first_0_3(bst_right_balance):
    """Test breadth_first Transversal with various tress."""
    assert tuple(bst_right_balance.breadth_first()) == (5, 2, 8, 6, 9, 7)


def test_breadth_first_0_4(bst_wiki):
    """Test breadth_first Transversal with various tress."""
    assert tuple(bst_wiki.breadth_first()) == (6, 2, 7, 1, 4, 9, 3, 5, 8)


# ===================  Delete Tests ===================== #


@pytest.fixture
def three():
    """Create three item tree."""
    from bst import Bst
    tree = Bst([2, 1, 3])
    return tree


@pytest.fixture
def comp():
    r"""Create Large binary tree.

                          10
                      /        \
                    6           13
                  /   \        /  \
                4      8     11    14
                      / \     \     \
                     7   9    12    15
    in_order (4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    """
    from bst import Bst
    return Bst([10, 6, 4, 8, 7, 9, 13, 11, 14, 12, 15])


@pytest.fixture
def right_left_most_has_right_child():
    r"""Large binary tree.

                     1
                      \
                       5
                     /  \
                    3    10
                        / \
                       8   20
                      /
                     6
                      \
                       7
    Depth: 6
    """
    from bst import Bst
    return Bst([1, 5, 3, 10, 8, 6, 20, 7])


def test_del_right_left_most_has_right_child(right_left_most_has_right_child):
    """Delete one child deletion test."""
    right_left_most_has_right_child.delete(5)
    assert tuple(right_left_most_has_right_child.in_order()) == (
        1, 3, 6, 7, 8, 10, 20
    )


def test_handle_root_deletion(right_left_most_has_right_child):
    """Remove root retains tree."""
    right_left_most_has_right_child.delete(1)
    assert tuple(right_left_most_has_right_child.in_order()) == (
        3, 5, 6, 7, 8, 10, 20
    )


def test_delete_retains_depth(comp):
    """Depth correnctly retained through series of deletions."""
    assert comp.depth() == 4
    comp.delete(7)
    assert tuple(comp.in_order()) == (4, 6, 8, 9, 10, 11, 12, 13, 14, 15)
    comp.delete(9)
    assert comp.depth() == 4
    comp.delete(12)
    comp.delete(15)
    assert comp.depth() == 3
    comp.delete(11)
    comp.delete(14)
    assert comp.depth() == 3
    comp.delete(4)
    comp.delete(8)
    assert comp.depth() == 2
    comp.delete(6)
    assert comp.depth() == 2
    assert tuple(comp.in_order()) == (10, 13)
    comp.delete(10)
    assert next(comp.in_order()) == 13
    assert comp.depth() == 1
    comp.delete(13)
    assert comp.depth() == 0
    comp.delete(666)
    assert comp.depth() == 0


def test_balance_value(comp):
    """Balance value correnctly tracked through series of deletions."""
    assert comp.balance() == 0
    comp.delete(7)
    comp.delete(9)
    assert comp.balance() == 1
    comp.delete(12)
    comp.delete(15)
    assert comp.balance() == 0
    comp.delete(11)
    assert comp.balance() == 0
    comp.delete(14)
    assert comp.balance() == -1
    comp.delete(4)
    comp.delete(8)
    assert comp.balance() == 0
    comp.delete(6)
    assert comp.balance() == 1
    comp.delete(10)
    assert comp.balance() == 0
    comp.delete(13)
    assert comp.balance() == 0


def test_delete_node_empty_returns_none(bst_empty):
    """Test delete with empty bst."""
    assert bst_empty.delete(5) is None


def test_delete_on_empty_bst_leaves_bst_intact(bst_empty):
    """Pretty verbose test name."""
    bst_empty.delete(1)
    assert bst_empty._root is None


def test_delete_tree_with_one_node_leaves_empty_tree(bst_empty):
    """Delete single node."""
    bst_empty.insert(1)
    assert bst_empty.delete(1) is None
    with pytest.raises(AttributeError):
        bst_empty._root.val
    assert bst_empty.size() == 0


def test_delete_two_node_left_balanced_tree_01(bst_empty):
    """Delete root node shifts other node."""
    bst_empty.insert(2)
    bst_empty.insert(1)
    bst_empty.delete(2)
    assert bst_empty._root.val == 1
    assert bst_empty._root.left is None


def test_delete_two_node_left_balanced_tree_02(bst_empty):
    """Delete last node leaves one node tree."""
    bst_empty.insert(2)
    bst_empty.insert(1)
    bst_empty.delete(1)
    assert bst_empty._root.val == 2
    assert bst_empty._root.right is None
    assert bst_empty._root.left is None
    # assert len(bst_empty) == 1


def test_delete_left_tree_single_child(bst_left_balance):
    """One child deletion test."""
    bst_left_balance.delete(4)
    assert bst_left_balance.search(3).val == 3
    assert bst_left_balance.search(4) is None


def test_delete_two_node_right_balanced_tree_01(bst_empty):
    """Delete root node shifts other node."""
    bst_empty.insert(1)
    bst_empty.insert(3)
    bst_empty.delete(1)
    assert bst_empty._root.val == 3
    assert bst_empty._root.left is None


def test_delete_two_node_right_balanced_tree_02(bst_empty):
    """Delete last node leaves one node tree."""
    bst_empty.insert(1)
    bst_empty.insert(3)
    bst_empty.delete(3)
    assert bst_empty._root.val == 1
    assert bst_empty._root.right is None
    assert bst_empty._root.left is None
    assert len(bst_empty) == 1


def test_delete_three_node_tree_01(three):
    """Delete route node leaves tree in correct order."""
    three.delete(2)
    assert three._root.val == 3
    assert three._root.right is None
    assert three._root.left.val == 1
    assert tuple(three.in_order()) == (1, 3)


def test_delete_three_node_tree_02(three):
    """Delete left node leaves tree in order."""
    three.delete(1)
    assert three._root.val == 2
    assert three._root.right.val == 3
    assert three._root.left is None
    assert tuple(three.in_order()) == (2, 3)


def test_delete_three_node_tree_03(three):
    """Delete right node leaves tree in order."""
    three.delete(3)
    assert three._root.val == 2
    assert three._root.right is None
    assert three._root.left.val == 1
    assert tuple(three.in_order()) == (1, 2)


def test_delete_complex_tree_01(comp):
    """Delete route 10."""
    comp.delete(10)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 11, 12, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (11, 6, 13, 4, 8, 12, 14, 7, 9, 15)


def test_delete_complex_tree_02(comp):
    """Delete left most 4."""
    comp.delete(4)
    assert tuple(comp.in_order()) == (6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (10, 6, 13, 8, 11, 14, 7, 9, 12, 15)


def test_delete_complex_tree_03(comp):
    """Delete right most 15."""
    comp.delete(15)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    assert tuple(comp.breadth_first()) == (10, 6, 13, 4, 8, 11, 14, 7, 9, 12)


def test_delete_complex_tree_04(comp):
    """Delete mid right 13."""
    comp.delete(13)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 11, 12, 14, 15)
    assert tuple(comp.breadth_first()) == (10, 6, 14, 4, 8, 11, 15, 7, 9, 12)


def test_delete_complex_tree_05(comp):
    """Delete mid left 8."""
    comp.delete(8)
    assert tuple(comp.in_order()) == (4, 6, 7, 9, 10, 11, 12, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (10, 6, 13, 4, 9, 11, 14, 7, 12, 15)


def test_delete_complex_tree_06(comp):
    """Delete bottom left 9."""
    comp.delete(9)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 10, 11, 12, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (10, 6, 13, 4, 8, 11, 14, 7, 12, 15)


def test_delete_complex_tree_07(comp):
    """Delete bottom right 12."""
    comp.delete(12)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 11, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (10, 6, 13, 4, 8, 11, 14, 7, 9, 15)


def test_delete_complex_tree_08(comp):
    """Delete mid bottom right 11."""
    comp.delete(11)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 12, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (10, 6, 13, 4, 8, 12, 14, 7, 9, 15)


@pytest.fixture
def robust():
    r"""More robust tree.

                   10
                /      \
             2           18
           /   \        /  \
          1     9      11   19
               /        \
              4          16
            /  \        /  \
           3    8      12   17
               /        \
              6          14
            /  \        /  \
           5    7     13   15
    """
    from bst import Bst
    return Bst([
        10, 2, 1, 9, 4, 3, 8, 6, 5, 7, 18, 11, 19, 16, 12, 17, 14, 13, 15
    ])


def test_del_handles_multiple_place_changes(robust):
    """Delete a node that requires multiple changes to correct."""
    robust.delete(9)
    assert robust.balance() == 1
    assert tuple(robust.in_order()) == (
        1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
    )
    robust.delete(10)
    assert tuple(robust.in_order()) == (
        1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19
    )
    assert robust.balance() == 0
    assert robust.depth() == 6
    robust.delete(19)
    robust.delete(11)
    robust.delete(12)
    assert tuple(robust.in_order()) == (
        1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 15, 16, 17, 18
    )
    assert robust.balance() == 0
    assert robust.depth() == 5


# ========= depth test, just becasue =========== #


def test_robust_depth(robust):
    """Robust depth is 7."""
    assert robust.depth() == 7


def test_right_left_most_has_right_child(right_left_most_has_right_child):
    """Depth of right_left_most_has_right_child is 6."""
    assert right_left_most_has_right_child.depth() == 6


def test_comp(comp):
    """Depth of comp is 4."""
    assert comp.depth() == 4


def test_three(three):
    """Depth of three is 2."""
    assert three.depth() == 2


def test_bst_wiki(bst_wiki):
    """Depth of bst_wiki is 4."""
    assert bst_wiki.depth() == 4


def test_bst_right_balance(bst_right_balance):
    """Depth of bst_right_balance is 4."""
    assert bst_right_balance.depth() == 4


def test_bst_balanced(bst_balanced):
    """Depth of bst_balanced is 3."""
    assert bst_balanced.depth() == 3


def test_bst_left_balance(bst_left_balance):
    """Depth of bst_left_balance is 5."""
    assert bst_left_balance.depth() == 5


def test_bst_empty(bst_empty):
    """Depth of bst_empty is 0."""
    assert bst_empty.depth() == 0


def test_bst_long_and_left():
    """Long left bst."""
    from bst import Bst
    bst = Bst([x for x in range(1, 100)])
    assert bst.depth() == 99
