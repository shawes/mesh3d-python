import pytest
from mesh3d.shapes.vertex import Vertex


class TestVertex:

    def test_vertex_contructor(self):
        vertex = Vertex(1, 2, 3)
        assert vertex is not None

    def test_vertex_x(self):
        vertex = Vertex(1, 2, 3)
        assert (vertex.x, 1)

    def test_vertex_y(self):
        vertex = Vertex(1, 2, 3)
        assert (vertex.y, 2)

    def test_vertex_z(self):
        vertex = Vertex(1, 2, 3)
        assert (vertex.z, 3)
