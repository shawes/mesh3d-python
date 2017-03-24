"""face.py."""
import math
from vertex import Vertex


class Face(object):
    """Class representing a face."""

    def __init__(self, vertex1, vertex2, vertex3):
        """Constructor."""
        self.v1 = vertex1
        self.v2 = vertex2
        self.v3 = vertex3

    def centroid(self):
        """Get the centroid of the face."""
        return Vertex((self.v1.x + self.v2.x + self.v3.x) / 3,
                      (self.v1.y + self.v2.y + self.v3.y) / 3,
                      (self.v1.z + self.v2.z + self.v3.z) / 3)

    def get_area_3d(self):
        """Get the 3-dimensional area of the face."""
        edge1 = self.v1.distance_to_xyz(self.v2)
        edge2 = self.v2.distance_to_xyz(self.v3)
        edge3 = self.v3.distance_to_xyz(self.v1)
        return self._area(edge1, edge2, edge3)

    def get_area_2d(self):
        """Get the 2-dimensional area of the face."""
        edge1 = self.v1.distance_to_xy(self.v2)
        edge2 = self.v2.distance_to_xy(self.v3)
        edge3 = self.v3.distance_to_xy(self.v1)
        return self._area(edge1, edge2, edge3)

    def _area(self, edge1, edge2, edge3):
        semiperimeter = (edge1 + edge2 + edge3) * 0.5
        area = math.sqrt(semiperimeter * (semiperimeter - edge1) *
                         (semiperimeter - edge2) * (semiperimeter - edge3))
        return area

    def __str__(self):
        print("centroid is " + self.centroid())
