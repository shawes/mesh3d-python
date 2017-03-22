import math
from vertex import Vertex


class Line(object):
    """Class Line represents a line object."""

    def __init__(self, start, end):
        """Constructor takes a start and end vertex."""
        self.start = start
        self.end = end
        self._x_displacement = end.x - start.x
        self._y_displacement = end.y - start.y

    def slope(self):
        """Get the slope of the line."""
        return self.y_displacement / self.x_displacement

    def midpoint(self):
        """Get the midpoint of the line."""
        return Vertex((self.start.x + self.end.x) / 2,
                      (self.start.y + self.end.y) / 2,
                      (self.start.z + self.end.z) / 2)

    def length(self):
        """Get the length of the line."""
        return math.sqrt(math.pow(self.x_displacement, 2) +
                         math.pow(self.y_displacement, 2))
