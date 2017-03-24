import math
import pytest
from mesh3d.shapes.line import *
from mesh3d.shapes.vertex import *


class TestLine:

    def test_line_contructor_not_none(self):
        self.my_line = Line(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert self.my_line is not None

    def test_line_start_vertex(self):
        """Constructor test."""
        self.my_line = Line(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert self.my_line.start == Vertex(0, 0, 0)

    def test_line_end_vertex(self):
        """Constructor test."""
        self.my_line = Line(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert self.my_line.end == Vertex(1, 1, 1)

    def test_line_slope(self):
        """Constructor test."""
        self.my_line = Line(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert (self.my_line.slope, 1.0)

    def test_line_midpoint(self):
        """Midpoint test."""
        self.my_line = Line(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert (self.my_line.midpoint, Vertex(0.5, 0.5, 0.5))

    def test_line_length(self):
        """Length test."""
        self.my_line = Line(Vertex(0, 0, 0), Vertex(1, 1, 1))
        length = math.sqrt(math.pow(1.0, 2) + math.pow(1.0, 2))
        assert (self.my_line.length, length)
