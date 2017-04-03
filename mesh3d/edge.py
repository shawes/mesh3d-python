import math
from vertex import Vertex

class Edge(object):
    """Class Edge represents the edge of a feature object."""

    def __init__(self, start, end):
        """Constructor takes a start and end vertex."""
        self.start = start
        self.end = end
        self.midpoint = Vertex((start.x + end.x) / 2,
                               (start.y + end.y) / 2,
                               (start.z + end.z) / 2)
        _x_displacement = float(end.x - start.x)
        _y_displacement = float(end.y - start.y)
        _z_displacement = float(end.z - start.z)
        #self.slope = _y_displacement / _x_displacement  # TODO: Check for 0 demoninator
        self.length = math.sqrt(math.pow(_x_displacement, 2) +
                                math.pow(_y_displacement, 2) +
                                math.pow(_z_displacement, 2))


    # def slope(self):
    #     """Get the slope of the Edge."""
    #     return
    #
    # def midpoint(self):
    #     """Get the midpoint of the Edge."""
    #     return
    #
    # def length(self):
    #     """Get the length of the Edge."""
    #     return
