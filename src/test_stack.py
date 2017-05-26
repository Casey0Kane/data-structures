"""Module test linked list."""
from stack import Stack
import pytest


@pytest.fixture
def stack():
    """Create a stack fixture."""
    from stack import Stack
    stack = Stack()
    return stack


@pytest.fixture
def stack_of_five_pancakes(stack):
    """Create a stack with five items."""
    from stack import Stack
    stack = Stack(
        ['plate'] + ['pancake' for pancake in range(3)] + ['strawberry syrup'])
    return stack


def test_stack_init(stack):
    """Can be Initalized with iterable or nothing only."""
    assert stack._stack.head is None


def test_stack_init_five(stack_of_five_pancakes):
    """Testing the init method with five pancakes, yumm."""
    assert stack_of_five_pancakes._stack.head.value == 'strawberry syrup'
    assert stack_of_five_pancakes._stack.head.next_node.value == 'pancake'
    a_few_pancakes = stack_of_five_pancakes._stack.head.next_node.next_node
    assert a_few_pancakes.next_node.next_node.value == 'plate'


def test_stack_init_raises_typeerror():
    """Can't initialize with value."""
    with pytest.raises(TypeError):
        Stack(5)


def test_push_five_pancakes(stack_of_five_pancakes):
    """Add 5 nodes to stack."""
    assert stack_of_five_pancakes._stack.head.value == 'strawberry syrup'


def test_pop_five_pancakes(stack_of_five_pancakes):
    """Pop resets _stack.head's value to previous value."""
    assert stack_of_five_pancakes.pop() == 'strawberry syrup'
    assert stack_of_five_pancakes._stack.head.value == 'pancake'


def test_pop_from_empty_stack(stack):
    """Pop raises error on empy list."""
    assert stack.pop() == "Can not pop from empty list."


def test_len_empty_stack(stack):
    """Testing length of empty stack."""
    assert len(stack) == 0


def test_len_stack_of_five(stack_of_five_pancakes):
    """Test length of stack with five items."""
    assert len(stack_of_five_pancakes) == 5
