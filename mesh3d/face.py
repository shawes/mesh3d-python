import math
from vertex import Vertex
from edge import Edge
# import pdb


class Face(object):
    """Class representing a face."""

    def __init__(self, vertex1, vertex2, vertex3):
        """Constructor."""
        self.vertices = [vertex1, vertex2, vertex3]
        self.centroid = Vertex((vertex1.x + vertex2.x + vertex3.x) / 3,
                               (vertex1.y + vertex2.y + vertex3.y) / 3,
                               (vertex1.z + vertex2.z + vertex3.z) / 3)
        # self.edges = [Edge(vertex1, vertex2), Edge(
        #     vertex2, vertex3), Edge(vertex3, vertex1)]
        # self.edges_xy = [Edge(vertex1.make_xy(), vertex2.make_xy()), Edge(vertex2.make_xy(), vertex3.make_xy()),
        #                   Edge(vertex3.make_xy(), vertex1.make_xy())]
        # self.area3d = self._calc_area3d(vertices[0], vertices[1], vertices[2])
        # self.area2d = self._calc_area2d(vertices[0], vertices[1],
        # vertices[2])


    def area_3d(self):
        edge1 = self.vertices[0].distance_to_xyz(self.vertices[1])
        edge2 = self.vertices[1].distance_to_xyz(self.vertices[2])
        edge3 = self.vertices[2].distance_to_xyz(self.vertices[0])
        return self._get_area(edge1, edge2, edge3)

    def area_2d(self):
        edge1 = self.vertices[0].distance_to_xy(self.vertices[1])
        edge2 = self.vertices[1].distance_to_xy(self.vertices[2])
        edge3 = self.vertices[2].distance_to_xy(self.vertices[0])
        return self._get_area(edge1, edge2, edge3)

    def _get_area(self, edge1, edge2, edge3):
        semiperimeter = (edge1 + edge2 + edge3) * 0.5
        #print("sp: "+ str(semiperimeter))
        result = math.sqrt(semiperimeter * (semiperimeter - edge1) * (semiperimeter - edge2) * (semiperimeter - edge3))
        return result

    def __str__(self):
        print("centroid is " + str(self.centroid))