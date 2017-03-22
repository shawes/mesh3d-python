"""Class for vertex."""
import math


class Vertex(object):
    """Vertex class."""

    def __init__(self, x, y, z):
        """Create a vertex with three points, x, y & z."""
        self.x = x
        self.y = y
        self.z = z

    def distance_to_xyz(self, to_vertex):
        """Get the distance between vertexs in XYZ plane."""
        return math.sqrt(math.pow(to_vertex.x - self.x, 2) +
                         math.pow(to_vertex.y - self.y, 2) +
                         math.pow(to_vertex.z - self.z, 2))

    def distance_to_xy(self, to_vertex):
        """Get the distance between vertexs in XY plane."""
        return math.sqrt(math.pow(to_vertex.x - self.x, 2) +
                         math.pow(to_vertex.y - self.y, 2))

    def __str__(self):
        """Pretty prints the vertex."""
        print("x=" + self.x + ", y=" + self.y + ", z=" + self.z)

    def __eq__(self, other):
        """Check the vertex equals another, returns a Boolean."""
        if type(other) is type(self):
            return (self.x == other.x & self.y == other.y & self.z == other.z)
        return False

    def __hash__(self):
        """Hash code for vertex."""
        return hash(self.x, self.y, self.z)
