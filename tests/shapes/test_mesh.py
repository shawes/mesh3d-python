from nose.tools import *
from src.shapes.mesh import Mesh
from src.shapes.vertex import Vertex


def test_contructor():
    """Constructor test."""
    test_vertex = Vertex(1, 2, 3)
    assert_equal(test_vertex.x, 1)
    assert_equal(test_vertex.y, 2)
    assert_equal(test_vertex.z, 3)
