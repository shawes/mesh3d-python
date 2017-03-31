import math
import pytest
from mesh3d.shapes.edge import Edge
from mesh3d.shapes.vertex import Vertex
from mesh3d.shapes.quadrilateral import Quadrilateral


class TestQuadrilateral:

    def test_quad_contains(self):
        box = Quadrilateral(Vertex(0,0,0), Vertex(0,1,0), Vertex(1,1,0), Vertex(1,0,0))
        point = Vertex(0.5,0.5,0)
        assert box.contains(point) is True
