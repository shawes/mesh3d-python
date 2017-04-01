import math
import pytest
from .context import mesh3d


class TestQuadrilateral:

    def test_quad_contains(self):
        box = Quadrilateral(Vertex(0,0,0), Vertex(0,1,0), Vertex(1,1,0), Vertex(1,0,0))
        point = Vertex(0.5,0.5,0)
        assert box.contains(point) is True