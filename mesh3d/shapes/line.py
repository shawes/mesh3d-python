import math
from vertex import Vertex

class Line(object):
    """Class Line represents a line object."""

    def __init__(self, start, end):
        """Constructor takes a start and end vertex."""
        self.start = start
        self.end = end
        self.midpoint = Vertex((start.x + end.x) / 2,
                               (start.y + end.y) / 2,
                               (start.z + end.z) / 2)
        self.length = math.sqrt(math.pow(self.x_displacement, 2) +
                                math.pow(self.y_displacement, 2))
        _x_displacement = float(end.x - start.x)
        _y_displacement = float(end.y - start.y)
        self.slope = y_displacement / x_displacement

    # def slope(self):
    #     """Get the slope of the line."""
    #     return
    #
    # def midpoint(self):
    #     """Get the midpoint of the line."""
    #     return
    #
    # def length(self):
    #     """Get the length of the line."""
    #     return
