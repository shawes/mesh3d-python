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
                               0)
        self.area3d = self._area_3d()
        self.area2d = self._area_2d()
        # print("3d: " + str(self.area3d) + ", 2d: " + str(self.area2d))
        # if self.area3d == 0:
        #     print("v1: " + str(vertex1))
        #     print("v2: " + str(vertex2))
        #     print("v3: " + str(vertex3))

        # self.edges = [Edge(vertex1, vertex2), Edge(
        #     vertex2, vertex3), Edge(vertex3, vertex1)]
        # self.edges_xy = [Edge(vertex1.make_xy(), vertex2.make_xy()), Edge(vertex2.make_xy(), vertex3.make_xy()),
        #                   Edge(vertex3.make_xy(), vertex1.make_xy())]
        # self.area3d = self._calc_area3d(vertices[0], vertices[1], vertices[2])
        # self.area2d = self._calc_area2d(vertices[0], vertices[1],
        # vertices[2])


    def _area_3d(self):
        edge1 = self.vertices[0].distance_to_xyz(self.vertices[1])
        edge2 = self.vertices[1].distance_to_xyz(self.vertices[2])
        edge3 = self.vertices[2].distance_to_xyz(self.vertices[0])
        return self._get_area(edge1, edge2, edge3)

    def _area_2d(self):
        edge1_xy = self.vertices[0].distance_to_xy(self.vertices[1])
        edge2_xy = self.vertices[1].distance_to_xy(self.vertices[2])
        edge3_xy = self.vertices[2].distance_to_xy(self.vertices[0])
        return self._get_area(edge1_xy, edge2_xy, edge3_xy)

    def _get_area(self, edge1, edge2, edge3):
        semiperimeter = (edge1 + edge2 + edge3) * 0.5
        #print("sp: "+ str(semiperimeter))
        result = math.sqrt(semiperimeter * (semiperimeter - edge1) * (semiperimeter - edge2) * (semiperimeter - edge3))
        return result

    def __str__(self):
        print("centroid is " + str(self.centroid))
