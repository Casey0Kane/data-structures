"""Module tests the graph datastructure."""
import pytest


@pytest.fixture
def empty_graph():
    """Create an empty graph."""
    from graph_1 import Graph
    return Graph()


@pytest.fixture
def tri_graph(empty_graph):
    """Create a graph with 3 nodes one pointing to next in circle."""
    new_graph = empty_graph
    empty_graph.add_node(1)
    empty_graph.add_node(2)
    empty_graph.add_node(3)
    empty_graph.add_edge(1, 2)
    empty_graph.add_edge(2, 3)
    empty_graph.add_edge(3, 1)
    return new_graph


def test_init_creates_empty_graph(empty_graph):
        """Initialize and empty graph."""
        assert empty_graph.nodes() == []


def test_nodes_returns_list_of_all_nodes(tri_graph):
    """Return a list of all nodes in the graph."""
    assert tri_graph.nodes() == [1, 2, 3]


def test_edges_returns_list_of_all_edges(tri_graph):
    """Return a list of all edges in the graph."""
    tri_graph.add_edge(3, 2)
    assert tri_graph.edges() == [(1, 2), (2, 3), (3, 1), (3, 2)]


def test_add_node_adds_node(empty_graph):
    """Add a new node with value 'val' to the graph."""
    empty_graph.add_node('test')
    assert empty_graph.nodes() == ['test']


def test_add_edge_adds_an_edge(tri_graph):
    """Add a new edge to the graph."""
    tri_graph.add_edge(3, 2)
    assert tri_graph.neighbors(3) == [1, 2]


def test_del_node_removes_a_node(tri_graph):
    """Delete the node containing 'val' from the graph."""
    tri_graph.del_node(3)
    assert tri_graph.nodes() == [1, 2]


def test_del_node_3_and_check_two_has_no_neighbors(tri_graph):
    """Delete the node containing 3 and check that 2 has no neighbors."""
    tri_graph.del_node(3)
    assert tri_graph.neighbors(2) == []


def test_del_node_raises_ValueError_when_node_not_in_graph(tri_graph):
    """Raise an error if no such node exists."""
    with pytest.raises(ValueError):
        tri_graph.del_node(10)


def test_del_edge_removes_edge_from_node(tri_graph):
    """Delete the edge connecting 'val1' and 'val2' from the graph."""
    tri_graph.del_edge(1, 2)
    assert tri_graph.neighbors(1) == []


def test_del_edge_raises_ValueError_when_edge_not_on_node(tri_graph):
    """Raise an error if no such edge exists."""
    with pytest.raises(ValueError):
        tri_graph.del_edge(1, 3)


def test_has_node_returns_true_or_false_if_node_present_or_not(tri_graph):
    """True if node containing 'val' is in the graph, False if not."""
    assert tri_graph.has_node(4) is False
    assert tri_graph.has_node(1) is True


def test_neighbors_returns_list_of_neighbors(tri_graph):
    """Return the list of all nodes connected to the node."""
    tri_graph.add_edge(3, 2)
    assert tri_graph.neighbors(3) == [1, 2]


def test_neighbors_raises_ValueError_if_node_not_in_graph(tri_graph):
    """Return the list of all nodes connected to the node."""
    with pytest.raises(ValueError):
        tri_graph.neighbors(4)


def test_adjacent_returns_true_or_false_if_node_has_the_edge_not(tri_graph):
    """Return True if there is an edge connecting val1 and val2."""
    assert tri_graph.adjacent(1, 2) is True
    assert tri_graph.adjacent(1, 3) is False


def test_adjacent_raises_ValueError_if_either_are_not_in_graph(tri_graph):
    """Raise an error if either of the supplied values are not in graph."""
    with pytest.raises(ValueError):
        tri_graph.adjacent(1, 4)
    with pytest.raises(ValueError):
        tri_graph.adjacent(4, 1)