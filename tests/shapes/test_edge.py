import math
import pytest
from mesh3d.shapes.edge import *
from mesh3d.shapes.vertex import *


class Testedge:

    def test_edge_contructor_not_none(self):
        self.my_edge = Edge(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert self.my_edge is not None

    def test_edge_start_vertex(self):
        """Constructor test."""
        self.my_edge = Edge(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert self.my_edge.start == Vertex(0, 0, 0)

    def test_edge_end_vertex(self):
        """Constructor test."""
        self.my_edge = Edge(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert self.my_edge.end == Vertex(1, 1, 1)

    def test_edge_slope(self):
        """Constructor test."""
        self.my_edge = Edge(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert (self.my_edge.slope, 1.0)

    def test_edge_midpoint(self):
        """Midpoint test."""
        self.my_edge = Edge(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert (self.my_edge.midpoint, Vertex(0.5, 0.5, 0.5))

    def test_edge_length(self):
        """Length test."""
        self.my_edge = Edge(Vertex(0, 0, 0), Vertex(1, 1, 1))
        length = math.sqrt(math.pow(1.0, 2) + math.pow(1.0, 2))
        assert (self.my_edge.length, length)
