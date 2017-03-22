import unittest
from nose.tools import *
from mesh3d.shapes.vertex import Vertex


class TestVertex(unittest.TestCase):

    def test_vertex_contructor(self):
        """Constructor test."""
        test_vertex = Vertex(1, 2, 3)
        assert_equal(test_vertex.x, 1)
        assert_equal(test_vertex.y, 2)
        assert_equal(test_vertex.z, 3)
