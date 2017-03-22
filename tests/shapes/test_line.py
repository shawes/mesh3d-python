import unittest
import math
from nose.tools import *
from mesh3d.shapes.line import Line
from mesh3d.shapes.vertex import Vertex


class TestLine(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_line_contructor(self):
        """Constructor test."""
        test_line = Line(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert test_line is not None
        assert test_line.start == Vertex(0, 0, 0)
        assert test_line.end == Vertex(1, 1, 1)
        assert test_line.x_displacement == 1
        assert test_line.y_displacement == 1

    def test_slope(self):
        """Slope test."""
        test_line = Line(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert test_line.slope() == 1

    def test_midpoint(self):
        """Midpoint test."""
        test_line = Line(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert test_line.midpoint() == Vertex(0.5, 0.5, 0.5)

    def test_length(self):
        test_line = Line(Vertex(0, 0, 0), Vertex(1, 1, 1))
        assert test_line.length() == math.sqrt(pow(1, 2) + pow(1, 2))
